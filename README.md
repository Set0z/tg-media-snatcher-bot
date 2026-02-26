<h1 align="center">tg-media-snatcher-bot</h1>
<div align="center">
tg-media-snatcher-bot - is a Telegram media Bot that allows you to download, and forward media time-limited (TTL) files content.
  
## `🚨 Telegram Premium Needed! 🚨`

</div>

<h1 align="center">Navigation </h1>

- [Installation](#installation)
- [Install dependencies](#installation)
- [Configuration](#configuration)
- [Launch](#launch)
- [Bot Settings](#bot-settings)
- [How to get media](#how-to-get-media)

## Installation

### 1. Clone the repository

Clone the project and move into its directory:

```bash
git clone https://github.com/Set0z/tg-media-snatcher-bot.git
cd tg-media-snatcher-bot
````

### 2. Install dependencies

Install the required Python packages:

```bash
pip install -r requirements.txt
````

## Configuration

### 3. Create a `.env` file

In the project root directory, create a `.env` file and add your Telegram Bot Token and User Id:

```
TOKEN=YOUR_BOT_TOKEN
OWNER=YOUR_USER_ID
```

## Launch

Run the script with:

```bash
python3 bot.py
```
## Bot Settings

Go to `BotFather`, select your bot whose token you specified in .env

In the bot settings, enable the `"Business Mode"` parameter

Add your bot to the necessary chats using `Telegram Premium` features

## How to get media

In order for the bot to send you a disappearing message, you must reply to it in the chat to which the bot is connected and running

### `🚨 Do not look at the message until you reply!`

If the message timer starts counting down, the bot will not be able to send it to you!
