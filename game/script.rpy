# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Eileen")
define m = Character("Mickey Mouse", color="#dd1c1c")

# The game starts here.

label start:
    scene black

    "At the Mickey Club House Prison..."

    scene prison with dissolve
    show mickey with dissolve
    m "Welcome to the Mickey Club House."
    m "You are my prisoner."
    m "And you are so so guilty."
    m "Here's your schedule for the week."
    show schedule at top with dissolve
    m "You'll be doing the mining first."
    m "Make sure to behave."
    hide schedule with dissolve
    m "Hahahahahahaha!"

    menu:
        "Go to your dorm":
            jump chapter1

label chapter1:
    scene black
    "You are now in the dorm."    

    jump end

label end:
    return
