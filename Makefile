# Copyright (C) 2018, Baking Bits Studios - All Rights Reserved

# So we can see what commands get ran from the command line output.
SHELL = sh -xv

.PHONY: all up down newreqs

# Take the containers down and then bring them back up
all: down up

# Start up the bot containers
up:
	@docker-compose up -d

# Stop the bot containers
down:
	@docker-compose down

# Rebuild the Docker containers from scratch. This is required if dependencies in `requirements.txt` are changed.
newreqs:
	@docker-compose build --no-cache

applogs:
	@docker logs -f dndtextbotslack_bot_1
