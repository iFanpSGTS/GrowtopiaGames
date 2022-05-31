import random;import discord, json;from discord.ext import commands

class QQ(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    @commands.command()
    async def qq(self, ctx, coin):
        try:
            coin = int(coin)
            uang = await data_money()
            if coin > int(uang[str(ctx.author.id)]["wallet"]):
                await ctx.send("You don't have enough money to play CSN.")
            if coin == 0:
                await ctx.send("You can't play without money.")
            else:
                user = random.randint(0, 36)
                bot = random.randint(0, 36)
                
                user_angkaBelakang = "".join([str(user)])[1:]
                bot_angkaBelakang = "".join([str(bot)])[1:]
                
                embed = discord.Embed(title="QQ", color=0x254ea8)
                embed.add_field(name="Press to play", value="Press 🎲 to play")
                embed.set_footer(text="QQ | Games")
                em = await ctx.send(embed=embed)
                await em.add_reaction("🎲")
                
                while True:
                    fetch = await ctx.channel.fetch_message(em.id)
                    reaksi_gamer_id = await fetch.reactions[0].users().flatten() # reaction 1
                    reaksi_gamer_id.pop(reaksi_gamer_id.index(ctx.guild.me)) # RIL
                    
                    if len(reaksi_gamer_id) == 0:
                        pass
                    if len(reaksi_gamer_id) >= 1:
                        if user < 10 or bot < 10:
                            if int(user)>int(bot):
                                uang[str(ctx.author.id)]["wallet"] += coin * 3
                                with open("./data.json","w") as f:
                                    json.dump(uang,f) 
                                await ctx.send("WIN | **{1}** Point from roll : **{0}** - Bot roll : {2}".format(user, ctx.author.mention, bot))
                                break
                            else:
                                uang[str(ctx.author.id)]["wallet"] -= coin
                                with open("./data.json","w") as f:
                                    json.dump(uang,f) 
                                await ctx.send("LOSE! | Bot Point from roll : **{0}** - Your roll : **{1}**".format(bot, user))
                                break
                        else:
                            if int(user_angkaBelakang)>int(bot_angkaBelakang):
                                uang[str(ctx.author.id)]["wallet"] += coin * 3
                                with open("./data.json","w") as f:
                                    json.dump(uang,f) 
                                await ctx.send("WIN | {1} Point from roll : **{0}** - Bot roll : {2}".format(user_angkaBelakang, ctx.author.mention, bot_angkaBelakang))
                                break
                            else:
                                uang[str(ctx.author.id)]["wallet"] -= coin
                                with open("./data.json","w") as f:
                                    json.dump(uang,f) 
                                await ctx.send("LOSE! | Bot Point from roll : **{0}** - Your roll : **{1}**".format(bot_angkaBelakang, user_angkaBelakang))
                                break
        except KeyError:
            await ctx.send("Please do bot/register to regist your bank!")
            
async def data_money():
    with open('./data.json','r') as f:
        users = json.load(f)
    return users

def setup(bot):
    bot.add_cog(QQ(bot))