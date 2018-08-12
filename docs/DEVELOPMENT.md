# Development

## Prerequisites

Need to install Docker and Docker-Compose first.

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

Another container in the network is a Postgresql database that the bot utilizes.

## Contributors

Add yourself to the [contributors](docs/CONTRIBUTORS.md) list if you contribute!
