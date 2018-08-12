# Copyright (C) 2018, Baking Bits Studios - All Rights Reserved
from os import environ
from yaml import load
from simple_slack_bot.simple_slack_bot import SimpleSlackBot

# Read in config from config.yml to set an env var for the Slack bot's API token
f = open('config.yml', 'r')
config = load(f)
f.close()
environ['SLACK_BOT_TOKEN'] = config['slack']['apitoken']

# Creating SimpleSlackBot automatically checks connectivity to the API on startup
simple_slack_bot = SimpleSlackBot(debug=True)
bot_mention = '<@{}>'.format(simple_slack_bot._BOT_ID).lower()


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

    if len(msg_tokens) != 3:
        request.write("expected 3 tokens in command")
        return

    cmd = msg_tokens[1]
    var = msg_tokens[2]

    if cmd == "add":
        # TODO: Add config to store
        request.write(f"adding '{var}'")
        return
    elif cmd == "remove":
        # TODO: Remove config from store
        request.write(f"removing '{var}")
        return
    else:
        # TODO: Pass back valid cmds
        request.write(f"unknown command `{cmd} {var}`")
        return


def handle_msg(request, msg):
    # TODO: Determine if user is registered

    request.write("message")
    # TODO: Handle the user sending a regular message so forward to API


if __name__ == "__main__":
    # This makes the bot actually start listening for traffic
    simple_slack_bot.start()
