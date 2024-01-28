# The script of the game goes in this file.
# The game starts here.

label start:
    $ playername = renpy.input("What is your name, convict?", default = "Convict")
    $ playername = playername.strip()
    if playername == "":
        $ playername = "Convict"
    jump intro
