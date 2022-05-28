import random as psatirTJUY
from tkinter.tix import Balloon
from discord.ext import commands; import discord; from asyncio import sleep;import json

class CSN(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command()
    async def csn(self,ctx, coin):
        coin = int(coin)
        uang = await data_money(ctx.author)
        print(uang[str(ctx.author.id)]["wallet"])
        if coin > int(uang[str(ctx.author.id)]["wallet"]):
            await ctx.send("Make sure you put the wrong amount.")
        else:
            user = psatirTJUY.randint(0, 36)
            bot = psatirTJUY.randint(3, 36)
            
            embed = discord.Embed(title="CSN", color=0x254ea8)
            embed.add_field(name="Press to play", value="Press 🎲for play")
            embed.set_footer(text="CSN | Games")
            em = await ctx.send(embed=embed)
            
            await em.add_reaction("🎲")
            
            await sleep(10)
            
            fetch = await ctx.channel.fetch_message(em.id)
            reaksi_gamer_id = await fetch.reactions[0].users().flatten() # reaction 1
            reaksi_gamer_id.pop(reaksi_gamer_id.index(ctx.guild.me)) # RIL
            
            if len(reaksi_gamer_id) >= 1:
                if user>bot:
                    await ctx.send("WIN | {1} Point from roll : {0}".format(user, ctx.author.mention))
                else:
                    await ctx.send("LOSE!")

async def data_money(user):
    with open('./data.json','r') as f:
        users = json.load(f)
    return users

def setup(bot):
    bot.add_cog(CSN(bot))