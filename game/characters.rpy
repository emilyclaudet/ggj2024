# Declare characters used by this game. The color argument colorizes the
# name of the character.

define m = Character("Steamboat Warden", color="#c7cfcb")
define k = Character("Kagami", color="#C49C0F")
define c = Character("Cringe Lord", color="#C49C0F")
define o = Character("Osbald", color="#037cb5")
define q = Character("Queen Arachnificent", color="#af56db")
define p = Character("[playername]", color="#20e04d")
define u = Character("???", color="#FFFFFF")
define oz = Character("Oz", color="#037cb5")
define n = Character(None, what_italic=True)

#Kagami
image kagami neutral = "kagami_neutral"
image kagami blink = "kagami_neutralblink"
image kagami smile = "kagami_smile"
image kagami smileblink = "kagami_smileblink"
image kagami smirk = "kagami_smirk"
image kagami smirkblink = "kagami_smirkblink"

#Kagami animations
image kagami:
    "kagami neutral"
    3
    "kagami blink"
    0.2
    repeat

image kagami happy:
    "kagami smile"
    3
    "kagami smileblink"
    0.2
    repeat

image kagami annoyed:
    "kagami smirk"
    3
    "kagami smirkblink"
    0.2
    repeat


#Osbald
image osbald = "oswald_n_neutral"
image osbald badsurprisedred = "oswald_n_badsuprisedred"
image osbald badsurprised = "oswald_n_badsuprised"
image osbald distantsad = "oswald_n_distantsad"
image osbald evilgrin = "oswald_n_evilgrin"
image osbald upset = "oswald_n_upset"
image osbald surprised = "oswald_n_suprised"
image osbald surprisedblushing = "oswald_n_suprisedblushing"
image osbald surprisered = "oswald_n_suprisedred"
image osbaldmuscle = "oswald_m_neutral"
image osbaldmuscle badsurprisedred = "oswald_m_badsuprisedred"
image osbaldmuscle badsurprised = "oswald_m_badsuprised"
image osbaldmuscle distantsad = "oswald_m_distantsad"
image osbaldmuscle evilgrin = "oswald_m_evilgrin"
image osbaldmuscle upset = "oswald_m_upset"
image osbaldmuscle surprised = "oswald_m_suprised"
image osbaldmuscle surprisedblushing = "oswald_m_suprisedblushing"
image osbaldmuscle surprisered = "oswald_m_suprisedred"

#Warden 
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
image queen neutral = "queen_neutral"
image queen blink = "queen_neutral_blink"
image queen happy2 = "queen_happy"
image queen annoyedblink = "queen_annoyed_blink"
image queen annoyed2 = "queen_annoyed"
image queen sad = "queen_sad"
image queen bashfulblink = "queen_bashful_blink"
image queen bashful2 = "queen_bashful"
image queen flirtyblink = "queen_flirty_blink"
image queen flirty = "queen_flirty"

#queen animations
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
