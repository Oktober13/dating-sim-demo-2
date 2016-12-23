
init python:
# options 0-73 is True. Once certain options are chosen, they'll be labelled False. Options and dialog will be added or removed based on the flags set. This is the pattern I've followed while auditing this.
    option = []
    for i in range(0,73):
        option.append(True)
    option37_5 = True
    metfriskfirst = True #True if player met toriel before meeting frisk
    torielinviteaccept = True #True if player accepts toriel's invitation

    diary = 0
    cactus = 0

    frisk_fp = 0
    toriel_fp = 0

    determination = 0
    integrity = 0
    patience = 0
    kindness = 0
    perseverance = 0
    bravery = 0
    justice = 0

    stamina = 10

    MAX_SCORE = 100
    minigamescore = MAX_SCORE

label frisk_meeting_menu:
    menu:
        "From the Start":
            jump frisk_meeting_start
        "Questions":
            jump frisk_meeting_questions
        "Snail Catching":
            jump frisk_meeting_snail_catching
        "Snail Catching Results":
            jump frisk_meeting_play_snail_minigame
        "Meeting Late":
            jump frisk_meeting_late
        "Home":
            jump frisk_meeting_home
        "Meal with Toriel and Frisk":
            jump frisk_meeting_eat
        "After Eating":
            jump frisk_meeting_eat_after
        "Post Dinner":
            jump frisk_meeting_after_dinner

label frisk_meeting_start:
    #show Frisk surprised
    xxxfrisk "Oh! Um, hi. I wasn’t expecting to see another human. How... how did you get here?" 
    jump frisk_meeting_selection1
label frisk_meeting_selection1:
    menu:
        "I could ask you the same thing.":
            jump frisk_meeting_choice1
        "I tripped.":
            $ frisk_fp +=3
            jump frisk_meeting_choice2
        "You’re not Toriel’s kid, are you?" if metfriskfirst == False:
            $ frisk_fp -=3
            jump frisk_meeting_choice3
        "Hi, nice to meet you!":
            $ frisk_fp +=4
            jump frisk_meeting_choice4
label frisk_meeting_choice1:
    #show Frisk tiny smile
    xxxfrisk "Oh, well, you know... I guess I was hiking, and I just... sort of..."
    #show Frisk surprised
    xxxfrisk "Oh! I’m sorry, I forgot my manners."
    #show Frisk somewhat happy
    xxxfrisk "I’m Frisk. It’s nice to meet you!"
    frisk "I’m a human, too!"
    frisk "But, um, I guess you could probably see that."
    jump frisk_meeting_selection2

label frisk_meeting_selection2:
    menu:
        "Are there more humans down here?":
            $ frisk_fp +=1
            jump frisk_meeting_choice5
        "And you live with a monster?":
            jump frisk_meeting_choice6

label frisk_meeting_choice5:
    #show Frisk normal
    frisk "Oh, no... not that I know of."
    frisk "You’re actually the first human I’ve seen since I fell down here."
    frisk "I’ve been living here with Mom- I mean, you probably know her as Toriel."
    #show Frisk somewhat happy
    frisk "She’s taken care of me since I was a kid!"
    jump frisk_meeting_questions

label frisk_meeting_choice6:
    #show Frisk normal
    frisk "Yeah. When I came to the Underground, Mom... I mean, Toriel... found me and has been taking care of me ever since."
    jump frisk_meeting_questions

label frisk_meeting_choice2:
    #show Frisk giggly
    xxxfrisk "Ha ha! You're funny.  No one just 'trips' and ends up down here."
    #show Frisk slightly happy
    xxxfrisk "..."
    xxxfrisk "At least, no one that I know."
    #show Frisk somewhat happy
    xxxfrisk "Oh, where are my manners... my name is Frisk!"
    jump frisk_meeting_questions

label frisk_meeting_choice3:
    #show Frisk annoyed
    xxxfrisk "Yes I am!"
    #show Frisk disappointed
    xxxfrisk "Oh, right. You were probably expecting me to be a monster, huh?"
    #show Frisk normal
    xxxfrisk "My name is Frisk."
    frisk "I’m a human. Mom- well, you know her as Toriel..."
    frisk "She’s really nice, and she takes care of me."
    jump frisk_meeting_questions

label frisk_meeting_choice4:
    #show Frisk surprised
    xxxfrisk "Oh! Right, where are my manners... my name is Frisk!"
    #show Frisk tiny smile
    frisk "It’s nice to meet you, too. I, uh... hope you grow to like the Underground."
    frisk "It's pretty great once you get used to it."
    jump frisk_meeting_questions


label frisk_meeting_questions:
    jump frisk_meeting_selection3

label frisk_meeting_selection3:
    menu:
        "You’re actually a human? Not some monster?" if option[6]: 
            #[n/a 1,3]
            jump frisk_meeting_choice6_2
        "I’ve recently met Toriel. She seems nice.":
            $ frisk_fp +=3
            jump frisk_meeting_choice7
        "How’s life here in the Ruins?":
            $ frisk_fp +=3
            jump frisk_meeting_choice8
label frisk_meeting_choice6_2:
    #show Frisk somewhat happy
    frisk "Yeah! I live with my mom- I mean, Toriel, the caretaker of the Ruins. She’s really kind. Have you met her?"
    $ option[6] = False
    jump frisk_meeting_questions
label frisk_meeting_choice7:
    #show Frisk big smile
    frisk "Yeah! Out of all the people that could’ve found me, I’m glad it was her."
    jump frisk_meeting_selection4
label frisk_meeting_selection4:
    menu:
        "Are you saying the other monsters are bad?":
            $ frisk_fp -=1
            jump frisk_meeting_choice10
        "I can relate. She helped me, too.":
            $ frisk_fp +=2
            jump frisk_meeting_choice11
label frisk_meeting_choice10:
    #show Frisk surprised
    frisk "What? No!"
    #show Frisk upset
    frisk "I mean, other monsters are great, too. I shouldn't have said that... it was mean. But she’s the only one who’s really taken care of me, y’know?"
    jump frisk_meeting_snail_catching
label frisk_meeting_choice11:
    #show Frisk tiny smile
    frisk "That’s great! She can handle anything!"
    #show Frisk upset
    frisk "..."
    #show Frisk somewhat happy
    frisk "Well, most things."
    jump frisk_meeting_snail_catching
label frisk_meeting_choice8:
    #show Frisk somewhat happy
    frisk "Well, we don’t have much, but it’s nice. It’s just that sometimes Mom makes food with snails in it, and it’s..."
    #show Frisk upset
    frisk "...not amazing... but don’t worry about it."
    #show Frisk somewhat happy
    frisk "Other than that, things are pretty great."
    jump frisk_meeting_selection5

label frisk_meeting_selection5:
    menu:
        "Are you feeling okay? You look a little under the weather.":
            $ frisk_fp +=3
            jump frisk_meeting_choice12
        "I’m sure everything must be great for you then!":
            jump frisk_meeting_choice13
label frisk_meeting_choice12:
    frisk "Oh, um. I’m... I’m fine."
    frisk "Tiring day, ya know?"
    frisk "But... I appreciate your concern."
    jump frisk_meeting_selection6

label frisk_meeting_selection6:
    menu:
        "Are you sure you’re okay? Do you want to talk about something?":
            $ frisk_fp +=1
            jump frisk_meeting_choice14
        "...":                                
            jump frisk_meeting_choice15


label frisk_meeting_choice14:
    frisk "No, really... it’s fine. I appreciate the help... I really do. But, honestly, it’s nothing."
label frisk_meeting_selection7:
    menu:
        "Oh, come on, tell me!":
            $ frisk_fp -=2
            jump frisk_meeting_choice16
        "Just making sure.":
            $ frisk_fp +=2
            jump frisk_meeting_choice17
label frisk_meeting_choice16:
    #show Frisk annoyed
    frisk "Please, you're making this more than what it is."
    jump frisk_meeting_selection8
label frisk_meeting_selection8:
    menu:
        "You have to tell me!":
            $ frisk_fp -=3
            jump frisk_meeting_choice18
        "Alright, I’m sorry.":
            jump frisk_meeting_choice19
label frisk_meeting_choice18:
    #+1 Determination
    $ determination +=1
    #show Frisk angry
    frisk "No, I don’t have to tell you anything! I’m not talking about this anymore!"
    #show Frisk neutral
    frisk "Sorry, I don’t like people getting on my back about things."
    jump frisk_meeting_snail_catching
label frisk_meeting_choice19:
    #show Frisk annoyed
    frisk "..."
    frisk "...Thank you."
    jump frisk_meeting_snail_catching
label frisk_meeting_choice17:
    frisk "Thanks. You remind me a lot of Mom, actually."
    #show Frisk big smile
    frisk "But... don’t go thinking you can outdo her in the mothering department! She’s the master!"
    jump frisk_meeting_snail_catching
label frisk_meeting_choice15:
    jump frisk_meeting_snail_catching
label frisk_meeting_choice13:
    frisk "Yup... pretty much."
    jump frisk_meeting_snail_catching

label frisk_meeting_snail_catching:
    #show Frisk normal
    frisk "Oh, hey... is that a crack on your phone? It looks pretty banged up."
    #show Frisk tiny smile
    frisk "Here, you can take my old phone! My friend made me a new one, so I don’t mind."
    frisk "And I’ve already transferred all of my old junk off of it, so it’s just like new."
    frisk "Oh, and I’ll add my number into it! That way, if you ever need to get in touch with me, I’ll just be a phone call away!"
    #player has Frisk’s number now
    frisk "So..."
    #show Frisk surprised
    frisk "Oh wait, I almost forgot!"
    #show Frisk somewhat happy
    frisk "I’m actually supposed to be doing something important..."
    frisk "I need your help. It won’t take long, I promise."
    frisk "Just follow me!"

    ##-Transition to Snail Catching Room-
    ##-Transition: Snail Catching Mini-game-

    #show Frisk normal
    frisk "Okay, here we are."
    frisk "I know this is going to sound a bit weird, but I need to catch snails."
    frisk "Mom makes food with them, and she needs a lot!"
    jump frisk_meeting_selection9

label frisk_meeting_selection9:
    menu:
        "You’re right, that is weird.":
            jump frisk_meeting_choice20
        "That sounds completely reasonable.":
            $ frisk_fp +=3
            jump frisk_meeting_choice21
        "Oh yeah, Toriel already told me." if torielinviteaccept:
            $ frisk_fp +=4
            jump frisk_meeting_choice61
            #option 61 only available if the player went to Toriel’s house before meeting Frisk AND at some point accepted her invitation to stay at her house
label frisk_meeting_choice20:
    #-1 Patience
    $patience -=1
    frisk "Well, what can I say?" 
    frisk "But seriously, this is important. I’ll need your help."
    frisk "Catching snails is harder than you’d think."
label frisk_meeting_choice21:
    frisk "Really, you think so?"
    jump frisk_meeting_selection10

label frisk_meeting_selection10:
    menu:
        "Yeah, I do it all the time!":
            $ frisk_fp +=3
            jump frisk_meeting_choice22
        "I lied. That makes no sense whatsoever.":
            $ frisk_fp -=5
            jump frisk_meeting_choice23
label frisk_meeting_choice22:
    #show Frisk big smile
    frisk "That’s great! This’ll be easy!"
    jump frisk_meeting_play_snail_minigame
label frisk_meeting_choice23:
    #-1 Integrity
    $integrity -=1
    #show Frisk upset
    frisk "Oh... okay."
    frisk "Well- please, I really do need your help. Even if it doesn’t make sense to you." 
    jump frisk_meeting_play_snail_minigame
label frisk_meeting_choice61:
    #show Frisk big smile
    frisk "Nice!"
    frisk "Mom has a lot of different snail dishes. You wouldn’t believe what she can do with them!"
    frisk "Anyway..."
    jump frisk_meeting_play_snail_minigame
label frisk_meeting_play_snail_minigame:
    #show Frisk normal
    frisk "Here’s what I need you to do..."
    frisk "First, here, take this net."
    #player acquires net, which cannot be removed or dropped yet

    #/// if Check Butterfly Net
    "*It’s a big butterfly net, good for catching snails."

    frisk "Basically, just try to catch as many snails as you can!"
    frisk "It’s tricky, though, because you can only try to catch them for a certain amount of time per day. After that, they’ll start to get suspicious and won’t come out of their hiding places."
    frisk "Ready? Here we go!"

    ###-Snail mini game happens- (+5)
    $ frisk_fp +=5

    if frisk_fp >30 and frisk_fp <50:
        #/// If >(FP = 30 - 50)<
        #show Frisk normal
        frisk "That was good! Thanks for helping me out."
    elif frisk_fp >=50:
        #/// If >(FP > 50)<
        #show Frisk big smile
        frisk "Wow, you did great! Thanks again for helping. Toriel will be so happy!"
    else:
        #/// If >(FP < 30)<
        #show Frisk slightly happy
        frisk "Um, good job. You... um, did pretty well."

    #/// If >(Minigame score = MAX)<
    if minigamescore == MAX_SCORE:
        #+1 Perseverance
        $ perseverance +=1
        #show Frisk soulless
        frisk "..."
        frisk "...Good."
        frisk "Very good."
        #show Frisk normal
        frisk "You’re a natural!"


    #show Frisk tiny smile
    frisk "Ya know, I’m actually feeling a bit better right now."
    frisk "Mom will be happy, too... She really likes snails!"
    frisk "If you give her some, she’ll appreciate it. Maybe even pay you back somehow."
    frisk "She might want different kinds of snails on different days, so you might want to check with her to find out."
    #show Frisk surprised
    frisk "Oh!"
    #show Frisk big smile
    frisk "And if you want to do this again sometime, just tell me. This was fun!"
    frisk "...Or you could do it on your own, whatever works! Help in any form is appreciated!"
    #show Frisk normal
    frisk "I, uh, I should get going now. Mom is probably wondering why I’m out so late..."
    frisk "Our house isn’t too far from here. Do you want to come with me?"
    frisk "Mom and I would love it if you stayed for awhile..."
    jump frisk_meeting_selection11

label frisk_meeting_selection11:
    menu:
        "Yeah, I’m in!":
            $ frisk_fp +=3
            jump frisk_meeting_choice24
        "I’ll be there soon, but I think I’m gonna look around the Ruins for a little while longer.":            
            $ frisk_fp +=3
            jump frisk_meeting_choice25
        "I don’t want to stay with you guys." if torielinviteaccept==False:
            $ frisk_fp -=4
            #option 62 only available if the player has refused Toriel’s offers to stay (has NOT picked ruins outline option 56 OR ruins outline option 77)
            jump frisk_meeting_choice62
label frisk_meeting_choice24:
    #show Frisk big smile
    frisk "Alright, let’s go!"
    #scene change to Frisk and Toriel’s house
    #show Frisk small smile
    frisk "Here we are!"
    #show Frisk normal
    frisk "Hold on... let me tell Mom we’re back."
    #Frisk leaves the screen
    jump frisk_meeting_home
label frisk_meeting_choice25:
    frisk "Alright, that’s fine. I’ll see ya there!"
    frisk "Just be sure not to stay out too late. If you don’t get enough sleep, you could get sick."
    #show Frisk big smile
    frisk "I’m starting to sound like Mom now. Oh well... see ya!"
    $ option[25] = False
    #Frisk leaves. Player is free to roam. 
    if stamina==0:
        jump ruins_intro_pass_out
    else:
        jump frisk_meeting_late
    #If the player returns to Toriel’s house before running out of stamina, jump frisk_meeting_late
    #If the player does not return to Toriel’s house before running out of stamina, jump ruins_intro_pass_out
    
label frisk_meeting_choice62:
    #show Frisk disappointed
    frisk "Oh... okay. I just thought..."
    #show Frisk somewhat happy
    frisk "Well, if you ever change your mind, just stop on by our house! Mom and I love having guests."
    frisk "See ya later!"
    #Frisk leaves. Player is free to roam.
    #If the player returns to Toriel’s house before running out of stamina, jump ruins_intro_toriel_house (located in the ruins outline)
    #If the player does not return to Toriel’s house and accept her offer before running out of stamina, jump ruins_intro_pass_out (located in the ruins outline)
    if stamina==0:
        jump ruins_intro_pass_out
    else:
        jump frisk_meeting_late

label frisk_meeting_late:
    #Frisk off-screen
    frisk "Oh, I think they’re here. I’ll be right back!"
    #show Frisk normal
    frisk "Hi! You’re a bit late... the food is a little cold. But I’m sure it’s fine. Hold on, let me tell Mom you’re here."
    #Frisk off-screen again
    jump frisk_meeting_home

label frisk_meeting_home:
    #show Frisk normal
    #show Toriel normal
    frisk "This is the person I told you about."
    #If the player found Frisk BEFORE going to Toriel’s house:
    toriel "Ah, hello! It is very nice to have you over for dinner." 
    toriel "I do apologize for having to rush off so quickly before. Truthfully, I was a little worried about having to leave you on your own in the Ruins, but it is good to see that you are well."
    #show Frisk big smile
    frisk "Anyway, let’s eat!"
    toriel "Yes, please join us."
    if option[25]:
        jump chose_frisk_meeting_choice25
    else:
        jump frisk_meeting_eat
    #If the player went to Toriel’s house BEFORE finding Frisk:
    toriel "Welcome back! I am glad you and Frisk managed to find each other."
    #show Frisk big smile
    frisk "Anyway, let’s eat!"
    toriel "Yes, please join us."
    if option25:
        jump chose_frisk_meeting_choice25
    else:
        jump frisk_meeting_eat

label chose_frisk_meeting_choice25:

    toriel" “Frisk has told me a lot about you while you were gone.” "
    if toriel_fp<20:
        #/// If >(FP <20) - neutral rating
        #show Toriel normal
        toriel "There is not much to do here, but we are always looking for a helping hand--especially if you do not mind getting your hands dirty."
        #show Frisk big smile
        frisk "Anyway, let’s eat!"
        toriel "Yes, please join us."
        jump frisk_meeting_eat
    #/// If >(FP >20) - good rating            toriel//(+3)
    else:
        $ toriel_fp+=3
        #show Toriel smile
        toriel "It makes me happy to see you and Frisk have become such fast friends. It gets a little lonely here in the Ruins sometimes, and we do appreciate any well-meaning company." 
        toriel "I am sure you know this by now, but I would like you to know that any friend of Frisk is welcome here."
        #show Frisk big smile
        frisk "Anyway, let’s eat!"
        toriel "Yes, please join us."
        jump frisk_meeting_eat


label frisk_meeting_eat:
    #scene change living room
    #show Frisk normal
    #show Toriel normal
    frisk "I’m sure you’ll love it. We’re eating..."
    frisk "Mom, what’re we having again?"
    toriel "We are having snail casserole."
    #show Frisk somewhat happy
    frisk "Oh, good..."
    toriel "Is there something wrong?"
    frisk "Of course not. Hey, snail-catching friend, why don’t you try some?"
    "*You take a bite."
    "*..."
    "*It tastes..."
    "*...interesting."
    frisk "So, how is it?"
    toriel "Please, do tell."
    jump frisk_meeting_selection12
label frisk_meeting_selection12:
    menu:
        "It’s great, I love it!":            
            $ toriel_fp+=2
            $ frisk_fp+=2
            jump frisk_meeting_choice25_2
        "It’s not bad.":                     
            jump frisk_meeting_choice26
        "It’s kinda... bad.":                
            $ toriel_fp-=2
            $ frisk_fp-=2
            $ option[27] = False
            jump frisk_meeting_choice27
label frisk_meeting_choice25_2:
    #+1 Kindness
    $ kindness +=1
    #show Frisk surprised
    frisk "Really?"
    #show Frisk somewhat happy
    frisk "I mean, of course! I knew you would."
    toriel "Frisk, is there a problem with my cooking?"
    frisk "Never. Snails are great!"
    toriel "Oh, naturally. Either way, I am glad our guest seems to be enjoying them."

label frisk_meeting_choice26:
    #show Frisk normal
    frisk "See, I knew you would like it."
    toriel "Well, I try."

label frisk_meeting_choice27:
    #-1 Kindness
    $kindness -=1
    #show Frisk disappointed
    frisk "Shhh, don’t say that."
    #show Toriel annoyed
    toriel "Ah, well I suppose snails are not everyone's cup of tea. Still, they are the only thing around here that will fill you up. So, if you decide to stay, you will just have to get used to them."

    #show Frisk somewhat happy
    frisk "...So, um... how have you been liking the Ruins so far?"
    jump frisk_meeting_selection13
label frisk_meeting_selection13:
    menu:
        "I think I like it better than the surface!":    
            jump frisk_meeting_choice28
        "I don’t think I like this place.":         
            jump frisk_meeting_choice29
        "I hate this place.":                
            $ toriel_fp-=2
            $ frisk_fp-=4
            $ option[30] = False
            jump frisk_meeting_choice30
        "It scares me...":                    
            $ toriel_fp+=2
            $ frisk_fp+=2
            jump frisk_meeting_choice31
label frisk_meeting_choice28:
    #show Frisk surprised
    #show Toriel surprised
    frisk "D-do you really mean that?"
    #if the player chose option 27 of frisk_meeting_selection 12 (if not, skip this line and go right to frisk_meeting_selection 14)
    if option[27]===False:
        toriel "Even though you did not like the cooking?"
        jump frisk_meeting_selection14
    else:
        jump frisk_meeting_selection14
label frisk_meeting_selection14:
    menu:
        "Yeah!":                    
            $ toriel_fp+=4
            $ frisk_fp+=4
            jump frisk_meeting_choice32

        "Actually no, I just didn’t want to be rude.":
            $ toriel_fp-=2
            $ frisk_fp-=3
            jump frisk_meeting_choice33

label frisk_meeting_choice32:
    #+1 Integrity
    $ integrity +=1
    #show Frisk big smile
    #show Toriel smile
    frisk "That’s great!"
    toriel "Oh, well I’m glad you are enjoying your stay!"
    jump frisk_meeting_eat_after
label frisk_meeting_choice33:
    #-1 Integrity
    $ integrity -=1
    #show Toriel sad
    #show Frisk sad
    frisk "Oh... what?"
    toriel "I guess I should not be too surprised."
    #show Toriel small smile
    toriel "Well... erm... thank you for your consideration."
    #show Frisk somewhat happy
    frisk "Oh come on. It isn’t that bad, right?"
    jump frisk_meeting_eat_after
label frisk_meeting_choice29:
    #show Toriel normal
    toriel "Oh, I know things may be difficult for you at first. This must be very different from what you were used to on the surface, after all. Still, I do encourage you to give it a chance."
    #show Frisk big smile
    frisk "Yeah! It’s actually pretty great once you get used to everything!"
    jump frisk_meeting_eat_after
label frisk_meeting_choice30:
    #show Frisk sad
    frisk "Aw, but... it’s not that bad, really."
    #show Toriel awkward
    toriel "I understand that this place may not be to your liking."
    #show Toriel small smile
    toriel "But I think that, with a bit of time, you will learn to tolerate it."
    #show Frisk small smile
    frisk "R-right! It’s not so bad!"

    jump frisk_meeting_eat_after
label frisk_meeting_choice31:
    #-1 Bravery
    $ bravery -=1
    #show Toriel small smile
    toriel "Aww, poor thing. I had not realized until now that this must all seem very jarring."
    #show Frisk sad
    frisk "Oh, yeah."
    frisk "To be honest, when I first fell down here, I didn’t take it very well."
    #show Frisk sad
    frisk "When people tried to help, I shoved them away and ran..."
    #show Frisk teary eyes
    frisk "I even tried to run away from Mom. I thought she wanted to hurt me..."
    #show Toriel normal
    toriel "Frisk, please. Remember, I do not blame you for any of that. You were afraid, and I understand maybe I was being a bit... erm..."
    #show Toriel awkward
    toriel "...clingy, which you could have easily found threatening."
    #show Toriel small smile
    toriel "Besides, you are here now, and everything turned out alright."
    #show Frisk somewhat happy
    frisk "Yeah..."
    #show Frisk friendly smile
    frisk "So, the point is... I know this might be scary for now. But, if you give it a chance, I think you’ll find this place is actually pretty great."
    frisk "I mean it!"
    toriel "And we will be here to help you if you need anything."
    jump frisk_meeting_eat_after

label frisk_meeting_eat_after:
    #show Frisk normal
    frisk "Well, whatever you think, you're always welcome here."
    #show Toriel small smile
    toriel "Of course. It would be impolite to kick a guest out, especially if they have nowhere else to go. However, I must ask that you contribute to gathering food--specifically, snails--everyday."
    if option[27]==False or option[30]==False:
        #if the player has chosen option 27 or option 30 (if not, skip this line):
        toriel "And as long as you work on your manners..."

    toriel "Now please, have some more food. It is good for you." 
    toriel "Even though some people... may not find it to their taste."
    #show Frisk somewhat happy
    frisk "W-what are you looking at me for? I love all of your cooking!"
    #show Toriel laughing
    toriel "Oh, it is alright, my child. I know snails are not your favorite dish."
    #show Frisk 
    frisk "..."
    frisk "How long have you known?"
    toriel "A mother can always tell what her child is really thinking, but I do appreciate the sentiment."
    #show Frisk somewhat happy
    frisk "Oh..."
    frisk "Actually, is it okay if I turn in early? I feel a little tired."
    #show Toriel sad
    toriel "But you have hardly eaten anything."
    toriel "..."
    #show Toriel normal
    toriel "Oh, alright. After all, it is important that you get your rest."
    #show Frisk small smile
    frisk "Thanks, Mom."
    #Frisk exits the scene
    toriel "As for you, eat at least one more bite before you go."
    jump frisk_meeting_selection15
label frisk_meeting_selection15:
    menu:
        "No problem. I’ll even eat two bites!":        
            #//(+3)
            $toriel_fp+=3
            jump frisk_meeting_choice34
        "Fair enough.":                        
            #//(+0)
            jump frisk_meeting_choice35
        "But...":                            
            #//(-1)
            $toriel-=1
            jump frisk_meeting_choice36
label frisk_meeting_choice34:
    #+1 Perseverance
    $ perseverance +=1
    #show Toriel smile
    toriel "That’s the spirit."
    "*You take another bite."
    "*..."
    "*And another."
    "*You feel a bit... weird?"
    jump frisk_meeting_after_dinner
label frisk_meeting_choice35:
    #show Toriel normal
    toriel "Thank you."
    "*You take another bite"
    "*..."
    #if the player chose option 27 earlier:
    if option[27]==False:
        "*You bite off a bit too much. You gag, but you force it down."
        "*Uhg... "
        toriel "See, was that so hard?"
    #if the player chose option 25 or 26 earlier:
    if option[25]==False or option[26]==False:
        "*Eh..."
    jump frisk_meeting_after_dinner
label frisk_meeting_choice36:
    #/// If >36"But...":<
    #-1 Perseverance
    $ perseverance -=1
    #show Toriel annoyed
    toriel "No buts. Eat, or you’ll be hungry later."
    "*You take another bite."
    "*..."
    "*Meh..."

    jump frisk_meeting_after_dinner

label frisk_meeting_after_dinner:
    #show Toriel normal
    "Toriel “Thank you. You may be excused."

    #scene change to hallway
    "*What will you do now?"
    jump frisk_meeting_selection16

label frisk_meeting_selection16:
    menu:
        "Go back and talk to Toriel a bit longer" if option[37]:
            jump frisk_meeting_choice37
        "Check Toriel’s room":
            jump frisk_meeting_choice37_5
        "Go to bed":
            jump frisk_meeting_choice38
        "Go talk to Frisk":
            jump frisk_meeting_choice39
label frisk_meeting_choice37:
    #scene change living room
    #show Toriel surprised
    toriel "Oh, hello again. Did you want to talk about something?"
    jump frisk_meeting_selection17

label frisk_meeting_selection17:
menu:
    "What can I do?":
        jump frisk_meeting_choice40
    "Nothing in particular.":
        jump frisk_meeting_choice41
label frisk_meeting_choice40:
    #show Toriel normal
    toriel "Oh, good question!"
    #show Toriel awkward
    toriel "Hmm... There is not really any work to be done for the rest of the day--at least, not that I can think of at the moment."
    #show Toriel smile
    toriel "It appears you are off the hook. Personally, I would use this chance to rest. After all, you must be very tired by now. I know I would be! The ruins are not usually this lively."
    toriel "I will see you again in the morning... sleep well!"
    $ option[37]=False
    #scene change hallway
    jump frisk_meeting_after_dinner
label frisk_meeting_choice41:
    #+1 Patience
    $patience +=1
    toriel "Hm, that is alright. Although..."
    #show Toriel awkward
    toriel "I cannot think of anything to talk about quite yet, either. I suppose sitting in silence can be nice, too--if you would like to do that."    
    #show Toriel normal
    "*You and toriel sit in silence for a little while."
    "*It is nice."
    toriel "As much as I enjoy your company, I think it would be wise if you went to bed. We can always talk in the morning, if you wish."
    toriel "Sleep well!"
    $ option[37] = False
    #scene change hallway
    jump frisk_meeting_after_dinner
label frisk_meeting_choice37_5:
    #/// If >37.5(Check Toriel’s room)< 
    "*Toriel’s room strikes you as the type to be clean, orderly, and cozy."
    "*Going inside would be a huge invasion of privacy. You should know better."
    jump frisk_meeting_selection18
label frisk_meeting_selection18:
    menu:
        "Go inside anyway":
            jump frisk_meeting_choice63
        "Do not":
            jump frisk_meeting_choice64
label frisk_meeting_choice63:
    $ diary = 0
    #-1 Justice
    $ justice -=1
    "*There are a plethora of items to snoop through."
    #see questions at top of doc
    jump frisk_meeting_selection21

label frisk_meeting_selection21:

    menu:
        "Look in the diary" if option[65]:
            $ diary+=1
            jump frisk_meeting_choice65
        "Examine the chair" if option[66]:
            jump frisk_meeting_choice66
        "Examine the cactus" if option[67]:
            jump frisk_meeting_choice67
        "Examine the shelf" if option[68]:
            jump frisk_meeting_choice68
        "Look in the drawer" if option[69]:
            jump frisk_meeting_choice69
        "Examine the bed" if option[70]:
            jump frisk_meeting_choice70
        "Examine the bucket" if option[71]:
            jump frisk_meeting_choice71
        "Leave Toriel’s room" if option[72]:
            jump frisk_meeting_choice72
label frisk_meeting_choice65:
    #/// If >65(Look in the diary)x1<
    if diary==1:
        "*There are several entries about humans, but most of the diary is filled with random, bad puns."
        #return to frisk_meeting_selection 21
        jump frisk_meeting_selection21
    elif diary==2:
        #/// If >65(Look in the diary)x2<
        "*The man who invented knock-knock jokes must have won the No-Bell prize."
        #return to frisk_meeting_selection 21
        jump frisk_meeting_selection21
    elif diary==3:
        #/// If >65(Look in the diary)x3<
        "*Toucan do jokes as good as mine only if you dove in. No need to swallow your pride to make one."
        #rejump frisk_meeting_selection21turn to frisk_meeting_selection 21
        jump frisk_meeting_selection21
    else:
    #/// If >65(Look in the diary)x4+<
        "*In the midst of bad puns, you find a rather serious entry. It seems personal..."
        jump frisk_meeting_selection22
label frisk_meeting_selection22:
    menu:
        "Read it":
            jump frisk_meeting_choice73
        "Do not":
            jump frisk_meeting_choice74
label frisk_meeting_choice73:
    "*Frisk has been acting strange recently. Some days, they seem exhausted despite going to bed at a decent hour. I am uncertain as to why this is, but I have my ideas. I am not sure if I should confront them about it, though. They might not be as energetic as they were when they first came here, but they seem happier now more than ever. I must think on this."
    $ option[65]=False
    jump frisk_meeting_selection21
label frisk_meeting_choice74:
    "*You shouldn’t peek..."
    jump frisk_meeting_selection21
label frisk_meeting_choice66:
    "*The chair seems really cozy. Anyone could spend hours writing while sitting in this beauty."
    $ option[66]=False
    jump frisk_meeting_selection21
label frisk_meeting_choice67:
    if cactus == 1:
        "*Ah, truly stunning, a plant that can survive in such extreme heat."
        "*It looks like it’s rooting for you."
        jump frisk_meeting_selection21
    else:
        "*Truly the most tsundere of plants."
        $ option[67]= False
        jump frisk_meeting_selection21
label frisk_meeting_choice68:
    "*There are several books about cooking, gardening, and bug hunting. There is even one called “101 Snail Facts.” It looks well-thumbed."
    $ option[68]= False
    jump frisk_meeting_selection21
label frisk_meeting_choice69:
    "*There are a lot of socks for someone who doesn’t need them... s-scandalous."
    $ option[69]= False
    jump frisk_meeting_selection21
label frisk_meeting_choice70:
    "*It’s way more comfortable than it looks."
    $ option[70]= False
    jump frisk_meeting_selection21
label frisk_meeting_choice71:
    "*This bucket is filled entirely with a slimy mass of live snails."
    "*Looks delicious."
    $ option[71]= False
    jump frisk_meeting_selection21
label frisk_meeting_choice72:
    "*Finally, you’re done snooping."
    "*Don’t you feel even a little guilty about what you’ve done?"
    $ option37_5 = False
    jump frisk_meeting_after_dinner
label frisk_meeting_choice64:
    #+1 Justice
    "*You are above that."
    $ option37_5 = False
    #scene change hallway
    jump frisk_meeting_after_dinner

label frisk_meeting_choice38:
    "*You hear Toriel calling from the kitchen."
    toriel "I forgot to mention, there is a room you can use at the far end of the hall. Goodnight, and sleep well!"
    #scene change MC’s room
    "*You enter the room, plop down on the bed, and fall asleep..."
    "*..."
    #END DAY 1
label frisk_meeting_choice39:
    "*You see a light on in one of the rooms."
    #scene change Frisk’s room
    #show Frisk big smile
    "Frisk “Oh, hi again!"
    #show Frisk normal
    "Frisk “Something on your mind?"
    jump frisk_meeting_selection19

label frisk_meeting_selection19:    
    menu:
        "How are you?" if option[40]:                        
            $ frisk_fp +=1
            jump frisk_meeting_choice40_2
        "I was just stopping by to say ‘hey’. I’m heading off to bed. Goodnight!":                        
            $ frisk_fp +=1
            jump frisk_meeting_choice41_2
        "What’s all that stuff you have on your shelves?": 
            #//(+0)
            jump frisk_meeting_choice42
label frisk_meeting_choice40_2:
    frisk "I’m doing fine, thank you."
    $ option[40]=False
    #go back to frisk_meeting_selection 19
    jump frisk_meeting_selection19
label frisk_meeting_choice41_2:
    #show Frisk small smile
    frisk "Oh, alright. That was nice of you!"
    frisk "Goodnight!"
    $ option[39]=False
    #scene change hallway
    jump frisk_meeting_after_dinner
label frisk_meeting_choice42:
    #show Frisk normal
    frisk "Oh, just a couple of things from the Underground."
    jump frisk_meeting_selection20
label frisk_meeting_selection20:
    menu:
        "Just wondering. I think I’ll be heading off to bed now.":
            jump frisk_meeting_choice43
        "But how did you actually get all of this?":
            jump frisk_meeting_choice44

label frisk_meeting_choice43:
    #show Frisk normal
    frisk "Oh, okay. It was nice seeing you."
    frisk "Goodnight!"
    $ option[39] = False
    #remove option 39 from frisk_meeting_selection 16
    #scene change hallway
    jump frisk_meeting_after_dinner
label frisk_meeting_choice44:
    #show Frisk blush
    frisk "Oh, you know..." 
    frisk "I just found it laying around..."
    #show Frisk normal
    frisk "Actually, I’m pretty tired. I think I’m gonna go to bed, sorry."
    frisk "Goodnight!"
    $ option[39]=False
    #remove option 39 from frisk_meeting_selection 16
    #scene change hallway
    jump frisk_meeting_after_dinner
