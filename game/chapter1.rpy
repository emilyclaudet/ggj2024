label chapter1:
    scene prison with dissolve
    m "Alrighty, folks! Make your way to the mess hall! Can't work on an empty stomach!"
    show warden with dissolve
    m "Hey there! You look lost! We have loads of new… Erm- friends you can make! Just look over there!"
    m "Don't they look nice? Why don't you go and talk to them?"
    hide warden with dissolve
    menu: 
        "Sit next to gangster dude":
            jump chapter1_oswald
        "Sit next to spider lady":
            jump chapter1_queen
        "Sit next to the strangely dressed man":
            jump chapter1_kagami

label chapter1_kagami:
    show kagami with dissolve
    u "Oho… You dare to approach me? One more step and it could cost you your life."
    menu:
        "Take a step forward":
            jump kagami_optionA
        "Take a step back":
            jump kagami_optionB

label kagami_optionA:
    "You ignore his threat and takes another step forward. Silence fills the space between them. Nothing seemed to have happened."
    "The strange man looks at you perplexed before pointing at you angrily."
    u "Uh - I was merely testing you, mortal. >:c! You are not worthy of my hyper blast fist of the south star."
    "[playername] nods, stifling a laugh, before they sit next to Kagami."
    menu:
        "Ask him his name.":
            u "..."
    show kagami back with dissolve
    u "... ..."
    u "... ... ..."
    show kagami with dissolve
    u "You've lost the privilege of learning my name. It is a word carrying the weight and brutality within this prison ward."
    u "Uttering it, even for a moment, would cause this prison society to cave in."
    menu:
        "Ah…that's so lame - I'll just call you cringelord then.":
            c "W-WHAT-matte matte!!-- Ah heck, I mean WAIT."
    c "Ahem…I'll allow you to hear my name just once. You've proven yourself to be a powerful foe."
    menu: 
        "I don't know if I really want to know anymore, Cringelord just…oh, I don't know…just rolls off the tongue whenever I conceptualize you.":
            c "shocked face...."
    "Defeated, Cringelord hangs his head."
    menu:
        "Relax, I was just testing you like you did me earlier.--I'm [playername]":
            "[playername] felt a bit bad for breaking the illusion of “coolness” for this guy. Though he was a bit cringe, he was an entertaining and oddly vibrant breath of fresh air in this otherwise dulled and surreal hellscape."
    "Cringelord shifts his gaze upwards..."
    c "Kagami…"
    k "It's not nice to meet you - but I suppose, having a lackey understand the beauty of my power is worthwhile."
    "Kagami gets up from his seat, getting ready to leave before he turns around to face [playername] again."
    k "But just know, that next time, I'll turn you into toad oil if you get on my bad side again."
    "[playername] watches Kagami leave. They felt bewildered but decided to not think about the weird guy anymore and instead focused on the weird dystopian slop on his plate…known as a bhocolate bhip bookie."
    "Bell rings and it's time for him to do an activity!-"
    jump chapter1end

label kagami_optionB:
    "You nervously step backwards, feeling a wall of intimidation blocking your path forward."
    u "As you should, hmph. Glad someone around here understands the wonders of my powers. The name's Kagami - come, you are permitted to enter my domain."
    menu:
        "I'm uh, [playername].":
            "[playername] sits a bit further away from the intimidating man, placing their slop of food on the table as [playername] eyes the villain."
    k "Bhocolate Bhip Bookies, huh? I'm more of a Bhicken Bugget person—though, your taste in meals are as good as your taste in seating partners." 
    menu:
        "Seating partners?":
            k "Aha, is that not what we are?"
    "Kagami lets out a thunderous roar of laughter."
    k "My dear lackey, you have chosen wisely. I have been in this domain expansion before…"
    k "You see, I was a murderer - reformed and then..unformed…I murdered again and here we are."
    k "Choosing a person to sit with for a meal- an expert of this prison, in fact…why, you may have just saved yourself from being killed."
    "Kagami gives [playername] a smug grin, nudging his shoulder at them before he takes a bite of his bhicken bugget."
    menu:
        "Is this place really that dangerous?":
            k "Not as dangerous as myself - buuut, I guess you could say it comes in at a close third place. Second has to go to Mickey McGuzzler."
    "You reflect over your interactions with Mickey Mouse, his threatening and booming voice sent shivers down your spine."
    "Though, this Kagami guy was nothing in comparison…he felt more like a gentle gust of wind that sent a piece of dirt in your eye, if anything."
    menu:
        "Ah…I see.":
            "You finish the last of your Bhocolate Bhip Bookies before Kagami continues his monologue of being the most powerful prisoner."
    "[playername] waves at Kagami as he is mid monologue and darts away."
    jump chapter1end

label chapter1_oswald:
    "You approach the grim bulky figure sitting at the far table."
    show oswald with dissolve
    "He doesn't appear to eating anything, just holding in coughs and gasp from repeatedly taking hits from his comically large pipe."
    "You're about to sit down but pause when he glares at you."
    o "You want something boy?"
    menu:
        "Can I try your pipe?":
            o "shove it up yer ass."
            "The fact that he doesn't offer you the pipe leads you to believe he isn't offering to insert the pipe into your rear."
        "Can I sit next to you?":
            o "Guess kid."
        "Can I eat that? It looks like you haven't touched it…":
            o "Keep talking like that boy they only think y'll be eatin is the heel of my Size 35 Meher Kakalia Queen Bauhaus Point - Shiny Black Boots."
            "You look down at his feet but you can't really tell what he's wearing, they're just black blobs"
    "You stay silent."
    o "That's what I thought punk."
    o "Scram if ya know what's good for ya."
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
    "You scram."
    "..."
    "Lame."
    jump chapter1end

label chapter1_oswald_optionB:
    o "AW! What the devil! You tryna start something kid!"
    "He puts his paws up like John L. Sullivan and starts rhythmically circling them while slowly bobbing his whole body up and down."
    show warden at left with dissolve
    m "Say fellas, do we have a problem here?"
    "Oswald jumps as Willie clasps his shoulder from behind."
    "Willie is grinning, lips stretched ear to ear, and his emotionless pitch black eyes fix robotically onto Oswald."
    o "N-non-nothin boss I was just-"
    m "hoHO! Of course not! You wouldn’t want to get into any more trouble with me."
    m "Would you Oz?"
    o "N-no Mister Steamboat Warden Willie- sir."
    "Willie leaves"
    o "*whispers* You lucky the rat is watching."
    "Before you can do anything else he walks over to the corner of the cafeteria to inhale more smoke."
    "He inhales too much and starts gagging."
    "You might want to consider this one a lost cause."
    jump chapter1end

label chapter1_oswald_optionC:
    "As you come within inches of his face he blushes for a moment before lurching back"
    o "Aw! What the devil! You tryna start something kid!"
    "He puts his paws up like a boxer from the 20s and starts rhythmically circling them while slowly bobbing his whole body up and down."
    show warden at left with dissolve
    m "Say fellas, do we have a problem here?"
    "Oswald jumps as Willie clasps his shoulder from behind."
    "Willie is grinning, lips stretched ear to ear, and his emotionless pitch black eyes fix robotically onto Oswald."
    o "N-non-nothin boss I was just-"
    m "hoHO! Of course not! You wouldn't want to get into any more trouble with me."
    m "Would you Oz?"
    o "N-no Mister Steamboat Warden Willie- sir."
    "Willie pats him on the head and leaves"
    o "*whispers* You lucky the rat is watching."
    "Before you can do anything else he walks over to the corner of the cafeteria to inhale more smoke."
    "He inhales too much and starts gagging."
    "You might want to consider this one a lost cause."
    jump chapter1end

label chapter1_oswald_optionD:
    "He glares at you. Again. It looks like he's trying to be more intimidating than before… but it sort of just looks like he's constipated."
    "Before you can do anything else he walks over to the corner of the cafeteria to inhale more smoke."
    "He inhales too much and starts gagging."
    "You might want to consider this one a lost cause."
    jump chapter1end

label chapter1_queen:
    "You walk up to the beautiful spidery woman, she is stabbing her food with her long legs and eating off of them."
    menu queen_questions1:
        "What are you in here for?":
            q "I tried making everyone beautiful with 8 arms, like me."
            q "The whole world was nearly full of my little slave children. If not for that tiny prince's luck, they all would've been mine!"
            $ queenchoice1 = True
            jump queen_questions1
        "What's your name?":
            q "Hmm so you're a new little maggot in this prison, bold enough to ask my name?"
            q "I am Mother Arachnificent, you should know me."
            $ queenchoice2 = True
            jump queen_questions1
        "You're a mother?" if queenchoice1 and queenchoice2 == True:
            q "I have 5000 adorable little spider children. They are always hungry."
            jump queen_questions1
        "Tiny prince?" if queenchoice1 and queenchoice2 == True:
            q "You're a nosy lost soul aren't you?"
            jump queen_questions1
        "Stop asking questions":
            jump chapter1_queen_questions2

label chapter1_queen_questions2:
    q "Little maggot, what villainous thing could you possibly be in here for?"
    menu queen_questions2:
        "I'm innocent!":
            q "Ahahahah you unfortunate fool. You're fresh bait in this world! evil laugh"
        "I'm actually mass murderer":
            q "And a terrible liar. annoyed"
        "I was too hot and seggsy":
            q "Your form is hideous, that cannot possibly be true. *annoyed*"
    q "Well, goodbye little maggot, I cannot wait to see how you get torn apart in here."
    jump chapter1end

label chapter1end:
    scene prison with dissolve
    show warden with dissolve
    m "You aren't getting too friendly with the other's, right? Don't want to have any escapees on my watch! Ha. Ha."
    m "*Neutral looking to the side* I'm joking. Anyways! Back to your regularly scheduled programming!"
    jump chapter2


