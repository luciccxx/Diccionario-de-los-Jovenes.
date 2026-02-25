import discord
from discord.ext import commands

# Prefijo del bot
intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.command(name = 'Saludar')
async def saludar(ctx):
    await ctx.send("Bienvenido Luciana Castaño 😂")

@bot.command()
async def repeat(ctx, times: int, content='repeating...'):
    """Repeats a message multiple times."""
    for i in range(times):
        await ctx.send(content)


bot.run("")
