import lightbulb
import hikari
from pprint import pprint
import requests

bot = lightbulb.BotApp(
    token="OTM1NTk3Nzc1MTQ2NTg2MTMy.YfA9VA.nErMeGTVYIrPJPrAKeYEkFw-P_Q", 
    default_enabled_guilds=(502162705575182336)
)

"""
# EVENT EXAMPLES: (EVENTS WRITE SOMETHING TO THE COMMAND LINE WHEN CRITERIA IS MET)
@bot.listen(hikari.GuildMessageCreateEvent)
async def print_message(event):
    print(event.content)

@bot.listen(hikari.StartedEvent)
async def bot_started(event):
    print('Bot has started!!!!!!')

# COMMAND - INSTRUCT BOT TO DO SOMETHING (GROUPS, SUBCOMMANDS AND OPTIONS BELOW)
@bot.command
@lightbulb.command('ping', 'Says pong!')
@lightbulb.implements(lightbulb.SlashCommand)
async def ping_pong(context):
    await context.respond('Pong!')
"""

def greet():
    # Command - greet
    @bot.command
    @lightbulb.command('hey', 'Say hi!')
    @lightbulb.implements(lightbulb.SlashCommand)
    async def hey(context):
        await context.respond('Ayo, whaddup?')

def math_module():
    #####   MATH GROUP  #####
    # Group - math
    @bot.command
    @lightbulb.command('math', "I'll do the math for you.. I'm a computer dummy, I eat math for entrée!")
    @lightbulb.implements(lightbulb.SlashCommandGroup)
    async def math_group(context):
        pass

    # Subcommand - help
    @math_group.child
    @lightbulb.command('help', 'What math will I do?')
    @lightbulb.implements(lightbulb.SlashSubCommand)
    async def help(context):
        await context.respond('With the math function, I can... \n> Add\n> Subtract\n> Multiply\n> Divide\n> Modulus\n> Floor Division\n> Exponant')

    # Subcommand - addition
    @math_group.child
    @lightbulb.option('num2', 'Second number?', type=int)
    @lightbulb.option('num1', 'First number?', type=int)
    @lightbulb.command('addition', 'Add numbers!')
    @lightbulb.implements(lightbulb.SlashSubCommand)
    async def addition(context):
        await context.respond(context.options.num1 + context.options.num2)

    # Subcommand - subtract
    @math_group.child
    @lightbulb.option('num2', 'Second number?', type=int)
    @lightbulb.option('num1', 'First number?', type=int)
    @lightbulb.command('subtract', 'Subtract numbers!')
    @lightbulb.implements(lightbulb.SlashSubCommand)
    async def subtract(context):
        await context.respond(context.options.num1 - context.options.num2)

    # Subcommand - multiply
    @math_group.child
    @lightbulb.option('num2', 'Second number?', type=int)
    @lightbulb.option('num1', 'First number?', type=int)
    @lightbulb.command('multiply', 'Multiply numbers!')
    @lightbulb.implements(lightbulb.SlashSubCommand)
    async def multiply(context):
        await context.respond(context.options.num1 * context.options.num2)

    # Subcommand - divide
    @math_group.child
    @lightbulb.option('num2', 'Second number?', type=int)
    @lightbulb.option('num1', 'First number?', type=int)
    @lightbulb.command('divide', 'Divide numbers!')
    @lightbulb.implements(lightbulb.SlashSubCommand)
    async def divide(context):
        await context.respond(context.options.num1 / context.options.num2)

    # Subcommand - modulus
    @math_group.child
    @lightbulb.option('num2', 'Second number?', type=int)
    @lightbulb.option('num1', 'First number?', type=int)
    @lightbulb.command('modulus', 'Divide numbers!')
    @lightbulb.implements(lightbulb.SlashSubCommand)
    async def modulus(context):
        await context.respond(context.options.num1 % context.options.num2)

    # Subcommand - floor division
    @math_group.child
    @lightbulb.option('num2', 'Second number?', type=int)
    @lightbulb.option('num1', 'First number?', type=int)
    @lightbulb.command('floor', 'Divide numbers!')
    @lightbulb.implements(lightbulb.SlashSubCommand)
    async def floor(context):
        await context.respond(context.options.num1 // context.options.num2)

    # Subcommand - exponant
    @math_group.child
    @lightbulb.option('num2', 'Second number?', type=int)
    @lightbulb.option('num1', 'First number?', type=int)
    @lightbulb.command('exponant', 'Divide numbers!')
    @lightbulb.implements(lightbulb.SlashSubCommand)
    async def exponant(context):
        await context.respond(context.options.num1 ** context.options.num2)

def weather_module():
    # API connection
    URL = ("http://api.openweathermap.org/data/2.5/weather?q=Cork&APPID=a96ce88fe9d17f75eb44312d7aab6d5c")
    r = requests.get(URL)
    # Parse as JSON
    r_json = r.json()
    # Loop through JSON
    for i in r_json['weather']:
        main = i['main']
        desc = i['description']

    #####   MATH GROUP  #####
    @bot.command
    @lightbulb.command('weather', "You haven't been out in awhile.. Wanna know what it's like out there?")
    @lightbulb.implements(lightbulb.SlashCommandGroup)
    async def weather_group(context):
        pass

    # Subcommand - help
    @weather_group.child
    @lightbulb.command('help', 'What weather will I do?')
    @lightbulb.implements(lightbulb.SlashSubCommand)
    async def help(context):
        await context.respond('With the weather function, I can... \n> Tell you the weather\n> That is all -_-')

    # Subcommand - forecast
    @weather_group.child
    @lightbulb.command('forecast', "Here's the weather for Cork!")
    @lightbulb.implements(lightbulb.SlashSubCommand)
    async def forecast(context):
            await context.respond(main + "\nMore specifically, " + desc)

    # Subcommand - json
    @weather_group.child
    @lightbulb.command('json', "Here's the JSON object for Cork!")
    @lightbulb.implements(lightbulb.SlashSubCommand)
    async def json(context):
            await context.respond(r_json)

greet()
math_module()
weather_module()
bot.run()