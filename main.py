import asyncio
import os

import discord
from discord.ext import commands

import config

intents = discord.Intents.default()
intents.members = True
intents.message_content = True

bot = commands.Bot(command_prefix=config.COMMAND_PREFIX, intents=intents)


@bot.event
async def on_ready():
    print(f"✅ Bot online sebagai {bot.user} (ID: {bot.user.id})")
    print(f"📡 Terhubung ke {len(bot.guilds)} server")

@bot.event
async def on_command_error(ctx, error):
    print(f"[ERROR] Command '{ctx.command}' gagal: {error}")
    await ctx.send(f"⚠️ Error: {error}")


async def load_cogs():
    cogs_dir = os.path.join(os.path.dirname(__file__), "cogs")
    for filename in os.listdir(cogs_dir):
        if filename.endswith(".py") and not filename.startswith("_"):
            cog_name = f"cogs.{filename[:-3]}"
            try:
                await bot.load_extension(cog_name)
                print(f"  ✔ Cog dimuat: {cog_name}")
            except Exception as e:
                print(f"  ✘ Gagal load {cog_name}: {e}")


async def main():
    async with bot:
        await load_cogs()
        await bot.start(config.DISCORD_TOKEN)


if __name__ == "__main__":
    asyncio.run(main())
