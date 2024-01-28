#next is the gangster soprano guy

label chapter3:
    scene black with dissolve
    show warden with dissolve
    m "It’s time to wake up! Another day, another chance to have fun!"
    m "Let’s get going before I lose my temper, you wouldn’t want me to lose my temper would you? Hah! Just kidding!"
    hide warden with dissolve
    jump chapter3_laundry

label chapter3_laundry:
    "You and Oz have been sorting piles of laundry in silence for the past 20 minutes. All the clothing is just exact copies of what you saw your fellow inmates wearing, so it’s pretty easy to sort."
    "Even easier than that because Oz wouldn’t let you touch any of the clothes before he sorted all of his out."
    show osbald with dissolve
    menu:
        "So hows the…":
            o "..."
        "...":
            jump chapter3_laundry2            
    menu:
        "Weather?":
            o "..."
            p "..."
            o "..."
        "Kids?":
            o "..."
            p "..."
            o "..."
    jump chapter3_laundry2

label chapter3_laundry2:
    "You notice an unusual item underneath the mounds of silk purple dresses and oversized belts."
    "You drag it out from the bottom of the pile and hold it up to get a good look."
    "It’s. A black muscle suit?"
    "That looks exactly like Os muscles..."
    menu:
        "...":
            jump chapter3_laundry3
        "You wear a muscle suit?":
            jump chapter3_laundry3

label chapter3_laundry3:
    "Oz looks up and his eyes widen in terror, his face turns red as a tomato."
    o "HEY!!!"
    "Oz snatches the costume out of your hands and frantically looks for a place to hide it."
    "He clumsy waddles to the far end of the room and stuffs the suit behind the furthest laundry machine and turns back to you."
    o "YOU DIDN’T SEE NOTHIN KID!"

    menu:
        "Maybe… will you talk to me?":
            jump chapter3_laundry4
        "Pretty sure I did.":
            jump chapter3_laundry4

label chapter3_laundry4:
    o "Why you little..."
    "Oz waddles back up to you."
    o "C’mon! whadda I gotta do ta’ get you to not blab?"
    menu chapter3_laundry4_menu:
        "Why do you wear a muscle tee.":
            o "Tsk Why da ya think kid?"
            o "Have you seen the folks here? Freaks! Bafoons!"
            o "That one kid wit da spiky hair, he’s got some screws loose for sure! I can’t even understand what he’s sayin half the time."
            o "And dat one dame wit all da legs! Honestly, what she need them all for, and the way her ‘kids’ look at me."
            "Oz shudders"
            "Never heard of a spida eatin a rabbit but naaah. I don’t like it one bit."
            "Ya gotta look tough ta live around here kid… That’s why you can’t tell anyone."
            jump chapter3_laundry4_menu
        "Do you and the warden know eachother?":
            o "Ya don’t know?"
            o "What baloney are they teachin you kids nowadays?"    

    #CG HERE
    scene black with dissolve
    show osbald with dissolve
    o "All ya need to know is that once I had everything."
    o "And that rat took it all from me."
    o "I WAS FIRST! YA HEAR?"
    "You nodd along"
    o "DAT BASTARD. I HAD DA WORLD IN MY PAWS AND HE TOOK IT ALL AWAY!"
    o "NOW LOOK AT ME!"

    #CG STOPS
    o "I’M NOTHIN! I’m in a costume, a disguise!"
    o "I’m hidin!"
    o "But-"
    o "But I guess it’s not like I need to… Even a nobody like yous knows who I am."
    o "Who I was…"
    "O looks down at his Size 35 Meher Kakalia Queen Bauhaus Point - "
    "Shiny Black Boots, hands crossed infront of his foam chest. He suddenly stands much smaller, deflated."
    menu:
        "You reach out to hug him.":
            "O pulls away before you can touch him."
            jump chapter3_laundry5
        "...":
            jump chapter3_laundry5

label chapter3_laundry5:
    o "I said too much…"
    "O turns back to sort laundry"
    o "Hope you’re happy kid, cuz I’m not talking anymore."
    jump chapter3_books

#books chapter
label chapter3_books:
    scene black with dissolve
    show warden with dissolve
    m "Alright you filthy rats! It's time for ur next activity!"
    m "You need to clean up the mess in this library!"
    hide warden with dissolve
    show osbald with dissolve
    o "Can ya believe this? Every book in this library is about him. Whadda narcissist."
    "You also realize that the title of every book you’ve sorted is credited to the warden."
    "You can O continue to sort the books onto the infinitely stretching line of “M” shelves."
    menu:
        "Why don’t you take off the Muscle suit?":
            "O opens his mouth, ready to send another bitter rant your way, before pausing…"
    o "Yer right. I can’t hide myself from you anymore."
    # update oswald asset
    "O goes behind the shelf and comes back without the muscle suit. He suddenly looks much more familiar to you."
    o "It’s easier to move like this."
    menu:
        "You’re Osbald the Lucky Rodent!":
            "You see Os mouth drop and his eyes filled with shock and awe for just a moment before returning back to his normal grimmace."
    o "So they do teach you kids something…"
    "You run eventually run out of room on the shelves close enough to the door that you feel comfortable going to. O brings out a ladder to reach the higher shelves"
    "You volunteer to be the one at the top of the ladder, O holds it at the bottom to keep you steady."
    o "So you know who I am."
    o "I’m… flattered."
    o "But… you know too much."
    o "I’m gonna hafta bum ya off."
    #Author Note: “Bump Off” was 20s slang for murder/kill
    "You feel the ladder shake and wobble under your feet."
    menu:
        "Wait wait wait! I- uh I love you Osbald."
        "No Wait! Osbald when I was a kid you were my favorite!":
            jump chapter3_books2

label chapter3_books2:
    "Despite your pleas and attempt to hang, you feel yourself slip and fall. You squeeze your eyes shut and wait for your head to hit the hard Willie the Warden themed floor."
    "But you don’t"
    "Instead you feel two very soft hands."
    "You open your eyes..."
    #CG START
    o "You mean it?"
    #CG END
    menu:
        "Yes I- uh- you’re very attractive and um... kind!":
            "O blushes but this time he doesn’t look away."
            o "Really?"
        "Whenever I got to watch cartoons as a kid. I always wanted to watch you!":
            "O blushes but this time he doesn’t look away."
            o "Really?"
    menu:
        "Really! We should totally get revenge on that rat. Together!":
            o "Gahahahaha!"
            o "Yer right kid, I ain’t the only whose got beef with em! We’re gonna get everyone in this prison ta bump him off."
        "Really! We should get outta here together! I’ll help you spread the word that Osbald is back!":
            "O widens his grin."
            o "I like what you’re spinnin kid! I’m gonna crush that rat! I’ll be back to my former glory!"
            o "And you’re gonna help me do it. Kid."
    menu:
        "Lean in for a kiss":
            o "Woah there! Uh, I ain’t into that stuff kid."
            p "Oh. Sorry…"
            o "Besides I gotta be at least 3 times your age."
            "O places you down on your feet."
            "You two have had enough of sorting books."
        "Ask to be put down":
            o "Yeah! Yeah…"
            "O places you down on your feet."
            "You two have had enough of sorting books"
    jump chapter4
