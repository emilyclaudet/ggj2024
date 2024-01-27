#first is the queen

label chapter2:
    scene black with dissolve
    "You are in the trash area"
    show warden with dissolve
    m "Ha ha! C'mooon fellas, it's time to pick up the trash if you want your next meal!"
    hide warden with dissolve
    "You see the same beautiful tall spidery woman glaring at the piles of trash. Her legs and chins jiggle majestically as she walks, her devious smile is enough to set the trash on fire. Metaphorically."
    show queen with dissolve
    q "These specks of trash are beneath me."
    q "Oh! It's you little maggot."
    menu:
        "Ask if she comes around here often":
            #scowl expression
            q "I am Mother Arachnificent, the queen of all evil. Of course I'm in the place for the most dangerous of villains."
        "Tell her she is super hot":
            #scowl expression
            q "A new maggot like you has no place talking to Mother Arachnificent in such a way."
    menu:
        "Sorry I meant no disrespect to your evil highness! So you’re a mother?":
            q "I am mother to over 5000 little spider children. They will eat anyone, they have a lovely appetite."
            #sly expression
            q "I miss those little darlings."
        "I love all your many legs, you are truly the fairest in the lands ;3":
            #scowl
            "No need to point out something so obvious."
    show warden at left with dissolve
    m "Haha I would advise you to stay focused on taking out the trash!"
    #show queen furious
    q "I would love to watch my sweet minions tear that rodent apart."
    hide warden with dissolve
    menu:
        "Pick up trash for her while tripping cutely and incompetently.":
            q "hmmm I am worthy of having minions, and you clearly need an overlord or someone will tear your poor soul apart. Go on, clear the trash so we can get through this quickly!"
        "Pick up trash for her while flexing your muscles and winking cutely.":
            q "Your pathetic display of strength does not fool me."
            # show queen annoyed 
            q "But you clearly need an overlord or someone will tear your poor soul apart. Go on, clear the trash so we can get through this quickly!"
    menu:
        "Continue picking up the trash quickly while tripping cutely and incompletely":
            #show queen smile
            q "Ahahahah you are truly a pathetic soul in need of an overlord."
        "Continue picking up the trash quickly while flexing your muscles":
            q "Quit trying to show off and get the job done!"
        "Stop picking up the trash":
            q "You fool! Who told you you could stop?!"
    "You continue picking up the trash, most of it is cleared. Arachnificent smiles, pleased. She starts decorating her crown with extra silken webs. How do you keep her attention?"

    menu:
        "Juggle the trash in the air":
            q "Ahahahah you are such a meek fool!"
        "Pick your nose and wipe it on the trash while looking at her suggestively":
            "Arachnificent raises her eyebrows, looking at you with surprise."
            #show queen smile
            q "I didn't know little human worms could be so bold and expressive."
    "You finished clearing up the trash with the queen, and enjoyed it more than you thought you would."
    jump chapter2_mopping

label chapter2_mopping:
    scene black with dissolve
    show warden with dissolve
    m "Now that the trash has been cleared it's time to mop some floors! Have a swell ol time ha ha!"
    #show queen annoyed
    q "Finally this hell will be over soon! I cannot have my fair webs in a tangle from all this muck!!"
    #show queen smile
    q "At least I finally have a minion back to help me."
    menu:
        "Am I just a minion to you?":
            q "My little worm maggot, what are you trying to say??"
        "I'm happy to be your minion…..but…":
            q "My little worm maggot, what are you trying to say??"
    menu:
        "Confess":
            p "You are the fairest, most beautiful in all the lands! Your spidery villainy should be seen by all my queen."
        "Say nothing":
            q "?!"
            q "Whatever it is we can save it for after the cleaning, that freakish rodent is always watching."
            "You and Arachnificent peacefully mop together. The endless abyss of neon tunnels don’t seem as cold and barren anymore."
            q "Human, you have shown yourself to be quite useful. In another life I would have put you to use and taken over the world."
    menu:
        "We can still take over the world":
            jump chapter2_ending
        "I want to spend more time with you":
            jump chapter2_ending

label chapter2_ending:
    q "?!"
    "Arachnificent plays with her webs, she looks lost in thought before she shakes her head."
    q "You fool, do you really expect that fantasy to play out? Romance stories are reserved for heroes and princesses. Not villainous queens..and..whatever you are."
    menu:
        "I love you for being a villainous spider queen":
            q "..."
        "I wouldn’t want anyone else":
            q "..."
        "Why can’t villains have a love story?":
            q "..."
    q "I already have my little babies…will there really be room for you in all this?"
    menu:
        "I’m great with kids":
            q "Fuhuhuh you are trying too hard."
    "We’re in prison, we might as well enjoy our time here."
    q "You have a point human."
    menu:
        "Lean in for kiss.":
            q "?!"
        "Hold her hand.":
            q "?!"
        "Sit in her lap.": 
            q "?!"
    q "I suppose we can stay like this…a little longer."
    "You and the queen enjoy an amateurish and awkward kissing session in the quiet labyrinth."
    jump chapter3