
import os
import discord
import logging
from discord import app_commands
from discord.ext import commands

from money import Money

from dotenv import load_dotenv
load_dotenv()

bot_token = os.environ.get('BOT_TOKEN')
if not bot_token:
    raise ValueError("BOT_TOKEN environment variable is not set.")


my_guild = discord.Object(id=os.environ.get('MY_GUILD'))

handler = logging.FileHandler(filename='discordCroupierBot.log', encoding='utf-8', mode='w')
# discord.utils.setup_logging(handler=handler, level=logging.DEBUG)


intents = discord.Intents.default()
intents.message_content = True

#client = discord.Client(intents=intents)
bot = commands.Bot(command_prefix='.', intents=intents, help_command=None)


@bot.event
async def on_ready():
    print(f'Croupier bot is logged in as {bot.user} (ID: {bot.user.id})')
    await bot.add_cog(Money(bot = bot))
    print(f'Money cog has been added to the bot.')
    try:
        synced = await bot.tree.sync(guild=my_guild)  # Sync commands globally, or specify a guild ID for guild-specific commands
        print(f'Bot has synced {len(synced)} command(s)!')
    except Exception as e:
        print(f'Error syncing bot commands: {e}')

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if message.content.startswith('.hello'):
        await message.channel.send(f'Hi {message.author.name}!')
        
@bot.tree.command(name='test1', description="This is a test1")
async def test1(ctx):
    await ctx.channel.send("This is a regular command!")
    await ctx.send("This is a regular command!")
    print("Regular command executed.")
        
@bot.hybrid_command(name='test', description='A test hybrid command :)')
async def test(interaction: discord.Interaction, ctx):
    """A test hybrid command that can be used as a slash command or a regular command."""
    await interaction.response.send_message(f"This is a hybrid command {interaction.user.mention}! :)")
    await ctx.send("This is a hybrid command!")
    print("Hybrid command executed.")

@bot.tree.command()
@app_commands.describe(
    first_value='The first value you want to add something to',
    second_value='The value you want to add to the first value',
)
async def add(interaction: discord.Interaction, first_value: int, second_value: int):
    """Adds two numbers together."""
    await interaction.response.send_message(f'{first_value} + {second_value} = {first_value + second_value}')

@bot.tree.command(name='boop')
async def boop(interaction: discord.Interaction):
    await interaction.response.send_message(f'Boop! :)', ephemeral=True)


bot.run(bot_token, log_handler=handler, log_level=logging.DEBUG)