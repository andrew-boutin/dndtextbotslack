# Copyright (C) 2018, Baking Bits Studios - All Rights Reserved

FROM python:3

RUN mkdir /bot
COPY requirements.txt /bot
WORKDIR /bot

RUN pip install -r requirements.txt
	
EXPOSE 8080
