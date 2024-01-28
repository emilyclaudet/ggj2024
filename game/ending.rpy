label ending_choice:
    scene prison with dissolve
    show warden with dissolve
    m "It’s the day you’ve been waiting for! The day where you get to pick… who you get to work out with! This decision could impact your entire future!"
    m "C'mon everyone, let's get going to the gym area..."
    scene gym with dissolve
    pause 1.0
    m "Well, well, well. Look who we have here."
    #[Looks in the direction the villains are then back at the player] 
    show warden at left with moveinleft
    m "So who will you choose?"
    show queen at right with dissolve
    m "The beautiful and- frankly terrifying- Queen Arachnificent!"
    hide queen with dissolve
    show osbald at right with dissolve
    m "The not-so-intimidating Osbald?"
    hide osbald with dissolve
    show kagami at right with dissolve
    m "Or, how about the mysterious and edgy Kagami?"
    hide kagami with dissolve
    menu:
        "My Queen, of course!":
            jump ending_queen
        "I’d like to go with the hunk!":
            jump ending_osbald
        "Give me that bracelet baddie!":
            jump ending_kagami
        "Why can’t I just choose all three?":
            jump ending_allthree
        "... My heart belongs with you, Warden.":
            jump ending_warden

label ending_kagami:
    scene gym with dissolve
    show kagami with dissolve
    k "If it isn’t my loyal lackey, why are you standing cooly against a wall like a mysterious anime protagonist?"
    n "You realize that Steamboat Warden is a formidable foe stopping you from escaping the hellish dreamscape."
    menu:
        "Kagami I need your help.":
            "Kagami moves closer, eager to hear that you actually value him as an individual."
    n "You explain to him your plan of wanting to escape, but struggle in actually doing so due to the Warden’s watchful eye."
    k "Aha, why didn’t you just ask me earlier?! Step back, lackey. I’ll turn this wall in front of us into a portal into the mortal realm!"
    n "Kagami lets out a deep breath, his eyes darker and much more menacing than before…You begin to wonder if he, perchance, does have actual powers."
    n "He raises his arms, then in one powerful swoop–he shoves his hands at the wall."
    k "OPEN SESAME!"
    n "The force of his hands impacting the rugged stone wall left muffled echoes of his attack."
    n "The wall remained unphased by Kagami and you find yourself wondering why you ever bothered asking him."
    k "It was a…miss input–I just need to focus on my chakra!"
    n "You stare at Kagami as he continues hitting his hand against the wall."
    n "The only damage being done here seems to be your brain cells as you continue to steel yourself against the cringe you’re witnessing."
    p "Kagami..."
    k "Just hang on–this wall’s gonna burst aaany second now."
    p "Kagami stop lying to yourself."
    n "He halts his barrage on the wall and faces you. His expression is sullen."
    p "You’re not really a villain are you?"
    k "[playername]..."
    p "The only crime you did was having poor fashion taste, isn’t it?"
    k "That’s not true! My fashion is iconic… you just don’t have a 5-star, SSS fashion sense like I do!"
    # kagami frustrated expression
    n "Kagami lets out a frustrated sigh, running a hand through his hair."
    k "But…I never murdered anyone…"
    p "Yeah I could tell by your honey fists hitting the wall. If anything, it looked like you were giving it a well deserved massage."
    n "Kagami ignored your remark."
    k "The first time I came here…it was from repeated Jaywalking…"
    p "...Really?"
    k "The urge to be diagonal was too strong to resist…The speed…The velocity…It felt like I was Sanic the Speedster in that moment…"
    n "He let out a passionate sigh, balling his fists as he looked longingly at the sky."
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
    n "Kagami looks at you with distraught before sadly agreeing with a pitiful nod."
    k "[playername]...I don’t want to be in this crusty dusty musty prison anymore."
    p "Neither do I..."
    k "...A new season of Jim Jim’s Mild Ventures came out before I got arrested."
    k "I can’t bear the thought of coming back to the mainland and getting spoiled–I need to get out of here before it’s too late."
    k "The fate of the Bowl Society rests in my hands, [playername]!"
    p "B-Bowl…society?"
    k "The legion of fierce warriors, my comrades in arms–it is what we call our anime club."
    n "You bite down on your inner cheek, resisting the urge to laugh at the crude name."
    k "We all…get bowl hair cuts together at the start of each year so–"
    p "Nope, nope…no need to explain. Bowl society needs to be saved."
    n "Kagami nods at your response, but soon lets out an exasperated sigh."
    k "But how can we even escape…we have nothing.."
    p "That’s not true Kagami!"
    n "He looks at you in confusion."
    p "Haven’t you learned anything from all of our bracelet making? We have the power of friendship! I’m sure we can…figure…something out…"
    n "Your voice trails off with uncertainty. Maybe there really was no way to get out of here…"
    k "I’VE GOT IT!!"
    p "Eh?"
    k "OUR FRIENDSHIP BRACELETS!!"
    p "...Eh?"
    k "THE POWER OF FRIENDSHIP THAT TRANSCENDS THROUGH SPACE AND TIME!"
    n "Kagami pulls out the bracelets you both made together."
    k "Put your hand on these bracelets!"
    n "You hesitate, but the unwavering determination on Kagami’s face convinces you to give it a shot."
    n "You place your hand over the bracelets in his hand…and you begin to feel the strung up orbs whirl against your palm."
    p "EEEEEEH?!"
    k "Don’t you see [playername]? Our friendship...is giving us the power to escape this place, I can feel it!"
    n "Dumbfounded, you could only listen to Kagami’s ecstatic excitement as the whirling orbs created a large black hole above them."
    n "You glance up and see something strange poking out of it until–"
    n "BONK"
    n "The bracelets fall onto the ground with an array of clinks and clanks."
    k "That was so not sugoi…"
    n "He let out a groan as he rubbed his aching head."
    n "You pick up the mysterious item that nearly gave your new bestie for liferz >//o//< a mild concussion."
    p "Wait… this is…"
    n "The Warden's key–they…somehow got Willie's key!!"
    n "You hold up the key and are startled to see a keyhole appear on the wall."
    k "That's gotta be the way to get out…"
    n "Kagami let out a light-hearted laugh."
    k "I can't believe it…"
    p "It's all thanks to believing in the heart of the cards–erm, uh..I mean bracelet."
    k "You place the key in the keyhole, turning back to face Kagami as you give him a reassuring smile."    
    p "We have peak anime content to watch through."
    n "You twist the key and the wall before you collapse. A strange, galaxy-like pathway peers through the hole, with a distant hole imaging the mortal world."
    n "At last, you've thwarted Steamboat Willy…and somehow gained a new friend."
    p "Kagami…"
    k "Yeah?"
    p "Let's be cringe together."
    # play CG scene
    k "Yeah!"
    jump end

label ending_osbald:
    scene gym with dissolve
    show osbald at left with dissolve
    o "Bahaha! Of course, guess I can trust ya kid."
    show warden at right with dissolve
    show osbald evilgrin with dissolve
    o "HEY RAT!!!"
    show osbald evilgrin at center with moveinright
    n "Osbald rips of his hat and overcoat in one swift motion."
    show osbaldmuscle evilgrin with dissolve
    o "Keys Kid!" with vpunch
    n "In the wardens shock you’re able to swipe the keys from his belt and throw them to Osbald."
    n "No turning back now."
    show osbaldmuscle with dissolve
    o "Tell the whole world: OSBALDS BACK!!!"
    jump end 

label ending_queen:
    scene gym with dissolve
    show queen with dissolve
    n "You and Queen Arachnificent work out together. You try to show off but Arachnificent seems distracted."
    p "Is something bothering you?"
    show queen sad with dissolve
    q "My little worm, I’ve been planning this moment for years but..I needed someone who was willing to..."
    menu:
        "What is it?":
            q "I can give you power."
        "I’ll do anything for you":
            q "I can give you power."
        "Yes! Tell me Queen <333":
            q "I can give you power."
    q "If you join me..your life will change forever. Do you accept?"
    p "I’ve made my choice, of course I will!"
    show queen happy with dissolve
    q "Then it is done."
    p "?!"
    "The Queen pricks you with one of her sharp spidery legs…you feel nauseous?? The world is fading."
    q "Little worm are you alright?"
    "You wake up..something feels different."
    "?!"
    "You have spider limbs now."
    "So cool and epic???"
    q "You are now able to understand my ancient spider tongue?"
    menu:
        "Understand you perfectly <33":
            show queen happy with dissolve
            q "You are so dependable"
        "WOAAH what is this?!!? I’m freaking out!!":
            show queen happy with dissolve
            q "Calm down my darling, you will get used to it with time."
        "This is freaking cool, I love being like you <3":
            show queen bashful with dissolve
            q "Finally someone understands."
    show queen annoyed with dissolve
    q "We can now communicate without that mousey faker dreams getting in our way."
    q "“That warden tried to snuff my archetype out…thinking I was too old for this world..BUT I WILL REIGN SUPREME AGAIN."
    p "We’re escaping together?"
    q "You catch on quickly."
    q "With both our powers combined…"
    q "..and the few hundred eggs I’ve been incubating for years for this exact moment...."
    q "..we will take over this prison, turn them all into slaves and RULE THE LANDS."
    menu:
        "..can we spare the prisoners?":
            q "..."
            show queen happy with dissolve
            q "My babies eat indiscriminately..but I will try to control them to the best of my ability. Just for you my darling."
        "..can we at least Osbald and Kagami?":
            show queen annoyed with dissolve
            q "..you really care about those fools?"
            show queen happy with dissolve
            q "Fine..my babies eat indiscriminately..but I will try to control them to the best of my ability. Just for you my darling."
        "YEEEAHAHAHAHAHHHAHAHAHAH!!!":
            show queen flirt with dissolve
            q "Exquisite reaction, I knew you’d be thrilled."   
    n "You and Queen Arachnificient escape together with your legion of spider minions. It’s a bloody battle. Many get killed or turned into spiders."
    n "Is there anyone who will stop you both?"
    n "Perhaps, perhaps not."
    n "For now you live happily together, taking over the world."
    jump end 

label ending_allthree:
    scene gym with dissolve
    "Placeholder all 3 ending."
    jump end 


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
    scene black
    "The End. Thanks for playing!"
    return

