label ending_choice:
    scene black with dissolve
    show warden with dissolve
    m "It’s the day you’ve been waiting for! The day where you get to pick… who you get to work out with! This decision could impact your entire future!"
    #The scene fades to the gym, Mickey and all three villains are there.
    m "Well, well, well. Look who we have here."
    #[Looks in the direction the villains are then back at the player] 
    show warden at left with moveinleft
    m "So who will you choose?"
    show queen at right with dissolve
    m "The beautiful and- frankly terrifying- Queen Arachnificent!"
    hide queen with dissolve
    show oswald at right with dissolve
    m "The not-so-intimidating Osbald?"
    hide oswald with dissolve
    show kagami at right with dissolve
    m "Or, how about the mysterious and edgy Kagami?"
    hide kagami with dissolve
    menu:
        "My Queen, of course!":
            jump ending_queen
        "I’d like to go with the hunk!":
            jump ending_oswald
        "Give me that bracelet baddie!":
            jump ending_kagami
        "Why can’t I just choose all three?":
            jump ending_allthree
        "... My heart belongs with you, Warden.":
            jump ending_warden

label ending_kagami:
    hide warden with dissolve
    show kagami with dissolve
    k "If it isn’t my loyal lackey, why are you standing cooly against a wall like a mysterious anime protagonist?"
    "You realize that Mickey Mouse is a formidable foe stopping you from escaping the hellish dreamscape."
    menu:
        "Kagami I need your help.":
            "Kagami moves closer, eager to hear that you actually value him as an individual."
    "You explain to him your plan of wanting to escape, but struggle in actually doing so due to the Warden’s watchful eye."
    k "Aha, why didn’t you just ask me earlier?! Step back, lackey. I’ll turn this wall in front of us into a portal into the mortal realm!"
    "Kagami lets out a deep breath, his eyes darker and much more menacing than before…You begin to wonder if he, perchance, does have actual powers."
    "He raises his arms, then in one powerful swoop–he shoves his hands at the wall."
    k "OPEN SESAME!"
    "The force of his hands impacting the rugged stone wall left muffled echoes of his attack."
    "The wall remained unphased by Kagami and you find yourself wondering why you ever bothered asking him."
    k "It was a…miss input–I just need to focus on my chakra!"
    "You stare at Kagami as he continues hitting his hand against the wall."
    "The only damage being done here seems to be your brain cells as you continue to steel yourself against the cringe you’re witnessing."
    p "Kagami..."
    k "Just hang on–this wall’s gonna burst aaany second now."
    p "Kagami stop lying to yourself."
    "He halts his barrage on the wall and faces you. His expression is sullen."
    p "You’re not really a villain are you?"
    k "[playername]..."
    p "The only crime you did was having poor fashion taste, isn’t it?"
    k "That’s not true! My fashion is iconic… you just don’t have a 5-star, SSS fashion sense like I do!"
    # kagami frustrated expression
    "Kagami lets out a frustrated sigh, running a hand through his hair."
    k "But…I never murdered anyone…"
    p "Yeah I could tell by your honey fists hitting the wall. If anything, it looked like you were giving it a well deserved massage."
    "Kagami ignored your remark."
    k "The first time I came here…it was from repeated Jaywalking…"
    p "...Really?"
    k "The urge to be diagonal was too strong to resist…The speed…The velocity…It felt like I was Sanic the Speedster in that moment…"
    "He let out a passionate sigh, balling his fists as he looked longingly at the sky."
    k "And now…I’m in jail for tax fraud."
    p "That one actually seems serious, color me surprised!"
    k "[playername]...The pain of not understanding taxes was too daunting for me–THEY NEVER TAUGHT IT IN SCHOOL…granted I always skipped classes–BUT STILL."
    k "I blame society for causing me to fail…"
    p "Sounds like a skill issue."
    k "And a skill issue it may be…and a failure I am…"
    k "I have no lackeys…no gang of menacing monsters…"
    k "Only my Sunday Funday anime club members…but sadly it's Saturday–so I have…no one."
    p "Ahhh…it’s all making sense now."
    k "Me being a failure?"
    p "No, why you’re so cringe."
    "Kagami looks at you with distraught before sadly agreeing with a pitiful nod."
    k "[playername]...I don’t want to be in this crusty dusty musty prison anymore."
    p "Neither do I…"
    k "...A new season of Jim Jim’s Mild Ventures came out before I got arrested."
    "I can’t bear the thought of coming back to the mainland and getting spoiled–I need to get out of here before it’s too late."
    "The fate of the Bowl Society rests in my hands, [playername]!"
    p "B-Bowl…society?"
    k "The legion of fierce warriors, my comrades in arms–it is what we call our anime club."
    "You bite down on your inner cheek, resisting the urge to laugh at the crude name."
    k "We all…get bowl hair cuts together at the start of each year so–"
    p "Nope, nope…no need to explain. Bowl society needs to be saved."
    "Kagami nods at your response, but soon lets out an exasperated sigh."
    k "But how can we even escape…we have nothing.."
    p "That’s not true Kagami!"
    "He looks at you in confusion."
    p "Haven’t you learned anything from all of our bracelet making? We have the power of friendship! I’m sure we can…figure…something out…"
    "Your voice trails off with uncertainty. Maybe there really was no way to get out of here…"
    k "I’VE GOT IT!!"
    p "Eh?"
    k "OUR FRIENDSHIP BRACELETS!!"
    p "...Eh?"
    k "THE POWER OF FRIENDSHIP THAT TRANSCENDS THROUGH SPACE AND TIME!"
    "Kagami pulls out the bracelets you both made together."
    k "Put your hand on these bracelets!"
    "You hesitate, but the unwavering determination on Kagami’s face convinces you to give it a shot."
    "You place your hand over the bracelets in his hand…and you begin to feel the strung up orbs whirl against your palm."
    p "EEEEEEH?!"
    k "Don’t you see [playername]? Our friendship…is giving us the power to escape this place, I can feel it!"
    "Dumbfounded, you could only listen to Kagami’s ecstatic excitement as the whirling orbs created a large black hole above them."
    "You glance up and see something strange poking out of it until–"
    "BONK"
    "The bracelets fall onto the ground with an array of clinks and clanks."
    k "That was so not sugoi…"
    "He let out a groan as he rubbed his aching head."
    "You pick up the mysterious item that nearly gave your new bestie for liferz >//o//< a mild concussion."
    p "Wait… this is…"
    "Mickey’s key–they…somehow got Mickey’s key!!"
    "You hold up the key and are startled to see a keyhole appear on the wall."
    k "That’s gotta be the way to get out…"
    "Kagami let out a light-hearted laugh."
    k "I can’t believe it…"
    p "It’s all thanks to believing in the heart of the cards–erm, uh..I mean bracelet."
    k "You place the key in the keyhole, turning back to face Kagami as you give him a reassuring smile."    
    p "We have peak anime content to watch through."
    "You twist the key and the wall before you collapse. A strange, galaxy-like pathway peers through the hole, with a distant hole imaging the mortal world."
    "At last, you’ve thwarted Mickey Mouse…and somehow gained a new friend."
    p "Kagami…"
    k "Yeah?"
    p "Let’s be cringe together."
    # play CG scene
    k "Yeah!"

label ending_warden:
    show warden at center with dissolve
    m "..."
    m "..."
    #neutral looking at player
    m "... You want to choose me?"
    menu:
        "Of course! You’re the best option I have!":
            show warden bashful with dissolve
            m "Really?"
        "Why wouldn’t I?":
            m "..."
    m "Well, if you really want to work out with me- I’d be happy to lend you a hand..."
    #Time skip. 
    jump ending_warden2

label ending_warden2:
    scene black with dissolve
    "It is 5 years later, the background is a normal park. Steamboat Warden pops up with a hint of color in his design and in normal clothes."
    show warden with dissolve
    m "...Ha ha. I’m really glad I met you [playername]. You know, ever since that day, I think what would have happened if you didn’t take a chance on me."
    m "Your kindness has helped me to see that my actions are wrong. I’m really glad you and I are friends."
    m "..."
    m "...Hey [playername]? Do you... do you think we could ever be friends? Like real and genuinely close friends?"
    menu:
        "I would love that.":
            #smiles
            m "Me too."
        "Maybe one day… I still think we both have growing to do.":
            #smiles
            m "I understand. I hope we can keep meeting like this? Until next year?"
        "I’m sorry, but I don’t think that’s possible.":
            #smiles and closes eyes
            m "That’s fair. Hey, take care will yah?"
    jump end

label end:
    return

