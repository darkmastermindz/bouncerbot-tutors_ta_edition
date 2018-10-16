import discord

TOKEN = 'XXXXXXXXXX'

client = discord.Client()

@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return

    if message.content.startswith('!hello'):
        msg = 'Hello {0.author.mention}'.format(message)
        await client.send_message(message.channel, msg)

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')
    

@DiscordBotClient.event
async def on_member_join(member):
	if member.bot:
		BotRole = discord.utils.get(member.server.roles, id=BotRole)
		await DiscordBotClient.add_roles(member, BotRole)
		print(member.name + '#' + str(member.discriminator) + ' has been auto approved - bot.')
	else:
		ApproveRole = discord.utils.get(member.server.roles, id=ApproveRole)
		AlertChan = DiscordBotClient.get_channel(AlertChan)
		Embed = discord.Embed(title='New User', description=ApproveRole.mention + ' A new user has joined the server, please approve or deny using the reactions. User will be auto denied in 30 minutes if not accepted.', type='rich', colour=16711680)
		Embed.set_footer(text='Bouncer', icon_url=DiscordBotClient.user.avatar_url)
		Embed.set_thumbnail(url=member.avatar_url)
		Embed.add_field(name='Nickname', value=member.display_name)
		Embed.add_field(name='Handle', value=member.name + '#' + str(member.discriminator))
		Embed.add_field(name='Playing', value=str(member.game))
		Message = await DiscordBotClient.send_message(AlertChan, embed=Embed)
		await DiscordBotClient.add_reaction(Message, '✅')
		await DiscordBotClient.add_reaction(Message, '❎')
		ReactRply = await DiscordBotClient.wait_for_reaction(message=Message, emoji=['✅', '❎'], timeout=TimeOutTime, check=ReactCheck)
		if ReactRply.reaction.emoji == '✅':
			await DiscordBotClient.add_roles(member, ApproveRole)
			await DiscordBotClient.send_message(AlertChan, member.mention + ' has been approved! Welcome.')
			print(member.name + '#' + str(member.discriminator) + ' has been approved')
		elif ReactRply.reaction.emoji == '❎':
			await DiscordBotClient.kick(member)
			await DiscordBotClient.send_message(AlertChan, member.display_name + ' has been denied.')
			print(member.name + '#' + str(member.discriminator) + ' has been denied')
		else:
			await DiscordBotClient.kick(member)
			await DiscordBotClient.send_message(AlertChan, member.display_name + ' has been denied. We didn\'t receive a reaction.')
			print(member.name + '#' + str(member.discriminator) + ' has been auto denied')

client.run(TOKEN)
