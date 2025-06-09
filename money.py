from discord.ext import commands

class Money(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.hybrid_command(name='balance')
    async def balance(self, ctx):
        """Check your current balance."""
        user_id = ctx.author.id
        balance = await self.bot.db.get_balance(user_id)
        await ctx.send(f'Your current balance is: ${balance}')

    @commands.hybrid_command(name='addmoney')
    @commands.has_permissions(administrator=True)
    async def add_money(self, ctx, user: commands.UserConverter, amount: int):
        """Add money to a user's account (admin only)."""
        if amount <= 0:
            await ctx.send("You must add a positive amount.")
            return
        user_id = user.id
        await self.bot.db.add_money(user_id, amount)
        await ctx.send(f'Added ${amount} to {user.name}\'s account.')
 
    @commands.hybrid_command(name='removemoney')
    @commands.has_permissions(administrator=True)
    async def remove_money(self, ctx, user: commands.UserConverter, amount: int):
        """Remove money from a user's account (admin only)."""
        if amount <= 0:
            await ctx.send("You must remove a positive amount.")
            return
        user_id = user.id
        await self.bot.db.remove_money(user_id, amount)
        await ctx.send(f'Removed ${amount} from {user.name}\'s account.')