#next is the gangster soprano guy

label chapter3:
    scene black with dissolve
    show warden with dissolve
    m "It’s time to wake up! Another day, another chance to have fun!"
    m "Let’s get going before I lose my temper, you wouldn’t want me to lose my temper would you? Hah! Just kidding!"
    jump chapter3_laundry

label chapter3_laundry:
    "You and Oz have been sorting piles of laundry in silence for the past 20 minutes. All the clothing is just exact copies of what you saw your fellow inmates wearing, so it’s pretty easy to sort."
    "Even easier than that because Oz wouldn’t let you touch any of the clothes before he sorted all of his out."
    menu:
        "So hows the…":
            o "..."
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
    menu:
        "Why do you wear a muscle tee.":
            o "Tsk Why da ya think kid?"
    o "Have you seen the folks here? Freaks! Bafoons!"
    o "That one kid wit da spiky hair, he’s got some screws loose for sure! I can’t even understand what he’s sayin half the time."
    o "And dat one dame wit all da legs! Honestly, what she need them all for, and the way her ‘kids’ look at me."
    "Oz shudders"
    "Never heard of a spida eatin a rabbit but naaah. I don’t like it one bit."
    "Ya gotta look tough ta live around here kid… That’s why you can’t tell anyone."
    menu:
        "Do you and the warden know eachother?":
            o "Ya don’t know?"
            o "What baloney are they teachin you kids nowadays?"
    
    #CG HERE
    scene black with dissolve
    show oswald with dissolve
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
            jump chapter3_laundry5
        "...":
            jump chapter3_laundry5

label chapter3_laundry5:
    o "I said too much…"
    "O turns back to sort laundry"
    o "Hope you’re happy kid, cuz I’m not talking anymore."
    jump chapter3_books

label chapter3_books:
    scene black with dissolve
    show warden with dissolve
    m "Alright you filthy rats! It's time for ur next activity!"
    m "You need to clean up the mess in this library!"
    hide warden with dissolve
    show oswald with dissolve
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

    jump chapter4