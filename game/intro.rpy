label intro:
    scene black
    n "The warden is bringing you to your cell after you have been 'sentenced.'"
    scene prison with dissolve
    show warden with dissolve
    m "Ha ha! Welcome to the Interdimensional Prison for Villains! Within these walls are..."
    show warden at left with moveinleft
    show queen with dissolve
    m "the most dastardly!"
    hide queen with dissolve
    show osbald at right with dissolve
    m "the most deceiving!"
    hide osbald with dissolve
    show kagami at right with dissolve
    m "the most conniving!"
    m "convicts you will ever lay your eyes on...!"
    hide kagami with dissolve
    show warden at center with moveinright
    m "And what does the criminal, [playername], have to say for themselves?"
    menu:
        "I didn’t do anything wrong!":
            m "You know what you did! Don’t act like you don’t belong."
        "Woah- This place is so weird!":
            m "Wait until you see the courtyard!"
        "Has anyone ever told you that you have an amazing fashion sense?":
            m "*Angry* Flattery will get you nowhere with me!"
    m "As I was saying- once you get to your cell, you will be given your schedule. Make sure to keep your head down! The other inmates aren’t as friendly as I am!"
    jump intro_cell

label intro_cell:
    scene black with dissolve
    n "There's a schedule on the wall..."
    show schedule at top with dissolve
    n "Activities for next 3 days."
    hide schedule with dissolve
    n "First there's breakfast..."
    jump chapter1
