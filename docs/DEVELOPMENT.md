# Development

## Prerequisites

Need to install Docker and Docker-Compose first.

Follow [Slack Bot Getting Started](https://api.slack.com/bot-users#getting-started) to create a bot in Slack.

Get [`DNDTextAPI`](https://github.com/andrew-boutin/dndtextapi) up and running.

## Setup

Use `example-config.yml` to create a `config.yml` file at the root of the repo.

Fill in the Slack and DnD Text API configuration.

## Running

To start up the Slack bot and database run:

    make

See other commands in the [`Makefile`](Makefile).

## How things work

Makefile defines commands to run.

Docker-compose defines Docker containers to spin up.

One Docker container runs the Python code that makes up the Slack bot. Container based on [`Dockerfile`](Dockerfile) and Python dependencies defined in [`requirements.txt`](requirements.txt).

Another container in the network is a Redis store that the bot utilizes.

## Changing python dependencies

If you need to update existing or add new Python dependencies then modify the [`requirements.txt`](requirements.txt) file.

Then you can run a make cmd to get the container rebuilt since the normal cmds will used the cached version:

    make newreqs

Now you can run the other cmds like normal.

## View redis store

A [`redis-commander`](https://joeferner.github.io/redis-commander/) container is spun up alongside the Redis store. This allows you to browse to `localhost:8082` and view the contents of Redis with your favorite browser.

## Contributors

Add yourself to the [contributors](docs/CONTRIBUTORS.md) list if you contribute!
