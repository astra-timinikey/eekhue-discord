import os

import discord
from discord.ext import commands
from dotenv import load_dotenv

from eekhue_core import shared_utils
from eekhue_discord.handlers import basic


def run_bot():
    load_dotenv()
    token = os.getenv("DISCORD_TOKEN")

    intents = discord.Intents.default()
    bot = commands.Bot(command_prefix="!", intents=intents)

    @bot.event
    async def on_ready():
        print(f"Logged in as {bot.user}")

    bot.add_cog(basic.BasicHandler(bot))
    bot.run(token)


if __name__ == "__main__":
    run_bot()
