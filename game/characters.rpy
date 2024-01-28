# Declare characters used by this game. The color argument colorizes the
# name of the character.

define m = Character("Steamboat Warden", color="#c7cfcb")
define k = Character("Kagami", color="#C49C0F")
define c = Character("Cringe Lord", color="#C49C0F")
define o = Character("Osbald", color="#037cb5")
define q = Character("Queen Arachnificent", color="#af56db")
define p = Character("[playername]", color="#20e04d")
define u = Character("???", color="#FFFFFF")

#Kagami
image kagami = "anime_villain_concept"
image kagami stern = "anime_villain_concept2"
image kagami back = "anime_villain_conceptback"

#Soprano
image osbald = "sopranoconcept"

#Steamboat
image warden = "neutral_warden_closedmouth_forward"
image warden neutralleft  = "neutral_warden_closedmouth_left"
image warden neutralright  = "neutral_warden_closedmouth_right"
image warden neutraltalk = "neutral_warden_openmouth_forward"
image warden neutraltalkleft = "neutral_warden_openmouth_left"
image warden neutraltalkright = "neutral_warden_openmouth_right"
image warden happy = "happy_warden_closedmouth_forward"
image warden happyleft = "happy_warden_closedmouth_left"
image warden happyright = "happy_warden_closedmouth_right"
image warden happytalkright = "happy_warden_openmouth_forward"
image warden happytalkright = "happy_warden_openmouth_left"
image warden happytalkright = "happy_warden_openmouth_right"
image warden angry = "angry_warden_closedmouth_forward"
image warden angryleft = "angry_warden_closedmouth_left"
image warden angryright = "angry_warden_closedmouth_right"
image warden angrytalk = "angry_warden_openmouth_forward"
image warden angrytalkleft = "angry_warden_openmouth_left"
image warden angrytalkright = "angry_warden_openmouth_right"
image warden sad = "sad_warden_closedmouth"
image warden sadtalk = "sad_warden_openmouth"
image warden bashful = "bashful_warden"
image warden excited = "excited_warden"

#Femme disney villain
image queen neutral = "1Queen_Neutral"
image queen blink = "1Queen_Neutral_blink"
image queen happy2 = "2Queen_Happy"
image queen annoyedblink "3Queen_Annoyed_blink"
image queen annoyed2 = "3Queen_Annoyed"
image queen sad = "4Queen_Sad"
image queen bashfulblink = "5Queen_Bashful_blink"
image queen bashful2 = "5Queen_Bashful"
image queen flirtyblink = "6Queen_Flirty_blink"
image queen flirty = "6Queen_Flirty"

image queen:
    "queen neutral"
    3
    "queen blink"
    0.2
    repeat

image queen happy:
    "queen happy2"
    3
    "queen blink"
    0.2
    repeat

image queen annoyed:
    "queen annoyed2"
    3
    "queen annoyedblink"
    0.2
    repeat

image queen bashful:
    "queen bashful2"
    3
    "queen bashfulblink"
    0.2
    repeat

image queen flirt:
    "queen flirty"
    3
    "queen flirtyblink"
    0.2
    repeat
