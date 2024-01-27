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
label chapter4_kagami:
    scene black with dissolve
    show kagami with dissolve
    k "Okay–what the flip? [playername]! Do you also enjoy the wondrous and delightful taste sensation of friendship bracelet recreations?"
    k "This is so sugoi, my heart’s about to doki-doki into another dimension."
    "[playername] gives Kagami a quirked brow, contorting their face in confusion."
    p "...delightful taste sensation?"

    jump chapter_4end

label chapter_4end:
    jump end

