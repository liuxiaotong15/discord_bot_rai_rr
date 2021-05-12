FROM python:3.8

WORKDIR /code

RUN pip install discord.py requests

COPY bot.py .

CMD [ "python", "./bot.py" ]