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
    embed = discord.Embed(title="Help", color=0x3fbba3)
    embed.add_field(name="Growtopia Games | Commands list",value="CSN\nQQ\nDEPOSIT\nBAL\nINFO\nSTORE",inline=False)
    embed.set_footer(text="Help | Information about useable commands")
    await ctx.send(embed=embed)
    
bot.run("")
