import discord;from discord.ext import commands;import json;from asyncio import sleep

class Reg(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    @commands.command()
    async def register(self, ctx):
        user_bank = await check_bank()
        try:
            if user_bank[str(ctx.author.id)]:
                await ctx.send("Your bank already registered")
        except KeyError:
            msg = await ctx.send("**Registering your bank..**")
            await sleep(1.5)
            await msg.edit(content="**Registering your bank...**")
            await sleep(1.5)
            await regist(ctx.author.id)
            await msg.edit(content="***Your bank is registered!***")
            embed = discord.Embed(title="Bank", color=0x254ea8)
            embed.add_field("Balance", value=user_bank[str(ctx.author.id)]["wallet"])
            embed.set_footer("Bank | Games")
            await ctx.send(embed=embed)

async def check_bank():
    with open("./data.json",'r') as f:
        bank = json.load(f)
    return bank
    
async def regist(user):
    with open("data.json", 'r') as f:
        id_bank = json.load(f)
        id_bank[str(user)] = {}
        id_bank[str(user)]["wallet"] = 0
        with open("data.json", "w") as f:
            json.dump(id_bank,f)

def setup(bot):
    bot.add_cog(Reg(bot))