# Ngrok Automation

It's a hack to automate ngrok with telegram bot in python.

## Overview

![image](https://user-images.githubusercontent.com/25212918/158262424-804e3d27-333f-4ce0-bb45-1e52c8ad309e.png)


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
79    msg  = service.start(update.message.text.lower(),True)
```

> Verify if put your email credentials in the .env
