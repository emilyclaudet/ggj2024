label chapter1:
    scene prison with dissolve
    show warden neutraltalk with dissolve
    play sound bell
    m "Alrighty, folks!"
    m "Make your way to the mess hall! Can't work on an empty stomach!"
    scene canteen with dissolve
    play music dreamtheme
    show warden happytalk with dissolve
    m "Hey there! You look lost! We have loads of new…"
    show warden neutraltalk with dissolve
    m "Erm- friends you can make! Just look over there!"
    hide warden with dissolve
    show queen with dissolve
    show osbald muscle at center with dissolve
    show kagami at left with dissolve 
    m "Don't they look nice? Why don't you go and talk to them?"
    menu: 
        "Sit next to the chic pretty man":
            jump chapter1_kagami
        "Sit next to the gangster":
            jump chapter1_oswald
        "Sit next to spider lady":
            jump chapter1_queen

label chapter1_kagami:
    scene canteen with dissolve
    show kagami with dissolve
    u "Oho… You dare to approach me? One more step and it could cost you your life."
    menu:
        "Take a step forward":
            jump kagami_optionA
        "Take a step back":
            jump kagami_optionB

label kagami_optionA:
    n "You ignore his threat and takes another step forward. Silence fills the space between them. Nothing seemed to have happened."
    n "The strange man looks at you perplexed before pointing at you angrily."
    u "Uh - I was merely testing you, mortal. >:c! You are not worthy of my hyper blast fist of the south star."
    "You nod, stifling a laugh, before they sit next to the strange man."
    menu:
        "Ask him his name.":
            u "..."
    show kagami with dissolve
    u "... ..."
    u "... ... ..."
    show kagami annoyed with dissolve
    u "You've lost the privilege of learning my name. It is a word carrying the weight and brutality within this prison ward."
    u "Uttering it, even for a moment, would cause this prison society to cave in."
    menu:
        "Ah…that's so lame - I'll just call you cringelord then.":
            c "W-WHAT-matte matte!!-- Ah heck, I mean WAIT."
    c "Ahem…I'll allow you to hear my name just once. You've proven yourself to be a powerful foe."
    menu: 
        "I don't know if I really want to know anymore, Cringelord just…oh, I don't know…just rolls off the tongue whenever I conceptualize you.":
            c "shocked face...."
    n "Defeated, Cringelord hangs his head."
    menu:
        "Relax, I was just testing you like you did me earlier.--I'm [playername]":
            n "You felt a bit bad for breaking the illusion of “coolness” for this guy."
            n "Though he was a bit cringe, he was an entertaining and oddly vibrant breath of fresh air in this otherwise dulled and surreal hellscape."
    n "Cringelord shifts his gaze upwards..."
    c "Kagami…"
    show kagami with dissolve
    k "It's not nice to meet you - but I suppose, having a lackey understand the beauty of my power is worthwhile."
    n "Kagami gets up from his seat, getting ready to leave before he turns around to face you again."
    show kagami happy with dissolve
    k "But just know, that next time, I'll turn you into toad oil if you get on my bad side again."
    hide kagami with dissolve
    n "You watch Kagami leave."
    n "You felt bewildered but decided to not think about the weird guy anymore and instead focused on the weird dystopian slop on his plate…known as a bhocolate bhip bookie."
    jump chapter1end

label kagami_optionB:
    n "You nervously step backwards, feeling a wall of intimidation blocking your path forward."
    u "As you should, hmph. Glad someone around here understands the wonders of my powers. The name's Kagami - come, you are permitted to enter my domain."
    menu:
        "I'm uh, [playername].":
            n "You sit a bit further away from the intimidating man, placing your slop of food on the table as you lay eyes on the villain."
    k "Bhocolate Bhip Bookies, huh? I'm more of a Bhicken Bugget person—though, your taste in meals are as good as your taste in seating partners." 
    menu:
        "Seating partners?":
            k "Aha, is that not what we are?"
    n "Kagami lets out a thunderous roar of laughter."
    k "My dear lackey, you have chosen wisely. I have been in this domain expansion before…"
    k "You see, I was a murderer - reformed and then..unformed…I murdered again and here we are."
    k "Choosing a person to sit with for a meal- an expert of this prison, in fact…why, you may have just saved yourself from being killed."
    n "Kagami gives you a smug grin, nudging his shoulder at them before he takes a bite of his bhicken bugget."
    menu:
        "Is this place really that dangerous?":
            k "Not as dangerous as myself - buuut, I guess you could say it comes in at a close third place. Second has to go to Steamboat Warden Willie."
    n "You reflect over your interactions with the Steamboat Warden Willie, his threatening and booming voice sent shivers down your spine."
    n "Though, this Kagami guy was nothing in comparison…he felt more like a gentle gust of wind that sent a piece of dirt in your eye, if anything."
    menu:
        "Ah…I see.":
            n "You finish the last of your Bhocolate Bhip Bookies before Kagami continues his monologue of being the most powerful prisoner."
    n "You wave at Kagami as he is mid monologue and darts away."
    jump chapter1end

label chapter1_oswald:
    scene canteen with dissolve
    n "You approach the grim bulky figure sitting at the far table."
    show osbald muscle with dissolve
    n "He doesn't appear to eating anything, just holding in coughs and gasp from repeatedly taking hits from his comically large pipe."
    n "You're about to sit down but pause when he glares at you."
    show osbald muscleupset with dissolve
    oz "You want something boy?"
    menu:
        "Can I try your pipe?":
            show osbald muscle with dissolve
            oz "shove it up yer ass."
            n "The fact that he doesn't offer you the pipe leads you to believe he isn't offering to insert the pipe into your rear."
        "Can I sit next to you?":
            show osbald muscle with dissolve
            oz "Guess kid."
        "Can I eat that? It looks like you haven't touched it…":
            oz "Keep talking like that boy they only think y'll be eatin is the heel of my Size 35 Meher Kakalia Queen Bauhaus Point - Shiny Black Boots."
            "You look down at his feet but you can't really tell what he's wearing, they're just black blobs"
    n "You stay silent."
    show osbald muscleevilgrin with dissolve
    oz "That's what I thought punk."
    oz "Scram if ya know what's good for ya."
    menu:
        "Scram":
            jump chapter1_oswald_optionA
        "Take a bite of his food.":
            jump chapter1_oswald_optionB
        "Lean in for a kiss":
            jump chapter1_oswald_optionC
        "Sit down next to him":
            jump chapter1_oswald_optionD


label chapter1_oswald_optionA:
    n "You scram."
    show osbald muscle with dissolve
    oz "..."
    oz "Lame."
    jump chapter1end

label chapter1_oswald_optionB:
    show osbald musclebadsurprised with dissolve
    oz "AW! What the devil! You tryna start something kid!"
    n "He puts his paws up like John L. Sullivan and starts rhythmically circling them while slowly bobbing his whole body up and down."
    show warden at left with dissolve
    m "Say fellas, do we have a problem here?"
    show osbald musclesurprised with dissolve
    n "Oswald jumps as Willie clasps his shoulder from behind."
    n "Willie is grinning, lips stretched ear to ear, and his emotionless pitch black eyes fix robotically onto Oswald."
    show osbald muscleupset with dissolve
    oz "N-non-nothin boss I was just-"
    show warden happytalkright with dissolve    
    m "hoHO! Of course not! You wouldn’t want to get into any more trouble with me."
    show warden neutraltalkright with dissolve
    m "Would you Oz?"
    oz "N-no Mister Steamboat Warden Willie- sir."
    hide warden with dissolve
    show osbald muscle with dissolve
    oz "*whispers* You lucky the rat is watching."
    n "Before you can do anything else he walks over to the corner of the cafeteria to inhale more smoke."
    n "He inhales too much and starts gagging."
    n "You might want to consider this one a lost cause."
    jump chapter1end

label chapter1_oswald_optionC:
    show osbald musclebadsurprisedred with dissolve
    n "As you come within inches of his face he blushes for a moment before lurching back"
    oz "Aw! What the devil! You tryna start something kid!"
    n "He puts his paws up like a boxer from the 20s and starts rhythmically circling them while slowly bobbing his whole body up and down."
    show warden angry at left with dissolve
    m "Say fellas, do we have a problem here?"
    show osbald musclesurprised with dissolve
    n "Oswald jumps as Willie clasps his shoulder from behind."
    show warden excited with dissolve
    n "Willie is grinning, lips stretched ear to ear, and his emotionless pitch black eyes fix robotically onto Oswald."
    show osbald muscleupset with dissolve
    oz "N-non-nothin boss I was just-"
    show warden happytalkright with dissolve
    m "hoHO! Of course not! You wouldn't want to get into any more trouble with me."
    show warden neutraltalkright with dissolve
    m "Would you Oz?"
    oz "N-no Mister Steamboat Warden Willie- sir."
    hide warden with dissolve
    show osbald muscle with dissolve
    oz "*whispers* You lucky the rat is watching."
    n "Before you can do anything else he walks over to the corner of the cafeteria to inhale more smoke."
    n "He inhales too much and starts gagging."
    n "You might want to consider this one a lost cause."
    jump chapter1end

label chapter1_oswald_optionD:
    show osbald muscleupset with dissolve
    n "He glares at you. Again. It looks like he's trying to be more intimidating than before… but it sort of just looks like he's constipated."
    hide osbald muscleupset with dissolve
    n "Before you can do anything else he walks over to the corner of the cafeteria to inhale more smoke."
    n "He inhales too much and starts gagging."
    n "You might want to consider this one a lost cause."
    jump chapter1end

label chapter1_queen:
    scene canteen with dissolve
    n "You walk up to the beautiful spidery woman."
    n "She is stabbing her food with her long legs and eating off of them."
    show queen with dissolve
    menu queen_questions1:
        "What are you in here for?":
            show queen happy with dissolve
            q "I tried making everyone beautiful with 8 arms, like me."
            q "The whole world was nearly full of my little slave children. If not for that tiny prince's luck, they all would've been mine!"
            $ queenchoice1 = True
            jump queen_questions1
        "What's your name?":
            show queen annoyed with dissolve
            q "Hmm so you're a new little maggot in this prison, bold enough to ask my name?"
            q "I am Mother Arachnificent, you should know me."
            $ queenchoice2 = True
            jump queen_questions1
        "You're a mother?" if queenchoice1 and queenchoice2 == True:
            show queen happy with dissolve
            q "I have 5000 adorable little spider children. They are always hungry."
            jump queen_questions1
        "Tiny prince?" if queenchoice1 and queenchoice2 == True:
            show queen happy with dissolve
            q "You're a nosy lost soul aren't you?"
            jump queen_questions1
        "Stop asking questions":
            jump chapter1_queen_questions2

label chapter1_queen_questions2:
    show queen with dissolve
    q "Little maggot, what villainous thing could you possibly be in here for?"
    menu queen_questions2:
        "I'm innocent!":
            show queen happy with dissolve
            q "Ahahahah you unfortunate fool. You're fresh bait in this world! evil laugh"
        "I'm actually mass murderer":
            show queen annoyed with dissolve
            q "And a terrible liar."
        "I was too hot and seggsy":
            show queen annoyed with dissolve
            q "Your form is hideous, that cannot possibly be true."
    q "Well, goodbye little maggot, I cannot wait to see how you get torn apart in here."
    jump chapter1end

label chapter1end:
    scene prison with dissolve
    show warden happy with dissolve
    m "You aren't getting too friendly with the other's, right? Don't want to have any escapees on my watch! Ha. Ha."
    show warden neutralleft with dissolve
    m "Haha I'm joking."
    show warden happy with dissolve
    m "Anyways! Back to your regularly scheduled programming!"
    jump chapter2

