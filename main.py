from discord.ext import commands; import discord; import os

prefix = "janda/"
bot = commands.Bot(command_prefix=prefix)
bot.remove_command("help")

@bot.event 
async def on_ready():
    print("{0} is online".format(bot.user))
    for file in os.listdir('./games'):
        if file.endswith('.py'):
            bot.load_extension(f'games.{file[:-3]}')
    
@bot.command()
async def help(ctx):
    embed = discord.Embed(title="JEMBUT .COM", color=0x3fbba3)
    embed.add_field(name="Growtopia Games", value="CSN | QQ | DEPO | BAL | INFO | STORE", inline=False)
    embed.set_footer(text="GW IFANPS PRO GRAMMER HANDAL CUYH!!!!")
    await ctx.send(embed=embed)
    
bot.run("")