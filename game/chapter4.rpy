label chapter4:
    scene black with dissolve
    show warden with dissolve
    m "Good morning!"
    #[Fades to Neutral looking away before flipping back to looking at the player] 
    m "Be honest with me [playername], how would you rate my performance out of five stars?"
    menu:
        "What? Literally zero stars! You’re the worst.":
            #neutral
            m "I see."
        "Uh… three?":
            m "An average score coming from an average villain."
        "Five.":
            #Bashful, fades back to neutral looking away, fades to neutral looking at player] 
            m "Didn’t I tell you flattery will get you nowhere? ... Was that in this reality?"
    m "Well - Enough dilly dallying and get to where you’re going!"

#friendship bracelets scene
label chapter4_bracelet1:
    scene black with dissolve
    show kagami with dissolve
    k "Okay–what the flip? [playername]! Do you also enjoy the wondrous and delightful taste sensation of friendship bracelet recreations?"
    k "This is so sugoi, my heart’s about to doki-doki into another dimension."
    "[playername] gives Kagami a quirked brow, contorting their face in confusion."
    p "...delightful taste sensation?"
    k "Did I stutter?"
    p "No..but.."
    "[playername] grimaces at the thought of crunching on beads–though, oddly enough they do seem…tempting to give a little cronch..."
    "You sit next to Kagami as he hands you a plastic baggie filled with various crunch-able beads and slurpable string."
    "Kagami looks at you and gives a cheeky grin before you both work on your bracelets..."
    #a cooking timer sound effect and then the image of the friendship bracelets are shown
    "You make a scrumdiddlyum bracelet!--Wait, DON’T ACTUALLY EAT IT!!"
    jump chapter4_bracelet2

label chapter4_bracelet2:
    k "Are…you…ready…TO RUUUUUUUUMBLE!!!!!"
    p "Frick yeah I am–hand over those beads Kagami and let’s get to it."
    k "Erm..actually, these are decorative orbs–not just beads."
    "[playername] shakes their head with a quiet chuckle."
    p "Ah, right right…I knew that, just testing your orb knowledge is all."
    "Kagami grins and tosses a few “decorative orbs” and string at [playername]."
    k "Then I’ll be sure to not hold back on my bracelet creations–I’m going all out!"
    "[playername] and Kagami fling around orbs and strings in a flurry of excitement."
    #a cooking timer sound effect and then the image of the friendship bracelets are shown
    "(You make a quirky and fun bracelet!)"
    jump chapter4_bracelet3

label chapter4_bracelet3:
    k "Everything is not daijoubou, [playername]."
    k "I dropped all of my decorative orbs and we have ten minutes before Mickey McDickey shows up and tells us to get back in the cage."
    p "But what about our emotionally charged and driven strings of life that brought us to this moment?!"
    "Kagami looks at you with a furrowed brow before looking at [playername], stunned."
    k "YOU’RE RIGHT! I can’t let a few orbs hold me down, I have the bracelet of friendship that I made before you came here!"
    p "Eh–wait you already made a bracelet–"
    k "These strings hold more power than just these measly beads–I mean, decorative orbs." 
    k "AHEM, these strings are the webs of friendship; if a bracelet dares to break, it would cause the world to combust in seconds."
    #his bracelet breaks
    k "Uh...in other universes, I mean.”  “YES–The world of Eorzea is done for, shattered to PIECES. You could even say, that was truly their…Final Fantasy."
    #a cooking timer sound effect and then the image of the friendship bracelets are shown
    "(You make a destructive and world-ending bracelet!)"
    jump ending_choice

