import random as psatirTJUY
from tkinter.tix import Balloon
from discord.ext import commands; import discord; from asyncio import sleep;import json

class CSN(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command()
    async def csn(self,ctx, coin):
        try:
            coin = int(coin)
            uang = await data_money()
            if coin > int(uang[str(ctx.author.id)]["wallet"]):
                await ctx.send("You don't have enough money to play CSN.")
            if coin == 0:
                await ctx.send("You can't play without money.")
            else:
                user = psatirTJUY.randint(0, 36)
                bot = psatirTJUY.randint(3, 10)
                
                embed = discord.Embed(title="CSN", color=0x254ea8)
                embed.add_field(name="Press to play", value="Press 🎲 to play")
                embed.set_footer(text="CSN | Games")
                em = await ctx.send(embed=embed)
                
                await em.add_reaction("🎲")
                
                while True:
                    fetch = await ctx.channel.fetch_message(em.id)
                    reaksi_gamer_id = await fetch.reactions[0].users().flatten() # reaction 1
                    reaksi_gamer_id.pop(reaksi_gamer_id.index(ctx.guild.me)) # RIL
                    
                    if len(reaksi_gamer_id) == 0:
                        pass
                    if len(reaksi_gamer_id) >= 1:
                        if user>bot:
                            uang[str(ctx.author.id)]["wallet"] += coin * 3
                            with open("./data.json","w") as f:
                                json.dump(uang,f) 
                            await ctx.send("WIN | {1} Point from roll : {0}".format(user, ctx.author.mention))
                            break
                        else:
                            uang[str(ctx.author.id)]["wallet"] -= coin
                            with open("./data.json","w") as f:
                                json.dump(uang,f) 
                            await ctx.send("LOSE! | Bot Point from roll : {0}".format(bot))
                            break
        except KeyError:
            await ctx.send("Please do bot/register to regist your bank!")

async def data_money():
    with open('./data.json','r') as f:
        users = json.load(f)
    return users

def setup(bot):
    bot.add_cog(CSN(bot))
