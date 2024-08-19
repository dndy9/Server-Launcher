from discord.ext import commands
import subprocess
import discord
from dataclasses import dataclass
import os
import asyncio


BOT_TOKEN = #New BotToken create new bot token from discord dev website and paste here
CHANNEL_ID = #Copy the channel ID from the wanted Discord and paste into here

bot = commands.Bot(command_prefix = "!", intents = discord.Intents.all())

@bot.event
async def on_ready():
   print("Hello! Dandy Bot is online.")
   channel = bot.get_channel(CHANNEL_ID)
   await channel.send("Hello Dandy Bot is ready. Servers Available:\n Minecraft \n " )
    
    
@bot.command()
async def commands(ctx):
    await ctx.send("Valheim commands: \n Turn server on: **!ValOn** \n Turn server off: **!ValOff** \n Check Server Status: **!ValStatus** \n\nMinecraft commands:\n Minecraft server- **104.10.238.79** \n Turn MC server on: **!MinecraftOn** \n Turn MC server off: **!MinecraftOff** \n Minecraft server status: **!MinecraftStatus**")

@bot.command()
async def testings(ctx):    
    await ctx.send("The bot is working. Death to Riot")

#@bot.command()
#async def add(ctx, *arr):
#    result = 0
#    for i in arr:
#        result += int(i)
#        
#    await ctx.send(f"Result: {result}")

@bot.command()
async def ValOn(ctx):    
    

    await ctx.send("Valheim server is on")
    batch_file_path = r'"C:\Users\16266\Desktop\School\ServerBot\start_headless_server.bat"'
    try:
        # Start the batch file
        process = subprocess.Popen(batch_file_path, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, shell=True)
        stdout, stderr = process.communicate()
        if process.returncode == 0:
            await ctx.send("Batch file executed successfully.")
            print(stdout)
        else:
            await ctx.send(f"Failed to execute batch file. Error: {stderr}")
            print(stderr)
    except FileNotFoundError as e:
        await ctx.send(f"File not found error: {e}")
    except Exception as e:
        await ctx.send(f"An unexpected error occurred: {e}")



@bot.command()
async def ValOff(ctx):
    await ctx.send("Valheim server is off")
    
@bot.command()
async def ValStatus(ctx):    
    await ctx.send("Valheim server is")

@bot.command()
async def MinecraftOn(ctx):    
    await ctx.send("Minecraft server is starting.")
    
    # Start the server in a separate thread
    await asyncio.to_thread(start_minecraft_server)

    await ctx.send("Server has been turned off.")

def start_minecraft_server():
    batch_file_path = r'insert .jar server start file to start the server '
    process = subprocess.Popen(['java', '-jar', batch_file_path], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    stdout, stderr = process.communicate()
    print(stdout)


# async def MinecraftOn(ctx):    
#     await ctx.send("Minecraft server is opening...")
#     batch_file_path = r'C:\Users\16266\Desktop\ \MC 2024\server.jar'
#         # Start the .jar file using Java
#     process = subprocess.Popen(['java', '-jar', batch_file_path], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
#     stdout, stderr = process.communicate()
#     await ctx.send("Server started successfully.")
#     print(stdout)


@bot.command()
async def MinecraftOff(ctx):    
    await ctx.send("Minecraft server is off")
    batch_file_path = r'insert directory here to check if off'
        # Start the .jar file using Java
    process = subprocess.Popen(['java', '-jar', batch_file_path], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    stdout, stderr = process.communicate()
    await ctx.send("Server started successfully.")
    print(stdout)

@bot.command()
async def MinecraftStatus(ctx):    
    await ctx.send("Minecraft server is ")
def checkFileClosed(file_obj):
    # check if file is closed using `closed` property
    if file_obj.closed == True:
        print("Your file is closed.")
    else:
        print("Your file is open.")



bot.run(BOT_TOKEN)