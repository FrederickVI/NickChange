import discord
from discord.ext import commands
from discord.ui import Button, View
from discord import Intents
import asyncio

Guild_ID = 844747238445023242

class MyClient(discord.Client):
    def __init__(self):
        intents = discord.Intents.default()
        intents.message_content = True
        intents.members = True

        super().__init__(command_prefix=commands.when_mentioned_or('!'), intents=intents)


    async def on_ready(self):
        print("Bot running with:")
        print("Username: ", client.user.name)
        print("User ID: ", client.user.id)
        print('-----')
    
    # Nickname change
    async def on_message(self, message):
        # To prevent the bot replying to itself
        guild = client.get_guild(Guild_ID)
        channel = message.channel
        member = guild.get_member(message.author.id)
        if message.author.id == self.user.id:
            return
        try:
            if message.content.startswith('!') and message.channel.type == discord.ChannelType.private:
                await channel.send(f'Nickname set to **{message.content[1:]}**')
                await member.edit(nick=message.content[1:])
            elif message.channel.type == discord.ChannelType.private and message.content.lower() == "nonick":
                await member.edit(nick=None)
                await channel.send("Nickname was reseted.")

        except discord.errors.Forbidden as error:
            embed = discord.Embed(description=f'```diff\n- {error}```', color=discord.Color.red())
            embed.set_author(name="Looks like I don't have permission to change your nickname.")
            await channel.send(embed=embed)

    # Welcome message
    async def on_member_join(self, member):
        view = Introduction()
        await member.send(f'Welcome to the server {member}! Use the button below to make an introduction and get access to the server.', view=view)

class Introduction(discord.ui.View):
    def __init__(self):
        super().__init__()
        self.value = None

    # Write an introduction button
    @discord.ui.button(label='Write an introduction', style=discord.ButtonStyle.green)
    async def callback(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.channel.send('Under construction!')
        self.value = True
        self.stop()


client = MyClient
client.run('token')