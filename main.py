# Copyright (C) 2018, Baking Bits Studios - All Rights Reserved
import logging
from os import environ
from yaml import load
from redis import Redis
from dndtextapi_client import DNDTextAPIClient

from simple_slack_bot.simple_slack_bot import SimpleSlackBot

# Read in config from config.yml
f = open('config.yml', 'r')
config = load(f)
f.close()

# Set up config required by simple slack bot
environ['SLACK_BOT_TOKEN'] = config['slack']['apitoken']

# Creating SimpleSlackBot automatically checks connectivity to the API on startup
simple_slack_bot = SimpleSlackBot(debug=True)
bot_mention = '<@{}>'.format(simple_slack_bot._BOT_ID).lower()

# Connect to the Redis store
REDIS_HOST = config['redis']['host']
REDIS_PORT = config['redis']['port']
redis = Redis(host=REDIS_HOST, port=REDIS_PORT)

# TODO: What does __name__ here do?
logger = logging.getLogger(__name__)

API_HOST = config['api']['host']
api_client = DNDTextAPIClient(API_HOST)


@simple_slack_bot.register("message")
def message_receiver(request):
    """
    This automatically hooks the bot up to receive all message events for any
    channel it has been added to.
    """
    if request.message:
        msg = request.message.lower()

        # Determine if the message starts with `@dndtextbot`
        if msg.startswith(bot_mention):
            handle_command(request, msg)
        else:
            handle_msg(request, msg)


def handle_command(request, msg):
    """Figures out what command is being sent and handles it appropriately."""
    msg_tokens = msg.split()
    valid_cmds_msg = "Valid commands:\n\t@dndtextapi add <int>\n\t@dndtextapi remove"

    if len(msg_tokens) not in [2, 3]:
        request.write(valid_cmds_msg)
        return

    cmd = msg_tokens[1]

    # The format is `{channel_name}:{user_name}`
    key = build_key(request)
    cur_val = redis.get(key)

    if cmd == "add":
        if len(msg_tokens) != 3:
            request.write(valid_cmds_msg)
            return

        try:
            val = int(msg_tokens[2])
        except ValueError:
            request.write(valid_cmds_msg)
            return

        if cur_val is not None:
            request.write(f"Already registered character ID `{cur_val}`")
            return

        add_mapping(request, key, val)
    elif cmd == "remove":
        if len(msg_tokens) != 2:
            request.write(valid_cmds_msg)
            return

        if cur_val is None:
            request.write(f"No character ID to remove")
            return

        remove_mapping(request, key, cur_val)
    else:
        request.write(valid_cmds_msg)


def add_mapping(request, key, val):
    # TODO: Attempt to hit API using this config to verify if it's valid.
    redis.set(key, val)
    request.write(f"Added character ID `{val}`")


def remove_mapping(request, key, cur_val):
    redis.delete(key)
    request.write(f"Removed character ID `{cur_val}`")


def handle_msg(request, msg):
    key = build_key(request)
    character_id = redis.get(key)

    if character_id is not None:
        request.write(f"Message from registered user with character ID `{character_id}`")
        # TODO: Handle the user sending a regular message so forward to API


def build_key(request):
    user_name = simple_slack_bot.helper_user_id_to_user_name(request._slack_event.event["user"])

    # TODO: Pull in new version of simple slack bot when updated and switch back to one liner
    # ---
    # channel_name = simple_slack_bot.helper_channel_id_to_channel_name(request.channel)
    channels_list = simple_slack_bot._slacker.channels.list().body["channels"]

    for channel in channels_list:
        if channel["id"] == request.channel:
            channel_name = channel["name"]
            break

    if channel_name is None:
        request.write("Failed to convert channel id to name")
    # ---

    return f'{channel_name}:{user_name}'


if __name__ == "__main__":
    # Check for API connectivity on start up
    api_client.ping()

    # This makes the bot actually start listening for traffic
    simple_slack_bot.start()
