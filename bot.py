
import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.typing = True
intents.presences = True
intents.message_content = True
intents.members = True
intents.reactions = True  # Correct attribute for reaction events
intents.guilds = True
intents.members = True
intents.presences = True



bot = commands.Bot(command_prefix="!",
                   intents=intents)




@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name} ({bot.user.id})')


@bot.command()
async def reload(ctx):
   await ctx.send("test")


bot.run("MTA1NzI4MTE0NjU5NTA1Nzc1NA.GdUSv5.UOZVEgeiNMn_EjCZq8P6IUx-t1qu7Yj6ObykTY")



