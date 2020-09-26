import discord

token="NwijinnNIOMiiomdwfoihSDFwqwfohFw"#---enter your token id here--#
client=discord.Client()

@client.event
async def on_member_join(member):
    for channel in member.server.channels:
        if str(channel)=='general':
            await client.send_message(f"""welcome to the server {member.mention}""")

@client.event
async def on_member_leave(member):
    for channel in member.server.channels:
        if str(channel)!='general':
            await client.send_message(f"""{member.mention}has left the server""")

@client.event
async def on_message(message):
    if message.content.find("-hii") != -1:
        await message.channel.send("Hello")  
    
    elif message.content.find("-how are you") != -1:
        await message.channel.send(" I am fine what about you")  

    elif message.content.find("-do you eat?") != -1:
        await message.channel.send("No,I am a Machine")  

    elif message.content.find("-who has made you?") != -1:
        await message.channel.send("Rupesh Prajapati ")  
        await message.channel.send("Follow on Insta @call.me_pr")  
    
    elif message.content.find("-really") != -1:
        await message.channel.send("yehh.Don't you think so..")  
        await message.channel.send("Follow on Insta @call.me_pr")

    elif message.content.find("-tell me your friend  name") != -1:
        await message.channel.send("I dont have any friend.Would you be my friend.")

    elif message.content.find("-bye") != -1:
        await message.channel.send("bbyyee,See you soon..")
  

client.run(token)