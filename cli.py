'''
Welcome!
This program is a command line interface.
The purpose of the program is to have fun making it.
Your job is to add commands to the program.
The commands can do anything, like say something funny or open a webpage.
To add a command, simply add a function to the `commands` class that will be called by name.

Here is an example:
```python

@staticmethod               # Make sure to put this line before your function
def commandname(*args):     # Make sure to put `*args` as the last parameter
    """Description goes here. The description will be used in the `help` function."""
    print("Hello World!")   # Do something here

```
Feel free to import any standard libraries.
'''

# IMPORTS
import time
import os
import shlex
import random

# GLOBAL VARIABLES
prefix = '> '
debug = False


# COMMANDS
class commands:
    @staticmethod
    def default(*args):
        """This is what happens when an unknown command is entered."""
        print("Unknown command. Type 'help' for a list of available commands.")

    @staticmethod
    def help(*args):
        """help [command]\nDisplay available commands or show help about a specific command."""
        if args and args[0] in dir(commands):
            print(getattr(commands, args[0]).__doc__)  # Print the docstring of a command
        else:
            print("Type 'help <command>' for information about a specific command.")
            print("Available commands:")
            for member in dir(commands):
                if not member.startswith('_'):
                    print('\t' + str(member))  # Print a list of all the available commands

    @staticmethod
    def exit(*args):
        """Initiate self-destruct protocol."""
        raise SystemExit  # Exit the program

    @staticmethod
    def license(*args):
        """Legal stuff."""
        print("""MIT License

Copyright (c) 2021 EBUS Coding Club

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.""")

    @staticmethod
    def about(*args):
        """About this program."""
        print("This is a command line program created by the students in the EBUS Coding Club. Have fun with the various commands available!")

    @staticmethod
    def credits(*args):
        """Who made this?"""
        members = [
            "LemonPi314 - Owner",
            "Duplexes - Contributor",
            "itsMimi - Contributor",
            "mdevauld - Contributor"
        ]
        for member in members:
            print(member)

    @staticmethod
    def boot(*args):
        """Initialize command line interface."""
        print("EBUS Coding Club CLI Project.")
        print("Type 'help' for a list of available commands.\n")

    @staticmethod
    def args(*args):
        """Show arguments passed here for debugging."""
        print(args)

    @staticmethod
    def debug(*args):
        """Turn debug mode on or off.\n\nUsage:\n\tdebug (on | off)"""
        global debug
        if args and (args[0] == 'on' or args[0] == 'off'):
            debug = True if args[0] == 'on' else False
            print(f"Debug mode {args[0]}.")
        else:
            print(commands.debug.__doc__)

    @staticmethod
    def prefix(*args):
        """Change the input prefix.\n\nUsage:\n\tprefix <string>\n\nArguments:\n\t<string>  string to use as a prefix"""
        global prefix
        if args:
            prefix = args[0]
        else:
            print(commands.prefix.__doc__)

    @staticmethod
    def shell(*args):
        """Pass commands to the underlying shell instance.\n\nUsage:\n\tshell <command>\n\nArguments:\n\t<command>  command to execute in the shell"""
        if args:
            os.system(' '.join(args))
        else:
            print(commands.shell.__doc__)

    @staticmethod
    def command(*args):
        """Type something else."""
        print(commands.command.__doc__)  # Print the docstring of this function

    @staticmethod
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
    def whatisthis(*args):
        """Don't ask."""
        commands.whatisthis.__doc__ = random.choice(["Don't ask.", "You think I know?", "A mystery still unsolved..."])
        print(commands.whatisthis.__doc__)

    @staticmethod
    def canipass(*args):
        """You shall not pass."""
        print(commands.canipass.__doc__)

    @staticmethod
    def crash(*args):
        """Don't try this at home. (Seriously, don't do it)"""
        if input("Are you sure? Type 'yes' if you are sure: ") != "yes":
            return
        if input("Are you absolutely 100% sure you want to continue? Last chance. Type 'YES I AM SURE' if you really want to continue: ") != "YES I AM SURE":
            return
        print("You have been warned.")
        time.sleep(5)
        os.system('shutdown -p -f')

    @staticmethod
    def bug(*args):
        """RuntimeError: Uh oh something's broken..."""
        commands.bug.__doc__ = random.choice(["RuntimeError: Uh oh something's broken...", "Bug? Where?", "It's not a bug, it's a feature.", "Error 404: Funny joke not found."])
        print(commands.bug.__doc__)

    @staticmethod
    def meaningoflife(*args):
        """The Answer to the Ultimate Question of Life, the Universe, and Everything."""
        print("The Answer to the Ultimate Question of Life, the Universe, and Everything is '42'.")

    @staticmethod
    def rainbow(*args):
        """Cycle through terminal background colors."""
        for color in '0123456789abcdef0':
            os.system(f'color {color}7')
            time.sleep(0.1)

    @staticmethod
    def minecraft(*args):
        """Awww man!"""
        print('██  ██')
        print(' ▄██▄ ')
        print(' █▀▀█ ')

    @staticmethod
    def browser(*args):
        """Open a browser window and navigate to a url.\n\nUsage:\n\tbrowser <url>\n\nArguments:\n\t<url>  url to navigate to"""
        import webbrowser
        chromePath = 'C:/Program Files/Google/Chrome/Application/chrome.exe'
        if not os.path.exists(chromePath):
            chromePath = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe'
        webbrowser.get(chromePath + ' %s').open_new_tab(''.join(args))

    @staticmethod
    def google(*args):
        """Search Google.\n\nUsage:\n\tgoogle [keyword...]\n\nArguments:\n\t[keyword...]  keywords to search for"""
        commands.browser(f"https://www.google.com/search?q={'+'.join(args)}")

    @staticmethod
    def memes(*args):
        """Ah yes, memes.\n\nUsage:\n\tmemes [keyword...]\n\nArguments:\n\t[keyword...]  keywords to add to the search query"""
        commands.google(*args, 'memes')

    @staticmethod
    def yoda(*args):
        """Say something, I will."""
        commands.quote('yoda')
        time.sleep(1)
        commands.browser('https://www.google.com/search?q=yoda&tbm=isch')

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
    def duckroll(*args):
        """Nothing sinister going on here."""
        commands.browser('https://i.kym-cdn.com/photos/images/newsfeed/000/002/941/Duckroll.jpg?1243959393')

    @staticmethod
    def ipinfo(*args):
        """Show public and private IP address."""
        import socket
        from requests import get
        privateIP = [ip for ip in socket.gethostbyname_ex(socket.gethostname())[2] if ip.startswith("192.168.")][:1]
        print(f"Host name: {socket.gethostname()}")
        print(f"Private IP: {privateIP[0]}")
        print(f"Public IP: {get('https://api.ipify.org').text}")

    @staticmethod
    def starlink(*args):
        """Show Starlink satellite info."""
        from requests import get
        from re import search, IGNORECASE
        response = get('https://en.wikipedia.org/wiki/Starlink').text
        orbiting = search(r'Total satellites currently working .*: (\d+)', response, IGNORECASE)
        launched = search(r'Total satellites launched .*: (\d+)', response, IGNORECASE)
        deorbited = search(r'Total satellites failed or deorbited .*: (\d+)', response, IGNORECASE)
        print(orbiting.group(0))
        print(launched.group(0))
        print(deorbited.group(0))

    @staticmethod
    def rockpaperscissors(*args):
        """Play "rock, paper, scissors" against the most powerful AI on the planet."""
        options = {
            'paper': 'rock',
            'scissors': 'paper',
            'rock': 'scissors'
        }
        player = input("Enter rock, paper, or scissors: ").lower().strip()
        if player in options.keys():
            ai = random.choice(list(options.keys()))
            print(f"AI: {ai}")
            if options[player] == ai:
                print("You won!")
            elif options[ai] == player:
                print("You lost.")
            else:
                print("Tie!")
        else:
            print(random.choice(["Nope.", "I'm disappointed.", "Try again.", "Better luck next time."]))

    @staticmethod
    def birthday(*args):
        """Show birthday and age info.\n\nUsage:\n\tbirthday <date>\n\nArguments:\n\t<date>  your date of birth in yyyy/mm/dd format"""
        if not args:
            print(commands.birthday.__doc__)
            return
        from datetime import date
        try:
            dob = date(*[int(i) for i in args[0].split("/")])
        except ValueError:
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
    def joke(*args):
        """Funny jokes."""
        jokes = [
            "Why did the bike fall over?\nIt was two-tired.",
            "What did the ocean say to the shore?\nNothing. It just waved.",
            "Why did the gym close down?\nIt just didn't work out.",
            "What do you call a pig that does Karate?\nA pork chop.",
            "What's the best thing about Switzerland?\nI don't know, but the flag is a big plus.",
            "What kind of tree can fit in your hand?\nA palm tree!",
            "Today at the bank, a woman asked me to check her balance. So I pushed her over.",
            "What did the traffic light say to the car?\n'Don't look! I'm about to change.'",
            "What ryhmes with orange?\nNo, it doesn't.",
            "What did the plate say to his friend?\nTonight, dinner's on me!",
            "How do trees get online?\nThey just log on!",
            "My daughter wanted a Cinderella-themed party, so I invited her friends and made them clean the house.",
            "'Can I watch the TV?'\nDad: 'Yes, but don't turn it on.'",
            "Are you free tonight?\nNo, I'm expensive.",
            "Why did the kid throw his clock out of the window?\nBecause he wanted to see time fly.",
            "What do you call a snake that is exactly 3.14 meters long?\nA πthon.",
            "What did the Science book say to the Math book?\nWow, you've got problems.",
            "What happened when the strawberry attempted to cross the road?\nThere was a traffic jam!",
            "Your WinRAR 30-day trial is up. Please pay to continue using service.",
            "Parallel lines have so much in common. It's a shame they'll never meet.",
            "People say nothing is impossible, yet I do nothing every day."
        ]
        print(random.choice(jokes))

    @staticmethod
    def fact(*args):
        """Random facts."""
        facts = [
            "The Mona Lisa has no eyebrows.",
            "The sentence, \"The quick brown fox jumps over the lazy dog\" uses every letter in the English alphabet.",
            "\"Sixth sick sheik's sixth sheep's sick\" is said to be the toughest tongue twister in the English language.",
            "111,111,111 x 111,111,111 = 12,345,678,987,654,321",
            "The world's longest French fry is 34 inches long.",
            "The record for the longest long jump is held by Mike Powell: 29 ft. 4 inches. That's like jumping the length of two minivans!",
            "A crocodile cannot stick its tongue out.",
            "The word computer 'bug' was inspired by a real bug. It was founded by Grace Hopper in 1947.",
            "The first programming language was called Fortran, and it was created in the 1950s.",
            "The Sun is so large that approximately 1.3 million Earths could fit inside.",
            "There is no atmosphere in space, which means that sound has no medium or way to travel to be heard.",
            "A day on Venus lasts 243 days, and a year is 224 days.",
            "Dwight D. Eisenhower was the first President of all 50 states.",
            "Tennis for Two (Pong) is widely considered the oldest video game in the world.",
            "The Golden Gate Bridge's clearance above high water averages 220 feet (67 meters).",
            "Generally, a horse has 205 bones (54 vertebral column, 36 ribs, 1 sternum, 34 skull, 40 front legs, and 40 hindlegs).",
            "'Set' has 464 definitions in the Oxford English Dictionary. 'Run' runs a distant second, with 396.",
            "Fish need oxygen too, but since they don't have lungs, they take oxygen from the water in which they live.",
            "The best code is code you didn't have to write."
        ]
        print(random.choice(facts))

    @staticmethod
    def quote(*args):
        """Wise quotes."""
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
            '"It\'s a trap!" - Admiral Ackbar',
            '"Never tell me the odds." - Han Solo',
            '"I find your lack of faith disturbing." - Darth Vader',
            '"It\'s not my fault." - Han Solo',
            '"No. I am your father." - Darth Vader',
            '"There\'s always a bigger fish." - Qui-Gon Jinn',
            '"Unlimited power!" - Darth Sidious',
            '"A long time ago in a galaxy far, far away..." - Star Wars',
            '"I don\'t like sand." - Anakin Skywalker',
            *yoda
        ]
        all = [
            '"There are 10 types of people in the world: Those who understand binary and those who don\'t." - The Talos Principle',
            '"You monster." - GLaDOS',
            *yoda,
            *starwars
        ]
        groups = {
            'yoda': yoda,
            'starwars': starwars
        }
        if args and args[0] in groups.keys():
            print(random.choice(groups[args[0]]))
        else:
            print(random.choice(all))

    @staticmethod
    def whosonfirst(*args):
        """Abott & Costello - Who's on First"""
        whos_on_first = [
            "Abott: There is a baseball team at the retired actors home and I am the manager."
            "Costello: Yes, I would like to join the retired baseball team.",
            "Abbott: Oh, you would, would you?",
            "Costello: I'd like to know some of the guys on the team.",
            "Abbott: You know, they give baseball players nowadays very peculiar names.",
            "Abbott: Okay, well let's see who we have on our team... we have Who's on first, What's on second, and I Don't Know is on third.",
            "Costello: That's what I want to find out, the guys name...",
            "Abott: I am telling you, Who's on first, What's on second, and I Don't Know is on third ",
            "Costello: Who's on first?",
            "Abbott: Yes.",
            "Costello: I mean the guy's name.",
            "Abbott: Who.",
            "Costello: The man playing first base.",
            "Abbott: Who.",
            "Costello: I am asking you who's on first base.",
            "...",
            "Costello: You got an outfield?",
            "Abbott: Naturally, Why.",
            "Costello: Because I want to know, because.",
            "Abbott: He is center field.",
            "...",
            "Costello: I don't give a darn!",
            "Abbott: Oh he's our shortstop!"
        ]
        for line in whos_on_first:
            print(line)
            time.sleep(1)
        commands.browser("https://www.youtube.com/watch?v=kTcRRaXV-fg")


commands.boot()
# INPUT LOOP
while True:
    try:
        # Get input from the user and split it into words
        command = shlex.split(input(prefix))
        # Call a function from the commands class that matches the first word, with the rest of the words as arguments
        # If a matching function doesn't exist, call the default function
        if command:
            getattr(commands, command[0], commands.default)(*command[1:])
    except KeyboardInterrupt:
        # If the user pressed Ctrl+C, exit gracefully
        print("\nShutting down...")
        break
    except Exception as exception:
        # If something breaks, print the exception message
        if debug:
            print(f"Exception: {exception}")
