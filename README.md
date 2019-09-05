# Ngrok service

It's a hack to manage ngrok with telegram bot in python.

## Prerequisites

* Create a telegram bot, follow this guide : [https://core.telegram.org/bots](https://core.telegram.org/bots)
* Fill the `.env` file with your credentials correctly.

## Guide

Install requirements modules.

```console
$ python3 -m pip install -r requirements.txt
```

Start the telegram bot daemon.

```console
$ python3 daemon.py start
$ <PID>
```

### Email notification

If you want to send email with notification, open `telegram_bot.py`, change the line 79 and add `True`, as follow:

```python
78    context.bot.send_message(chat_id=update.message.chat_id, text="Starting {}...".format(update.message.text.lower()))
79    msg  = service.start(update.message.text.lower(),True)
80    context.bot.send_message(chat_id=update.message.chat_id,text=msg)
```

> Verify if put your email credentials in the .env
