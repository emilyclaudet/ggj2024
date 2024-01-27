label chapter1:
    scene prison with dissolve
    m "Alrighty, folks! Make your way to the mess hall! Can't work on an empty stomach!"
    show warden with dissolve
    m "Hey there! You look lost! We have loads of new… Erm- friends you can make! Just look over there!"
    m "Don't they look nice? Why don't you go and talk to them?"
    hide warden with dissolve
    menu: 
        "sit next to gangster dude":
            jump chapter1_oswald
        "sit next to spider lady":
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
        "Ah…that's so lame - I'll just call you cringelord then."
    c "W-WHAT-matte matte!!-- Ah heck, I mean WAIT."
    c "Ahem…I'll allow you to hear my name just once. You've proven yourself to be a powerful foe."
    menu: 
        "I don't know if I really want to know anymore, Cringelord just…oh, I don't know…just rolls off the tongue whenever I conceptualize you."
    c "shocked face...."
    "Defeated, Cringelord hangs his head."
    menu:
        "Relax, I was just testing you like you did me earlier.--I'm [playername]"
    "[playername] felt a bit bad for breaking the illusion of “coolness” for this guy. Though he was a bit cringe, he was an entertaining and oddly vibrant breath of fresh air in this otherwise dulled and surreal hellscape."
    "Cringelord shifts his gaze upwards..."
    c "Kagami…"
    k "It's not nice to meet you - but I suppose, having a lackey understand the beauty of my power is worthwhile."
    "Kagami gets up from his seat, getting ready to leave before he turns around to face [playername] again."
    k "But just know, that next time, I'll turn you into toad oil if you get on my bad side again."
    "[playername] watches Kagami leave. They felt bewildered but decided to not think about the weird guy anymore and instead focused on the weird dystopian slop on his plate…known as a bhocolate bhip bookie."
    "Bell rings and it's time for him to do an activity!-"
    jump chapter1next

label kagami_optionB:
    "You nervously step backwards, feeling a wall of intimidation blocking your path forward."
    u "As you should, hmph. Glad someone around here understands the wonders of my powers. The name's Kagami - come, you are permitted to enter my domain."
    menu:
        "I'm uh, [playername]."
    "[playername] sits a bit further away from the intimidating man, placing their slop of food on the table as [playername] eyes the villain."
    k "Bhocolate Bhip Bookies, huh? I’m more of a Bhicken Bugget person—though, your taste in meals are as good as your taste in seating partners." 
    menu:
        "Seating partners?":
            k "Aha, is that not what we are?"
    "Kagami lets out a thunderous roar of laughter."
    k "My dear lackey, you have chosen wisely. I have been in this domain expansion before…"
    k "You see, I was a murderer–reformed and then..unformed…I murdered again and here we are."
    k "Choosing a person to sit with for a meal–an expert of this prison, in fact…why, you may have just saved yourself from being killed."
    "Kagami gives [playername] a smug grin, nudging his shoulder at them before he takes a bite of his bhicken bugget."
    menu:
        "Is this place really that dangerous?":
            k "Not as dangerous as myself–buuut, I guess you could say it comes in at a close third place. Second has to go to Mickey McGuzzler."
    "You reflect over your interactions with Mickey Mouse, his threatening and booming voice sent shivers down your spine."
    "Though, this Kagami guy was nothing in comparison…he felt more like a gentle gust of wind that sent a piece of dirt in your eye, if anything."
    menu:
        "Ah…I see.":
            "You finish the last of your Bhocolate Bhip Bookies before Kagami continues his monologue of being the most powerful prisoner."
    "[playername] waves at Kagami as he is mid monologue and darts away."
    jump chapter1next

label chapter1next:
    show warden with dissolve
    m "You aren't getting too friendly with the other's, right? Don't want to have any escapees on my watch! Ha. Ha."
    m "*Neutral looking to the side* I'm joking. Anyways! Back to your regularly scheduled programming!"
    jump end

label end:
    return


