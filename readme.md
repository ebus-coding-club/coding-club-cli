# Coding Club CLI
A collaborative command line project for the whole club.

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
## License
[MIT License](https://choosealicense.com/licenses/mit/)