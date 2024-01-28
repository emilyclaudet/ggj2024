label chapter4:
    scene prison with dissolve
    play sound bell
    show warden happytalk with dissolve
    m "Good morning!"
    show warden neutraltalk with dissolve
    m "Be honest with me [playername], how would you rate my performance out of five stars?"
    show warden with dissolve
    menu:
        "What? Literally zero stars! You’re the worst.":
            show warden neutraltalk with dissolve
            m "I see."
        "Uh… three?":
            show warden happytalkleft with dissolve
            m "An average score coming from an average villain."
        "Five.":
            show warden bashful with dissolve
            m "Didn’t I tell you flattery will get you nowhere? ... Was that in this reality?"
    show warden excited with dissolve
    m "Well - Enough dilly dallying and get to where you’re going!"
    jump chapter4_bracelet1

#friendship bracelets scene
label chapter4_bracelet1:
    scene courtyard with dissolve
    show kagami surprised with dissolve
    k "Okay–what the flip? [playername]! Do you also enjoy the wondrous and delightful taste sensation of friendship bracelet recreations?"
    show kagami talking1 with dissolve
    k "This is so sugoi, my heart’s about to doki-doki into another dimension."
    n "You give Kagami a quirked brow, contorting their face in confusion."
    p "...delightful taste sensation?"
    show kagami with dissolve
    k "Did I stutter?"
    p "No..but.."
    n "You grimace at the thought of crunching on beads–though, oddly enough they do seem…tempting to give a little cronch..."
    show kagami happy with dissolve
    n "You sit next to Kagami as he hands you a plastic baggie filled with various crunch-able beads and slurpable string."
    n "Kagami looks at you and gives a cheeky grin before you both work on your bracelets..."
    hide kagami with dissolve
    show activity1 with dissolve
    n "You make a scrumdiddlyum bracelet!--Wait, DON’T ACTUALLY EAT IT!!"
    jump chapter4_bracelet2

label chapter4_bracelet2:
    scene canteen with dissolve
    n "It's time for another bracelet making session..."
    show kagami happy with dissolve
    k "Are…you…ready…TO RUUUUUUUUMBLE!!!!!"
    p "Frick yeah I am–hand over those beads Kagami and let’s get to it."
    show kagami with dissolve
    k "Erm..actually, these are decorative orbs–not just beads."
    n "You shake your head with a quiet chuckle."
    p "Ah, right right…I knew that, just testing your orb knowledge is all."
    show kagami happy with dissolve
    n "Kagami grins and tosses a few “decorative orbs” and string at you."
    k "Then I'll be sure to not hold back on my bracelet creations– I'm going all out!"
    n "You and Kagami fling around orbs and strings in a flurry of excitement."
    hide kagami with dissolve
    show activity2 with dissolve
    n "(You make a quirky and fun bracelet!)"
    jump chapter4_bracelet3

label chapter4_bracelet3:
    scene prison with dissolve
    n "Another bracelet making session..."
    show kagami annoyed with dissolve
    k "Everything is not daijoubou, [playername]."
    k "I dropped all of my decorative orbs and we have ten minutes before Willy shows up and tells us to get back in the cage."
    p "But what about our emotionally charged and driven strings of life that brought us to this moment?!"
    n "Kagami looks at you with a furrowed brow before looking at you, stunned."
    show kagami happy with dissolve
    k "YOU’RE RIGHT! I can’t let a few orbs hold me down, I have the bracelet of friendship that I made before you came here!"
    p "Eh–wait you already made a bracelet–"
    k "These strings hold more power than just these measly beads–I mean, decorative orbs." 
    k "AHEM, these strings are the webs of friendship; if a bracelet dares to break, it would cause the world to combust in seconds."
    k "Uh...in other universes, I mean.”  “YES–The world of Eorzea is done for, shattered to PIECES. You could even say, that was truly their…Final Fantasy."
    scene kagami_bracelet with dissolve
    n "(You make a destructive and world-ending bracelet!)"
    jump ending_choice

