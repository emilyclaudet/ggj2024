# The script of the game goes in this file.
# The game starts here.

label start:
    $ playername = renpy.input("What is your name, convict?", default = "Convict")
    $ playername = playername.strip()
    if playername == "":
        $ playername = "Convict"
    jump chapter_1

label chapter_1:
    scene black
    "The warden is bringing you to your cell after you have been 'sentenced.'"
    scene prison with dissolve
    show mickey with dissolve
    m "Ha ha! Welcome to the Interdimensional Prison for Villains! Within these walls are..."
    hide mickey with dissolve
    show shadow with dissolve
    m "the most dastardly!"
    m "the most deceiving!"
    m "the most conniving!"
    m "convicts you will ever lay your eyes on...!"
    hide shadow with dissolve
    show mickey with dissolve
    menu:
        m "And what does the defendent have to say for themselves?"
        "I didn’t do anything wrong!":
            m "You know what you did! Don’t act like you don’t belong."
        "Woah- This place is so weird!":
            m "Wait until you see the courtyard!"
        "Has anyone ever told you that you have an amazing fashion sense?":
            m "*Angry* Flattery will get you nowhere with me!"
    m "As I was saying- once you get to your cell, you will be given your schedule. Make sure to keep your head down! The other inmates aren’t as friendly as I am!"
    jump chapter_1_cell

label chapter_1_cell:
    scene black with dissolve
    "There's a schedule on the wall..."
    show schedule at top with dissolve
    "Activities for next 3 days."
    hide schedule with dissolve
    "First there's breakfast..."
    jump chapter1_canteen

label chapter1_canteen:
    scene prison with dissolve
    m "Alrighty, folks! Make your way to the mess hall! Can’t work on an empty stomach!"
    show mickey with dissolve
    m "Hey there! You look lost! We have loads of new… Erm- friends you can make! Just look over there!"
    m "Don’t they look nice? Why don’t you go and talk to them?"
    hide mickey with dissolve
    "First villain canteen intro dialogue..."
    show kagami with dissolve
    k "Oho… You dare to approach me? One more step and it could cost you your life."
    jump end

label end:
    return
