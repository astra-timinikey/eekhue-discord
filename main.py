import discord
from discord.ext import commands
from eekhue_core import shared_utils  # example import from core
from eekhue_discord.handlers import basic

intents = discord.Intents.default()
bot = commands.Bot(command_prefix="!", intents=intents)

# Register cogs or commands
@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")

bot.add_cog(basic.BasicHandler(bot))

if __name__ == "__main__":
    import os
    from dotenv import load_dotenv
    load_dotenv()
    TOKEN = os.getenv("DISCORD_TOKEN")
    bot.run(TOKEN)
