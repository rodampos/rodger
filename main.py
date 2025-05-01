import discord
from discord.ext import commands
import os
from keep_alive import keep_alive
import asyncio

intents = discord.Intents.default()
intents.messages = True
intents.guilds = True
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)


@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")


# Function to load all cogs
async def load_cogs():
    for filename in os.listdir("./cogs"):
        if filename.endswith(".py"):
            await bot.load_extension(f"cogs.{filename[:-3]}")


# Main function to start everything
async def main():
    keep_alive()
    await load_cogs()
    await bot.start(os.environ['TOKEN'])


# Start the bot
asyncio.run(main())
