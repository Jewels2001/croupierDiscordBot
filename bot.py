
import os
import discord
import logging

from discord.ext import commands

#from money import Money

from dotenv import load_dotenv
load_dotenv()

bot_token = os.environ.get('BOT_TOKEN')
if not bot_token:
    raise ValueError("BOT_TOKEN environment variable is not set.")

#my_guild = discord.Object(id=os.environ.get('MY_GUILD'))

#handler = logging.FileHandler(filename='discordCroupierBot.log', encoding='utf-8', mode='w')
# discord.utils.setup_logging(handler=handler, level=logging.DEBUG)


intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='.', intents=intents)

#client = discord.Client(intents=intents)
#bot = commands.Bot(command_prefix='.', intents=intents, help_command=None)


@bot.event
async def on_ready():
    print(f'Croupier bot is logged in as {bot.user} (ID: {bot.user.id})')
    #await bot.add_cog(Money(bot = bot))
    #print(f'Money cog has been added to the bot.')
    #try:
    #    synced = await bot.tree.sync(guild=my_guild)  # Sync commands globally, or specify a guild ID for guild-specific commands
    #    print(f'Bot has synced {len(synced)} command(s)!')
    #except Exception as e:
    #    print(f'Error syncing bot commands: {e}')

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if message.content.startswith('.hello'):
        await message.channel.send(f'Hi {message.author.name}!')
        
@bot.slash_command(name='beep', description='BOOP!')
async def beep(ctx: discord.ApplicationContext):
    await ctx.respond("BoOp :)!")
        
bot.load_extension('cogs.tokens')  # Load the Tokens cog

bot.run(bot_token)