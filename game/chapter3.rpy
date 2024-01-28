#next is the gangster soprano guy

label chapter3:
    scene prison with dissolve
    show warden with dissolve
    m "It's time to wake up! Another day, another chance to have fun!"
    m "Let's get going before I lose my temper, you wouldn't want me to lose my temper would you? Hah! Just kidding!"
    hide warden with dissolve
    jump chapter3_laundry

label chapter3_laundry:
    scene laundryroom with dissolve
    n "You and Oz have been sorting piles of laundry in silence for the past 20 minutes. All the clothing is just exact copies of what you saw your fellow inmates wearing, so it's pretty easy to sort."
    n "Even easier than that because Oz wouldn't let you touch any of the clothes before he sorted all of his out."
    show osbald with dissolve
    menu:
        "So hows the…":
            oz "..."
        "...":
            jump chapter3_laundry2            
    menu:
        "Weather?":
            oz "..."
            p "..."
            oz "..."
        "Kids?":
            oz "..."
            p "..."
            oz "..."
    jump chapter3_laundry2

label chapter3_laundry2:
    n "You notice an unusual item underneath the mounds of silk purple dresses and oversized belts."
    n "You drag it out from the bottom of the pile and hold it up to get a good look."
    n "It's. A black muscle suit?"
    n "That looks exactly like Oz's muscles..."
    menu:
        "... Oz?":
            jump chapter3_laundry3
        "You wear a muscle suit?":
            jump chapter3_laundry3

label chapter3_laundry3:
    show osbald surprisedred with dissolve
    n "Oz looks up and his eyes widen in terror, his face turns red as a tomato."
    oz "HEY!!!"
    n "Oz snatches the costume out of your hands and frantically looks for a place to hide it."
    n "He clumsy waddles to the far end of the room and stuffs the suit behind the furthest laundry machine and turns back to you."
    show osbald badsurprisedred with dissolve
    oz "YOU DIDN'T SEE NOTHIN KID!"

    menu:
        "Maybe… will you talk to me?":
            jump chapter3_laundry4
        "Pretty sure I did.":
            jump chapter3_laundry4

label chapter3_laundry4:
    show osbald badsurprised with dissolve
    oz "Why you little..."
    n "Oz waddles back up to you."
    oz "C'mon! whadda I gotta do ta' get you to not blab?"
    menu chapter3_laundry4_menu:
        "Why do you wear a muscle tee.":
            show osbald with dissolve
            oz "Tsk Why da ya think kid?"
            show osbald distantsad with dissolve
            oz "Have you seen the folks here? Freaks! Bafoons!"
            oz "That one kid wit da spiky hair, he's got some screws loose for sure! I can't even understand what he's sayin half the time."
            show osbald badsurprised with dissolve
            oz "And dat one dame wit all da legs! Honestly, what she need them all for, and the way her 'kids' look at me."
            n "Oz shudders"
            oz "Never heard of a spida eatin a rabbit but naaah. I don't like it one bit."
            oz "Ya gotta look tough ta live around here kid… That's why you can't tell anyone."
            jump chapter3_laundry4_menu
        "Do you and the warden know eachother?":
            show osbald distantsad with dissolve
            oz "Ya don't know?"
            show osbald badsurprised with dissolve
            oz "What baloney are they teachin you kids nowadays?"    

    #CG HERE
    show osbald distantsad with dissolve
    oz "All ya need to know is that once I had everything."
    show osbald upset with dissolve
    oz "And that rat took it all from me."
    show osbald badsurprised with dissolve
    oz "I WAS FIRST! YA HEAR?"
    n "You nodd along..."
    show osbald badsurprisedred with dissolve
    oz "DAT BASTARD. I HAD DA WORLD IN MY PAWS AND HE TOOK IT ALL AWAY!"
    oz "NOW LOOK AT ME!"

    #CG STOPS
    oz "I’M NOTHIN! I’m in a costume, a disguise!"
    oz "I’m hidin!"
    show osbald with dissolve
    oz "But-"
    oz "But I guess it’s not like I need to… Even a nobody like yous knows who I am."
    show osbald distantsad with dissolve
    oz "Who I was…"
    n "Oz looks down at his Size 35 Meher Kakalia Queen Bauhaus Point - Shiny Black Boots, hands crossed infront of his foam chest."
    n "He suddenly stands much smaller, deflated."
    menu:
        "You reach out to hug him.":
            "Oz pulls away before you can touch him."
            jump chapter3_laundry5
        "...":
            jump chapter3_laundry5

label chapter3_laundry5:
    oz "I said too much…"
    n "Oz turns back to sort laundry"
    oz "Hope you’re happy kid, cuz I’m not blabbin anymore."
    jump chapter3_books

#books chapter
label chapter3_books:
    scene black with dissolve
    show warden with dissolve
    m "Alright you filthy rats! It's time for ur next activity!"
    m "You need to clean up the mess in this library!"
    hide warden with dissolve
    show osbald with dissolve
    oz "Can ya believe this? Every book in this library is about him. Whadda narcissist."
    n "You also realize that the title of every book you’ve sorted is credited to the warden."
    n "You and Oz continue to sort the books onto the infinitely stretching line of “M” shelves."
    menu:
        "Why don’t you take off the Muscle suit?":
            "Oz opens his mouth, ready to send another bitter rant your way, before pausing…"
    oz "Yer right. I can’t hide myself from you anymore."
    # update oswald asset
    n "Oz goes behind the shelf and comes back without the muscle suit. He suddenly looks much more familiar to you."
    oz "It’s easier to move like this."
    menu:
        "You’re Osbald the Fortunate Rodent!":
            "You see Osbald's mouth drop and his eyes filled with shock and awe for just a moment before returning back to his normal grimmace."
    o "So they do teach you kids something…"
    n "You run eventually run out of room on the shelves close enough to the door that you feel comfortable going to. Osbald brings out a ladder to reach the higher shelves"
    n "You volunteer to be the one at the top of the ladder, Osbald holds it at the bottom to keep you steady."
    o "So you know who I am."
    o "I’m… flattered."
    o "But… you know too much."
    o "I’m gonna hafta bum ya off."
    #Author Note: “Bump Off” was 20s slang for murder/kill
    n "You feel the ladder shake and wobble under your feet."
    menu:
        "Wait wait wait! I- uh I love you Osbald.":
            jump chapter3_books2
        "No Wait! Osbald when I was a kid you were my favorite!":
            jump chapter3_books2

label chapter3_books2:
    n "Despite your pleas and attempt to hang, you feel yourself slip and fall. You squeeze your eyes shut and wait for your head to break on the hard 'Willie the Warden' themed floor tiling."
    n "But you don’t"
    n "Instead you feel two very soft paws cradling you."
    n "You open your eyes..."
    #CG START
    o "You mean it?"
    #CG END
    menu:
        "Yes I- uh- you’re very attractive and um... kind!":
            n "Osbald blushes but this time he doesn’t look away."
            o "Really?"
        "Whenever I got to watch cartoons as a kid. I always wanted to watch you!":
            n "Osbald blushes but this time he doesn’t look away."
            o "Really?"
    menu:
        "Really! We should totally get revenge on that rat. Together!":
            o "Gahahahaha!"
            o "Yer right kid, I ain’t the only whose got beef with em! We’re gonna get everyone in this prison ta bump him off."
        "Really! We should get outta here together! I’ll help you spread the word that Osbald is back!":
            "Osbald widens his grin."
            o "I like what you’re spinnin kid! I’m gonna crush that rat! I’ll be back to my former glory!"
            o "And you’re gonna help me do it. Kid."
    menu:
        "Lean in for a kiss":
            o "Woah there! Uh, I ain’t into that stuff kid."
            p "Oh. Sorry…"
            o "Besides I gotta be at least 3 times your age."
            n "Osbald places you down on your feet."
            n "You two have had enough of sorting books."
        "Ask to be put down":
            o "Yeah! Yeah…"
            n "Osbald places you down on your feet."
            n "You two have had enough of sorting books"
    jump chapter4
