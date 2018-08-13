# DnD Text Bot Slack

This is a Slack bot that interfaces with the [DnD Text API](https://github.com/andrew-boutin/dndtextapi). It utilizes [Simple Slack Bot](https://github.com/GregHilston/Simple-Slack-Bot) to make the Slack integration easy.

@mention the bot in Slack with the `add` command and your DnD text character ID. The bot will then send all of your future messages in the channel to the API as if you sent them directly to the API.

    @dndtextbot add 1

@mention the bot in Slack with the `remove` command and your DnD text character ID to stop the bot from sending your messages to the API.

    @dndtextbot remove 1

See [development](DEVELOPMENT.md) for how to get started if you want to run and/or work on this.

TODO:

- pin requests
- Get api auth working
- Redis creds
- Keep ID/name mappings in Redis to cache lookups
- Periodically ping Slack and API for connectivity if no traffic for a while
