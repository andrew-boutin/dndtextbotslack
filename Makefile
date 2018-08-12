# Copyright (C) 2018, Baking Bits Studios - All Rights Reserved

# So we can see what commands get ran from the command line output.
SHELL = sh -xv

.PHONY: all up down

# Take the containers down and then bring them back up
all: down up

# Start up the bot containers
up:
	@docker-compose up -d

# Stop the bot containers
down:
	@docker-compose down
