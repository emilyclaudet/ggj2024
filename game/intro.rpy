label intro:
    scene black
    "The warden is bringing you to your cell after you have been 'sentenced.'"
    scene prison with dissolve
    show warden with dissolve
    m "Ha ha! Welcome to the Interdimensional Prison for Villains! Within these walls are..."
    show warden at left with moveinleft
    show queen with dissolve
    m "the most dastardly!"
    hide queen with dissolve
    show osbald with dissolve
    m "the most deceiving!"
    hide osbald with dissolve
    show kagami with dissolve
    m "the most conniving!"
    m "convicts you will ever lay your eyes on...!"
    hide kagami with dissolve
    show warden at center with moveinright
    menu:
        m "And what does the defendent, [playername], have to say for themselves?"
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
    "There's a schedule on the wall..."
    show schedule at top with dissolve
    "Activities for next 3 days."
    hide schedule with dissolve
    "First there's breakfast..."
    jump chapter1
