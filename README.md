# AIO Discord Bot

A modular Discord bot built with Python, designed to keep features separated and easy to extend.

The project uses a Cog-based architecture, allowing new functionality to be added without modifying the main application entry point.

## Features

### Welcome & Goodbye

Automatically sends an embedded message when a member joins or leaves the server.

### Music Player

A voice-channel music player with support for:

* Search by song title
* YouTube links
* Automatic audio downloading
* Play, pause, and resume
* Skip and stop
* Music queue

## Project Structure

```text
AIO-discord-bot/
├── main.py
├── config.py
├── requirements.txt
├── .env.example
└── cogs/
    ├── welcome.py
    └── music.py
```

### Architecture

`main.py` serves as the application entry point and automatically loads the available Cogs.

Each feature is isolated inside the `cogs/` directory. This keeps individual systems separated and makes the project easier to maintain as more features are added.

Adding a new feature generally means creating a new Cog rather than modifying the main application.

## Requirements

* Python 3.x
* FFmpeg
* A Discord Bot Application
* A Discord server where you have permission to add bots

## Installation

### 1. Create a Discord Application

Open the [Discord Developer Portal](https://discord.com/developers/applications) and create a new application.

Open the **Bot** section and:

1. Add a bot.
2. Copy the bot token.
3. Enable the following Privileged Gateway Intents:

   * Server Members Intent
   * Message Content Intent

Keep the bot token private. Do not commit it to the repository.

### 2. Install Dependencies

Clone the repository and install the required Python packages:

```bash
git clone https://github.com/your-username/AIO-discord-bot.git
cd AIO-discord-bot
python -m pip install -r requirements.txt
```

### 3. Install FFmpeg

FFmpeg is required by the music player.

On Windows, it can be installed with:

```bash
winget install ffmpeg
```

You can also install FFmpeg manually and provide the path to `ffmpeg.exe` in the music configuration.

### 4. Configure the Bot

Create a `.env` file from the provided example:

```bash
copy .env.example .env
```

Configure the required environment variables:

```env
DISCORD_TOKEN=your_discord_bot_token
WELCOME_CHANNEL_ID=your_welcome_channel_id
GOODBYE_CHANNEL_ID=your_goodbye_channel_id
```

Replace the placeholder values with the appropriate Discord configuration.

### 5. Invite the Bot

In the Discord Developer Portal, open:

**OAuth2 → URL Generator**

Select the `bot` scope and grant the permissions required by the bot:

* View Channel
* Send Messages
* Embed Links
* Connect
* Speak

Use the generated URL to invite the bot to your server.

### 6. Start the Bot

Run:

```bash
python main.py
```

The bot will connect to Discord and load the available Cogs.

## Commands

### Music

| Command         | Alias | Description                               |
| --------------- | ----- | ----------------------------------------- |
| `!play <query>` | `!p`  | Search for and play a song                |
| `!skip`         | —     | Skip the current song                     |
| `!pause`        | —     | Pause playback                            |
| `!resume`       | —     | Resume playback                           |
| `!stop`         | —     | Stop playback and leave the voice channel |
| `!queue`        | `!q`  | Display the current music queue           |

### Examples

```text
!play never gonna give you up
!play https://youtube.com/...
!queue
!skip
```

## Configuration

Sensitive configuration is stored in environment variables rather than directly in the source code.

```text
.env
  |
  v
config.py
  |
  v
Bot Cogs
```

The `.env` file should remain local and should not be committed to Git.

## Development

The project is designed to be extended through individual Cogs.

For example, a new feature can be added as:

```text
cogs/
├── welcome.py
├── music.py
└── new_feature.py
```

The goal is to keep each feature independent while maintaining a simple application entry point.