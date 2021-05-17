'''
==================================================
READ THIS FIRST

Welcome!
This program is a command line interface.
The purpose of the program is to have fun making it.
Your job is to add commands to the program.
The commands can do anything, like say something funny or open a webpage.
To add a command, simply add a function to the `commands` class that will be called by name.

Here is an example:
```python
@staticmethod             # Make sure to put this line before your function
def commandname(*args):   # Make sure to put '*args' as the last parameter
    """Description goes here. The description will be used in the `help` function."""
    print("Hello World!") # Do something here
```
Feel free to import any standard packages.
==================================================
'''

# IMPORTS
import time, os, random, shlex

# GLOBAL VARIABLES
prefix = "> "
debug = False

# COMMANDS
class commands:
    @staticmethod
    def default(*args):
        """This is what happens when an unrecognized command is typed."""
        print("Unrecognized command.")

    @staticmethod
    def help(*args):
        """help [command]\nDisplay available commands or show help about a specific command."""
        if args and args[0] in dir(commands):
            print(getattr(commands, args[0]).__doc__) # Print the docstring of a command
        else:
            print("Available commands:")
            for member in dir(commands):
                if not member.startswith('__'):
                    print('\t' + str(member)) # Print a list of all the available commands

    @staticmethod
    def exit(*args):
        """Initiate self-destruct protocol."""
        exit() # Exit the program

    @staticmethod
    def args(*args):
        """Show arguments passed here for debugging."""
        print(args)

    @staticmethod
    def debug(*args):
        """debug [on/off]\nTurn debug mode on or off."""
        global debug
        if args and (args[0] == 'on' or args[0] == 'off'):
            debug = True if args[0] == 'on' else False
            print(f"Debug mode {args[0]}.")

        else:
            print(commands.debug.__doc__)

    @staticmethod
    def prefix(*args):
        """prefix [string]\nSet the input prefix."""
        global prefix
        if args:
            prefix = args[0]

        else:
            print(commands.prefix.__doc__)

    @staticmethod
    def command(*args):
        """Type something else."""
        print(commands.command.__doc__) # Print the docstring of this function

    def welcome(*args):
        """Welcome to the future!"""
        print(commands.welcome.__doc__)

    @staticmethod
    def helloworld(*args):
        """Hello World!"""
        print(commands.helloworld.__doc__)

    @staticmethod
    def asdf(*args):
        """asdfasdfasdfasdf"""
        print(commands.asdf.__doc__)

    @staticmethod
    def true(*args):
        """false"""
        print(commands.true.__doc__)

    @staticmethod
    def false(*args):
        """true"""
        print(commands.false.__doc__)

    @staticmethod
    def purpose(*args):
        """What purpose?"""
        print(commands.purpose.__doc__)

    @staticmethod
    def browser(*args):
        """browser [url]\nOpen a browser window and navigate to a url."""
        import webbrowser
        chromePath = 'C:/Program Files/Google/Chrome/Application/chrome.exe' 
        if not os.path.exists(chromePath):
            chromePath = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe'

        webbrowser.get(chromePath + ' %s').open_new_tab(''.join(args))

    def google(*args):
        """google [keywords]\nSearch Google."""
        commands.browser(f"https://www.google.com/search?q={'+'.join(args)}")

    @staticmethod
    def memes(*args):
        """ah yes, meme."""
        args = list(args)
        commands.google(*args, 'memes')

    @staticmethod
    def rickroll(*args):
        """Try me."""
        print(random.choice(["Big mistake.", "Too late.", "Ladies and gentlemen, we gottem."]))
        time.sleep(1)
        commands.browser('https://www.youtube.com/watch?v=dQw4w9WgXcQ')

    @staticmethod
    def notrickroll(*args):
        """Not a rickroll."""
        commands.rickroll()

    @staticmethod
    def starlink(*args):
        """Show Starlink satellite info."""
        from requests import get
        from re import search, IGNORECASE
        response = get('https://en.wikipedia.org/wiki/Starlink').text
        orbiting = search(r'Total satellites currently in orbit .*: (\d+)', response, IGNORECASE)
        launched = search(r'Total satellites launched .*: (\d+)', response, IGNORECASE)
        deorbited = search(r'Total satellites deorbited .*: (\d+)', response, IGNORECASE)
        print(orbiting.group(0))
        print(launched.group(0))
        print(deorbited.group(0))

    @staticmethod
    def yoda(*args):
        """Say something, I will."""
        commands.quote('yoda')
        time.sleep(1)
        commands.browser('https://www.google.com/search?q=yoda&tbm=isch')

    @staticmethod
    def rainbow(*args):
        """Cycle through terminal colors."""
        for color in '0123456789abcdef0':
            os.system(f'color {color}7')
            time.sleep(0.1)

    @staticmethod
    def paradox(*args):
        """Break the laws of the universe."""
        paradoxes = [
            "True or False?\n'This statement is false.'",
            "Does a set of all sets contain itself?",
            "New mission: refuse this mission.",
            "The second sentence is false. The first sentence is true.",
            "I know one thing, that I know nothing. - Socrates",
            "Which came first? The chicken or the egg?",
            "This is a lie.",
            "If a potato is 99% water, and it dries to become 98% water, it loses 50% of it's weight.",
            "If you put a teaspoon of wine into a barrel of sewage, you get sewage.\nIf you put a teaspoon of sewage into a barrel of wine, you get sewage.",
            "Cats always land on their feet. Buttered toast always lands buttered side down.",
            "Do Stack Overflow developers use Stack Overflow?",
            "How did Google make Google without Google?",
            "A page with the words 'This page is intentionally left blank.' is no longer blank.",
            "Paperwork increases as more time is spent reporting on the less that is done.\nStability is achieved when all time is spent reporting on the nothing that is done."
        ]
        print(random.choice(paradoxes))

    @staticmethod
    def quote(*args):
        """I don't like sand."""
        yoda = [
            '"There is another..." - Yoda',
            '"Do or do not. There is no try." - Yoda',
            '"Patience you must have my young Padawan." - Yoda',
            '"Powerful you have become, the dark side I sense in you." - Yoda',
            '"Feel the force!" - Yoda',
            '"Size matters not." - Yoda',
            '"The dark side clouds everything. Impossible to see the light, the future is." - Yoda',
            '"You will find only what you bring with you." - Yoda',
            '"When you look at the dark side, careful you must be. For the dark side looks back." - Yoda',
            '"Your path you must decide." - Yoda',
            '"If no mistake you have made, losing you are. A different game you should play." - Yoda'
        ]
        starwars = [
            *yoda,
            '"It\'s a trap!" - Admiral Ackbar',
            '"Never tell me the odds." - Han Solo',
            '"I find your lack of faith disturbing." - Darth Vader',
            '"It\'s not my fault." - Han Solo',
            '"No. I am your father." - Darth Vader',
            '"There\'s always a bigger fish." - Qui-Gon Jinn',
            '"Unlimited power!" - Darth Sidious',
            '"A long time ago in a galaxy far, far away..." - Star Wars',
            '"I don\'t like sand." - Anakin Skywalker'
        ]
        other = [
            *yoda,
            *starwars,
            '"There are only 10 types of people in the world: Those that understand binary and those that don\'t." -The Talos Principle'
        ]
        groups = {
            'yoda': yoda,
            'starwars': starwars,
            'other' : other,
        }
        if args and args[0] in groups:
            print(random.choice(groups[args[0]]))

        else:
            print(random.choice(random.choice(list(groups.values()))))
    
    @staticmethod
    def birthday(*args):
        """birthday [yyyy/mm/dd]\nShow birthday and age info."""
        if not args:
            print(commands.birthday.__doc__)
            return

        from datetime import date
        try:
            dob = date(*[int(i) for i in args[0].split("/")])
            
        except:
            print("Invalid date.")
            return

        now = date.today()
        if dob > now:
            print(random.choice(["That's not how it works.", "Are you from the future?", "Nice try."]))
            return

        print(f"Today is {now.strftime('%A %b %d, %Y')}")
        numberOfDays = (now - dob).days
        print(f"You are {numberOfDays // 365} years old.")
        print(f"You were born on a {dob.strftime('%A')}.")
        print(f"You have spent {numberOfDays} days on Earth.")
        nextBirthday = date(now.year, dob.month, dob.day)
        if nextBirthday < now:
            nextBirthday = date(now.year + 1, dob.month, dob.day)
            
        elif nextBirthday == now:
            print("Today is your birthday! Happy birthday!")
            return
            
        print(f"Your birthday is in {(nextBirthday - now).days} days.")

    @staticmethod
    def joke(*args):
        """Funny jokes."""
        import random
        jokes = [
            "Why did the bike fall over? \nIt was two-tired.",
            "What did the ocean say to the shore? \nNothing. It just waved.",
            "Why did the gym close down? \nIt just didn't work out.",
            "What do you call a pig that does Karate? \nA pork chop.",
            "What's the best thing about Switzerland? \nI don't know, but the flag is a big plus.",
            "What kind of tree can fit in your hand? \nA palm tree!",
            "Today at the bank, a woman asked me to check her balance. So I pushed her over.",
            "What did the traffic light say to the car? \n'Don't look! I'm about to change.'",
            "What ryhmes with orange? \nNo, it doesn't.",
            "What did the plate say to his friend? \nTonight, dinner's on me!",
            "How do trees get online? \nThey just log on!",
            "My daughter wanted a Cinderella-themed party, so I invited her friends and made them clean the house.",
            "'Can I watch the TV?' \nDad: Yes, but don't turn it on.",
            "Are you free tonight? \nNo, I'm expensive.",
            "Why did the kid throw his clock out of the window? \nBecause he wanted to see time fly.",
            "What do you call a snake that is exactly 3.14 meters long? \nA πthon.",
            "What did the Science book say to the Math book? \nWow, you've got problems.",
            "What happened when the strawberry attempted to cross the road? \nThere was a traffic jam!",
            "Your WinRAR 30-day trial is up. Please pay to continue using service.",
            "Parallel lines have so much in common. It's a shame they'll never meet."
        ]
        print(random.choice(jokes))

# INPUT LOOP
while True:
    try:
        # Get input from the user and split it into words
        command = shlex.split(input(prefix))
        # Call a function from the commands class that matches the first word, with the rest of the words as arguments
        if command: getattr(commands, command[0], commands.default)(*command[1:])

    except Exception as exception:
        if debug:
            print(str(exception))