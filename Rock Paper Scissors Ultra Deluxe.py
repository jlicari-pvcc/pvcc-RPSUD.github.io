import random
import time
from playsound3 import playsound

choiceInput = "" #For picking hand weapons.
CPUchoice = 0 #For picking hand weapons and choosing new hand weapons.
previousInput = "" #For saving the user's previous hand weapon choice.
randomEvent = 0 #The RNG of hand weapon interactions.
UserActiveStun = 0 #Whether the user skips a move, denoted by 0 and 1.
CPUActiveStun = 0 #Whether the CPU skips a move, denoted by 0 and 1.
userHealth = 10 #Always 10. No more, no less.
maxUserHealth = 10 #No overhealing.
game_number = 1 #Number of games happened, starts at 1.
score = 0 #Adds from winning rounds, subtracts from losing rounds. Extra points when no more new hand weapons are available.
userWeapons = ["ROCK", "PAPER", "SCISSORS"]
CPUWeapons = ["Rock", "Paper", "Scissors"]
newWeapons = ["GEODE", "BOULDER", "SANDPAPER", "ALUMINUM FOIL", "CLAW", "PAPER SHREDDER", "FINGER GUN", "THUMBS UP", "TELEPHONE", "HOOK"]
newCPUWeapons = ["Finger Gun", "Rubber Band Gun", "Silent Fox", "Thumbs Up", "Telephone", "Hook", "Devil Horns"]

#Weapon Specific Activations
GeodeActive = 0 #Win against Paper after going against Rock, denoted by 0 and 1.
BoulderForm = 0 #Changes the state of Boulder to become cracked. Denoted by 0 and 1.
PaperShredderForm = 0 #Changes the state of Paper Shredder after going against Rock, Scissors, or Thumbs Up to become useless. Denoted by 0 and 1.
RemoteActive = 0 #Changes the ability that Remote can or can't disable a CPU's hand weapon. Denoted by 0 and 1.
RemoteActiveRounds = 0 #Counts how many rounds that CPU's hand weapon has been disabled.
RemoteDisabledWeapon = "" #Remote's ability to removing the CPU's option to play that certain hand weapon.
HookActiveUser = 0 #Changes the state whether Hook can critically win or not for the user. Denoted by 0 and 1.
HookActiveCPU = 0 #Changes the state whether Hook can critically win or not for the CPU. Denoted by 0 and 1.
HarpoonActive = 0 #Changes the state whether Harpoon can MEGA critically win or not for the user. Denoted by 0 and 1.
SilentActive = 0 #Changes the ability that Silent Fox can or can't disable a user's hand weapon. Denoted by 0 and 1.
SilentActiveRounds = 0 #Counts how many rounds that user's hand weapon has been disabled.
SilentDisabledWeapon = "" #Silent Fox's ability to removing a user's option to play that certain hand weapon.
DevilActive = 0 #Changes the ability that Devil Horns can or can't curse a user's hand weapon. Denoted by 0 and 1.
DevilCursedWeapon = "" #Devil Horns' ability to cursing a user's hand weapon throughout a game.
DevilHappen = 0 #Stops the Devil Horns' curse to happen when curse is inflicted.

#Audio Files (Mostly Taken from Undertale and Deltarune)
meow = "meow.mp3" #Plays when executing the program (this game). Meow :3
game_start = "game_start.mp3" #Plays when a new game starts against a CPU.
game_over = "game_over.mp3" #Plays when the user runs out of HP in a game.
win = "win.mp3" #Plays when the user wins a round.
lose = "lose.mp3" #Plays when the user lost a round.
tie = "tie.mp3" #Plays when user and CPU tie or nothing happens.
ding = "ding.mp3" #Plays during the Chant.
smack = "smack.mp3" #Plays at the end of Chant.
deflect = "deflect.mp3" #Plays when a hand weapon deflects into a tie.
critical_dmg = "critical_hit.mp3" #Plays when a hand weapon does a critical win / loss.
mega_critical = "mega_critical_hit.mp3" #Plays when a hand weapon does a mega critical win / loss.
activation = "activation.mp3" #Plays when a hand weapon activates a special ability.
stun = "stun.mp3" #Plays when a hand weapon creates a stun to user / CPU.
shot = "shot.mp3" #Exclusive Gunslinger hand weapon duel with Finger Gun.
telephoneStun = "telephone_stun.mp3" #Exclusive Telephone hand weapon ring to stun.
disable = "disable.mp3" #Plays when a hand weapon is disabled.
disable_off = "disable_off.mp3" #Plays when a hand weapon isn't disabled anymore.
curse = "curse.mp3" #Plays when a hand weapon applies curse to another hand weapon.
curse_activate = "curse_activate.mp3" #Plays when curse works.
heal = "heal.mp3" #Plays when a hand weapon heals to user / CPU.
winner = "winning_game.mp3" #Plays when the user wins a game.
new = "new.mp3" #Plays when the user is now given the choice of a new hand weapon.
gleam = "gleam.mp3" #Plays when a new hand weapon option appears.
acquire_new = "acquired_new.mp3" #Plays when user adds a new hand weapon to their arsenal.
acquire_upgrade = "acquired_upgrade.mp3" #Plays when user upgrades an existing hand weapon in their arsenal.
invalid = "invalid.mp3" #Plays when user inputs something not part of the given options.
good_game = "good_game.mp3" #Plays when user WINS the game!

#Classic Rock Paper Scissors Chant
def chant():
    print("Rock...")
    playsound(ding)
    print("Paper...")
    playsound(ding)
    print("Scissors...")
    playsound(ding)
    print("Shoot!")
    playsound(smack)
    print("")

#Hand Weapon Logic
def logic(choiceInput, CPUchoice):
    #Global Variables / Values
    global round_num
    global userHealth
    global CPUHealth
    global previousInput
    global randomEvent
    global UserActiveStun
    global CPUActiveStun
    global score

    #Weapon Specific Activations
    global GeodeActive
    global BoulderForm
    global PaperShredderForm
    global RemoteActive
    global RemoteActiveRounds
    global RemoteDisabledWeapon
    global HookActiveUser
    global HookActiveCPU
    global HarpoonActive
    global SilentActive
    global SilentActiveRounds
    global SilentDisabledWeapon
    global DevilActive
    global DevilCursedWeapon
    global DevilHappen
    
    #General Stun Check
    if UserActiveStun == 1: #For User
        if CPUchoice == "Rock":
            print("The CPU played Rock. Owch!")
            print("You snapped back from the stun!")
            playsound(lose)
            userHealth -= 1
            score -= 2
            UserActiveStun = 0
        elif CPUchoice == "Paper":
            print("The CPU played Paper. Owch?")
            print("You snapped back from the stun!")
            playsound(lose)
            userHealth -= 1
            score -= 2
            UserActiveStun = 0
        elif CPUchoice == "Scissors":
            print("The CPU played Scissors. You CRITICALLY lost... Owchie!")
            print("You snapped back from the stun!")
            playsound(critical_dmg)
            userHealth -= 2
            score -= 3
            UserActiveStun = 0
        elif CPUchoice == "Finger Gun":
            print("The CPU played Finger Gun. Owch!")
            print("You snapped back from the stun!")
            playsound(lose)
            userHealth -= 1
            score -= 2
            UserActiveStun = 0
        elif CPUchoice == "Rubber Band Gun":
            print("The CPU played Rubber Band Gun. Stunned again!")
            playsound(stun)
        elif CPUchoice == "Silent Fox":
            print("The CPU played Silent Fox. Nothing happened.")
            print("You snapped back from the stun!")
            playsound(tie)
            UserActiveStun = 0
        elif CPUchoice == "Thumbs Up":
            print("The CPU played Thumbs Up. The CPU heals 1 HP.")
            print("You snapped back from the stun!")
            playsound(heal)
            CPUHealth += 1
            UserActiveStun = 0
        elif CPUchoice == "Telephone":
            print("The CPU played Telephone. Owch!")
            print("You snapped back from the stun!")
            playsound(lose)
            userHealth -= 1
            score -= 2
            UserActiveStun = 0
        elif CPUchoice == "Hook":
            if HookActiveCPU == 0:
                print("The CPU played Hook. Owch!")
                print("You snapped back from the stun!")
                playsound(lose)
                userHealth -= 1
                score -= 2
            elif HookActiveCPU == 1:
                print("The CPU played Hook. You CRITICALLY lost... Owchie! The CPU's Hook now reverts back to regular wins.")
                print("You snapped back from the stun!")
                playsound(critical_dmg)
                playsound(activation)
                HookActiveCPU = 0
                userHealth -= 2
                score -= 3
            UserActiveStun = 0
        elif CPUchoice == "Devil Horns":
            print("The CPU played Devil Horns. Owch!")
            print("You snapped back from the stun!")
            playsound(lose)
            userHealth -= 1
            score -= 2
            UserActiveStun = 0
    elif CPUActiveStun == 1: #For CPU
        if choiceInput.upper() == "ROCK":
            print("You played Rock and win!")
            print("The CPU snapped back from the stun!")
            playsound(win)
            CPUHealth -= 1
            score += 3
            CPUActiveStun = 0
        elif choiceInput.upper() == "PAPER":
            print("You played Paper and win?")
            print("The CPU snapped back from the stun!")
            playsound(win)
            CPUHealth -= 1
            score += 3
            CPUActiveStun = 0
        elif choiceInput.upper() == "SCISSORS":
            print("You played Scissors and CRITICALLY win!")
            print("The CPU snapped back from the stun!")
            playsound(critical_dmg)
            CPUHealth -= 2
            score += 4
            CPUActiveStun = 0
        elif choiceInput.upper() == "GEODE":
            print("You played Geode and win!")
            print("The CPU snapped back from the stun!")
            playsound(win)
            CPUHealth -= 1
            score += 3
            CPUActiveStun = 0
        elif choiceInput.upper() == "BOULDER":
            if BoulderForm == 0: #Base Form
                print("You played Boulder and win!")
                print("The CPU snapped back from the stun!")
                playsound(win)
                CPUHealth -= 1
                score += 3
            elif BoulderForm == 1: #Cracked Form
                print("You played a cracked Boulder and win!")
                print("However, your Boulder is now broken and reverts back to Rock.")
                playsound(win)
                playsound(activation)
                userWeapons.remove("BOULDER") #Remove Boulder from the user's hand weapons
                userWeapons.append("ROCK") #Add Rock back into the user's hand weapons
                newWeapons.append("GEODE") #Add Geode back into the pool
                newWeapons.append("BOULDER") #Add Boulder back into the pool
                CPUHealth -= 1
                score += 3
            CPUActiveStun = 0
        elif choiceInput.upper() == "SANDPAPER":
            print("You played Sandpaper and win!")
            print("The CPU snapped back from the stun!")
            playsound(win)
            CPUHealth -= 1
            score += 3
            CPUActiveStun = 0
        elif choiceInput.upper() == "ALUMINUM FOIL":
            print("You played Aluminum Foil and win!")
            print("The CPU snapped back from the stun!")
            playsound(win)
            CPUHealth -= 1
            score += 3
            CPUActiveStun = 0
        elif choiceInput.upper() == "CLAW":
            print("You played Claw and CRITICALLY win!")
            print("The CPU snapped back from the stun!")
            playsound(critical_dmg)
            CPUHealth -= 2
            score += 4
            CPUActiveStun = 0
        elif choiceInput.upper() == "PAPER SHREDDER":
            if PaperShredderForm == 0: #Base Form
                print("You played Paper Shredder and win!")
                print("The CPU snapped back from the stun!")
                playsound(win)
                CPUHealth -= 1
                score += 3
            elif PaperShredderForm == 1: #Jammed Form
                print("You played a jammed Paper Shredder. Nothing happened.")
                print("The CPU snapped back from the stun!")
                playsound(tie)
            CPUActiveStun = 0
        elif choiceInput.upper() == "FINGER GUN":
            print("You played Finger Gun and win!")
            print("The CPU snapped back from the stun!")
            playsound(win)
            CPUHealth -= 1
            score += 3
            CPUActiveStun = 0
        elif choiceInput.upper() == "GUNSLINGER":
            print("You played Gunslinger and win!")
            print("The CPU snapped back from the stun!")
            playsound(win)
            CPUHealth -= 1
            score += 3
            CPUActiveStun = 0
        elif choiceInput.upper() == "THUMBS UP":
            print("You played Thumbs Up and heal 1 HP!")
            print("The CPU snapped back from the stun!")
            playsound(heal)
            userHealth += 1
            CPUActiveStun = 0
        elif choiceInput.upper() == "THUMBS DOWN":
            print("You played Thumbs Down and win!")
            print("The CPU snapped back from the stun!")
            playsound(win)
            CPUHealth -= 1
            score += 3
            CPUActiveStun = 0
        elif choiceInput.upper() == "TELEPHONE":
            print("You played Telephone and win!")
            print("The CPU snapped back from the stun!")
            playsound(win)
            CPUHealth -= 1
            score += 3
            CPUActiveStun = 0
        elif choiceInput.upper() == "HOOK":
            if HookActiveUser == 0:
                print("You played Hook and win!")
                print("The CPU snapped back from the stun!")
                playsound(win)
                CPUHealth -= 1
                score += 3
            elif HookActiveUser == 1:
                print("You played Hook. You CRITICALLY win! Your Hook now reverts back to regular wins.")
                print("The CPU snapped back from the stun!")
                playsound(critical_dmg)
                playsound(activation)
                HookActiveUser = 0
                CPUHealth -= 2
                score += 4
            CPUActiveStun = 0
        elif choiceInput.upper() == "HARPOON":
            if HarpoonActive == 0:
                print("You played Harpoon and win!")
                print("The CPU snapped back from the stun!")
                playsound(win)
                CPUHealth -= 1
                score += 3
            elif HarpoonActive == 1:
                print("You played Harpoon. You MEGA CRITICALLY win! Your Harpoon now reverts back to regular wins.")
                print("The CPU snapped back from the stun!")
                playsound(mega_critical)
                playsound(activation)
                HarpoonActive = 0
                CPUHealth -= 3
                score += 5
            CPUActiveStun = 0
    
    else:
    
    #Rock Matchups
        if choiceInput.upper() == "ROCK" and CPUchoice == "Rock": #Rock vs. Rock
            print("You played Rock, and the CPU played Rock. Tie.")
            playsound(tie)
        elif choiceInput.upper() == "ROCK" and CPUchoice == "Paper": #Rock vs. Paper
            print("You played Rock, and the CPU played Paper. You lost...")
            playsound(lose)
            userHealth -= 1
            score -= 2
        elif choiceInput.upper() == "ROCK" and CPUchoice == "Scissors": #Rock vs. Scissors
            print("You played Rock, and the CPU played Scissors. You win!")
            playsound(win)
            CPUHealth -= 1
            score += 3
        elif choiceInput.upper() == "ROCK" and CPUchoice == "Finger Gun": #Rock vs. Finger Gun
            print("You played Rock, and the CPU played Finger Gun. You lost...")
            playsound(lose)
            userHealth -= 1
            score -= 2
        elif choiceInput.upper() == "ROCK" and CPUchoice == "Rubber Band Gun": #Rock vs. Rubber Band Gun
            print("You played Rock, and the CPU played Rubber Band Gun. You got stunned!")
            playsound(stun)
            UserActiveStun = 1
        elif choiceInput.upper() == "ROCK" and CPUchoice == "Silent Fox": #Rock vs. Silent Fox
            print("You played Rock, and the CPU played Silent Fox. You lost...")
            playsound(lose)
            userHealth -= 1
            score -= 2
        elif choiceInput.upper() == "ROCK" and CPUchoice == "Thumbs Up": #Rock vs. Thumbs Up
            print("You played Rock, and the CPU played Thumbs Up. Tie, but the CPU heals 1 HP.")
            playsound(tie)
            playsound(heal)
            CPUHealth += 1
        elif choiceInput.upper() == "ROCK" and CPUchoice == "Telephone": #Rock vs. Telephone
            print("You played Rock, and the CPU played Telephone. You win!")
            playsound(win)
            CPUHealth -= 1
            score += 3
        elif choiceInput.upper() == "ROCK" and CPUchoice == "Hook": #Rock vs. Hook
            if HookActiveCPU == 0: #Ability Not Active
                print("You played Rock, and the CPU played Hook. You lost...")
                playsound(lose)
                userHealth -= 1
                score -= 2
            elif HookActiveCPU == 1: #Ability Active
                print("You played Rock, and the CPU played Hook. You CRITICALLY lost... The CPU's Hook now reverts back to regular wins.")
                playsound(critical_dmg)
                playsound(activation)
                HookActiveCPU = 0
                userHealth -= 2
                score -= 3
        elif choiceInput.upper() == "ROCK" and CPUchoice == "Devil Horns": #Rock vs. Devil Horns
            print("You played Rock, and the CPU played Devil Horns. Tie.")
            playsound(tie)
            if DevilActive == 0: #Ability Not Active
                randomEvent = random.randint(1, 2) #50% of Curse
                if randomEvent == 1: #Curse
                    print("However, your Rock got cursed by the CPU's Devil Horns! Throughout this game, when you play Rock again it now has a 25% chance that you'll hurt yourself for 1 damage!")
                    playsound(curse)
                    DevilActive = 1
                    DevilCursedWeapon = choiceInput.upper()
                    DevilHappen = 1
    
    #Paper Matchups
        elif choiceInput.upper() == "PAPER" and CPUchoice == "Rock": #Paper vs. Rock
            print("You played Paper, and the CPU played Rock. You win!")
            playsound(win)
            CPUHealth -= 1
            score += 3
        elif choiceInput.upper() == "PAPER" and CPUchoice == "Paper": #Paper vs. Paper
            print("You played Paper, and the CPU played Paper. Tie.")
            playsound(tie)
        elif choiceInput.upper() == "PAPER" and CPUchoice == "Scissors": #Paper vs. Scissors
            print("You played Paper, and the CPU played Scissors. You lost...")
            playsound(lose)
            userHealth -= 1
            score -= 2
        elif choiceInput.upper() == "PAPER" and CPUchoice == "Finger Gun": #Paper vs. Finger Gun
            print("You played Paper, and the CPU played Finger Gun. You CRITICALLY lost... Owchie!")
            playsound(critical_dmg)
            userHealth -= 2
            score -= 3
        elif choiceInput.upper() == "PAPER" and CPUchoice == "Rubber Band Gun": #Paper vs. Rubber Band Gun
            print("You played Paper, and the CPU played Rubber Band Gun. You got stunned!")
            playsound(stun)
            UserActiveStun = 1
        elif choiceInput.upper() == "PAPER" and CPUchoice == "Silent Fox": #Paper vs. Silent Fox
            print("You played Paper, and the CPU played Silent Fox. Tie.")
            playsound(tie)
        elif choiceInput.upper() == "PAPER" and CPUchoice == "Thumbs Up": #Paper vs. Thumbs Up
            print("You played Paper, and the CPU played Thumbs Up. You win!")
            playsound(win)
            CPUHealth -= 1
            score += 3
        elif choiceInput.upper() == "PAPER" and CPUchoice == "Telephone": #Paper vs. Telephone
            print("You played Paper, and the CPU played Telephone. Tie.")
            playsound(tie)
        elif choiceInput.upper() == "PAPER" and CPUchoice == "Hook": #Paper vs. Hook
            if HookActiveCPU == 0: #Ability Not Active
                print("You played Paper, and the CPU played Hook. You win! However, the CPU's Hook can now CRITICALLY win for it's next win.")
                playsound(win)
                playsound(activation)
                HookActiveCPU = 1
            elif HookActiveCPU == 1: #Ability Active
                print("You played Paper, and the CPU played Hook. You win!")
                playsound(win)
            CPUHealth -= 1
            score += 3
        elif choiceInput.upper() == "PAPER" and CPUchoice == "Devil Horns": #Paper vs. Devil Horns
            print("You played Paper, and the CPU played Devil Horns. You lost...")
            playsound(lose)
            userHealth -= 1
            score -= 2
    
    #Scissors Matchups
        elif choiceInput.upper() == "SCISSORS" and CPUchoice == "Rock": #Scissors vs. Rock
            print("You played Scissors, and the CPU played Rock. You lost...")
            playsound(lose)
            userHealth -= 1
            score -= 2
        elif choiceInput.upper() == "SCISSORS" and CPUchoice == "Paper": #Scissors vs. Paper
            print("You played Scissors, and the CPU played Paper. You win!")
            playsound(win)
            CPUHealth -= 1
            score += 3
        elif choiceInput.upper() == "SCISSORS" and CPUchoice == "Scissors": #Scissors vs. Scissors
            print("You played Scissors, and the CPU played Scissors. Tie.")
            playsound(tie)
        elif choiceInput.upper() == "SCISSORS" and CPUchoice == "Finger Gun": #Scissors vs. Finger Gun 
            randomEvent = random.randint(1, 2) #50% of Tie
            if randomEvent == 1: #Lose
                print("You played Scissors, and the CPU played Finger Gun. You tried to deflect the attack, but you lost...")
                playsound(lose)
                userHealth -= 1
                score -= 2
            elif randomEvent == 2: #Tie
                print("You played Scissors, and the CPU played Finger Gun. You deflected the attack, tie!")
                playsound(deflect)
        elif choiceInput.upper() == "SCISSORS" and CPUchoice == "Rubber Band Gun": #Scissors vs. Rubber Band Gun
            print("You played Scissors, and the CPU played Rubber Band Gun. Tie.")
            playsound(tie)
        elif choiceInput.upper() == "SCISSORS" and CPUchoice == "Silent Fox": #Scissors vs. Silent Fox
            if SilentActive == 0: #No Disabled Weapon
                randomEvent = random.randint(1, 2) #50% for User Disable
                if randomEvent == 1: #Disable
                    print("You played Scissors, and the CPU played Silent Fox. You win! However, Silent Fox disabled your Scissors for two rounds!")
                    playsound(win)
                    playsound(disable)
                    SilentDisabledWeapon = choiceInput.upper()
                    userWeapons.remove(SilentDisabledWeapon)
                    SilentActive = 1
                else:
                    print("You played Scissors, and the CPU played Silent Fox. You win!")
                    playsound(win)
            else:
                print("You played Scissors, and the CPU played Silent Fox. You win!")
                playsound(win)
            CPUHealth -= 1
            score += 3
        elif choiceInput.upper() == "SCISSORS" and CPUchoice == "Thumbs Up": #Scissors vs. Thumbs Up
            print("You played Scissors, and the CPU played Thumbs Up. You win!")
            playsound(win)
            CPUHealth -= 1
            score += 3
        elif choiceInput.upper() == "SCISSORS" and CPUchoice == "Telephone": #Scissors vs. Telephone
            randomEvent = random.randint(1, 2) #50% for User Stun
            if randomEvent == 1: #No Stun
                print("You played Scissors, and the CPU played Telephone. You lost...")
                playsound(lose)
            elif randomEvent == 2: #Stun
                print("You played Scissors, and the CPU played Telephone. You lost and got stunned!")
                playsound(lose)
                playsound(telephoneStun)
                playsound(stun)
                UserActiveStun = 1
            userHealth -= 1
            score -= 2
        elif choiceInput.upper() == "SCISSORS" and CPUchoice == "Hook": #Scissors vs. Hook
            print("You played Scissors, and the CPU played Hook. Tie.")
            playsound(tie)
        elif choiceInput.upper() == "SCISSORS" and CPUchoice == "Devil Horns": #Scissors vs. Devil Horns
            print("You played Scissors, and the CPU played Devil Horns. You win!")
            playsound(win)
            CPUHealth -= 1
            score += 3
    
    #Geode Matchups
        elif choiceInput.upper() == "GEODE" and CPUchoice == "Rock": #Geode vs. Rock
            if GeodeActive == 0: #Not Activated
                print("You played Geode, and the CPU played Rock. You win! Plus, your Geode smashed through Rock to reveal crystals to now win to Paper next time!")
                playsound(win)
                playsound(activation)
                GeodeActive = 1
            elif GeodeActive == 1: #Activated
                print("You played Geode, and the CPU played Rock. You win!")
                playsound(win)
            CPUHealth -= 1
            score += 3
        elif choiceInput.upper() == "GEODE" and CPUchoice == "Paper": #Geode vs. Paper
            if GeodeActive == 0: #Not Activated
                print("You played Geode, and the CPU played Paper. You lost...")
                playsound(lose)
                userHealth -= 1
                score -= 2
            elif GeodeActive == 1: #Activated
                print("You played Geode, and the CPU played Paper. You win!")
                playsound(win)
                CPUHealth -= 1
                score += 3
        elif choiceInput.upper() == "GEODE" and CPUchoice == "Scissors": #Geode vs. Scissors
            print("You played Geode, and the CPU played Scissors. You Win!")
            playsound(win)
            CPUHealth -= 1
            score += 3
        elif choiceInput.upper() == "GEODE" and CPUchoice == "Finger Gun": #Geode vs. Finger Gun
            print("You played Geode, and the CPU played Finger Gun. You Win!")
            playsound(win)
            CPUHealth -= 1
            score += 3
        elif choiceInput.upper() == "GEODE" and CPUchoice == "Rubber Band Gun": #Geode vs. Rubber Band Gun
            print("You played Geode, and the CPU played Rubber Band Gun. You got stunned!")
            playsound(stun)
            UserActiveStun = 1
        elif choiceInput.upper() == "GEODE" and CPUchoice == "Silent Fox": #Geode vs. Silent Fox
            print("You played Geode, and the CPU played Silent Fox. You Lost...")
            playsound(lose)
            userHealth -= 1
            score -= 2
        elif choiceInput.upper() == "GEODE" and CPUchoice == "Thumbs Up": #Geode vs. Thumbs Up
            print("You played Geode, and the CPU played Thumbs Up. Tie, but the CPU heals 1 HP.")
            playsound(tie)
            playsound(heal)
            CPUHealth += 1
        elif choiceInput.upper() == "GEODE" and CPUchoice == "Telephone": #Geode vs. Telephone
            randomEvent = random.randint(1, 2) #50% for User Stun
            if randomEvent == 1: #No Stun
                print("You played Geode, and the CPU played Telephone. You lost...")
                playsound(lose)
            elif randomEvent == 2: #Stun
                print("You played Geode, and the CPU played Telephone. You lost and got stunned!")
                playsound(lose)
                playsound(telephoneStun)
                playsound(stun)
                UserActiveStun = 1
            userHealth -= 1
            score -= 2
        elif choiceInput.upper() == "GEODE" and CPUchoice == "Hook": #Geode vs. Hook
            print("You played Geode, and the CPU played Hook. Tie.")
            playsound(tie)
        elif choiceInput.upper() == "GEODE" and CPUchoice == "Devil Horns": #Geode vs. Devil Horns
            print("You played Geode, and the CPU played Devil Horns. You win!")
            playsound(win)
            CPUHealth -= 1
            score += 3
    
    #Boulder Matchups
        elif choiceInput.upper() == "BOULDER" and CPUchoice == "Rock": #Boulder vs. Rock
            if BoulderForm == 0:
                print("You played Boulder, and the CPU played Rock. You win!")
                playsound(win)
                randomEvent = random.randint(1, 4)
                if randomEvent == 1: #25% to turn cracked
                    print("However, your Boulder became cracked! It can now break if used again.")
                    playsound(activation)
                    BoulderForm = 1
            elif BoulderForm == 1:
                print("You played a cracked Boulder, and the CPU played Rock. You win!")
                playsound(win)
                print("Your Boulder is now broken and reverts back to Rock.")
                playsound(activation)
                userWeapons.remove("BOULDER") #Remove Boulder from the user's hand weapons
                userWeapons.append("ROCK") #Add Rock back into the user's hand weapons
                newWeapons.append("GEODE") #Add Geode back into the pool
                newWeapons.append("BOULDER") #Add Boulder back into the pool
            CPUHealth -= 1
            score += 3
        elif choiceInput.upper() == "BOULDER" and CPUchoice == "Paper": #Boulder vs. Paper
            if BoulderForm == 0: #Base Form
                print("You played Boulder, and the CPU played Paper. You lost...")
                playsound(lose)
            elif BoulderForm == 1: #Cracked Form
                print("You played a cracked Boulder, and the CPU played Paper. You lost...")
                playsound(lose)
                print("Your Boulder is now broken and reverts back to Rock.")
                playsound(activation)
                userWeapons.remove("BOULDER") #Remove Boulder from the user's hand weapons
                userWeapons.append("ROCK") #Add Rock back into the user's hand weapons
                newWeapons.append("GEODE") #Add Geode back into the pool
                newWeapons.append("BOULDER") #Add Boulder back into the pool
            userHealth -= 1
            score -= 2
        elif choiceInput.upper() == "BOULDER" and CPUchoice == "Scissors": #Boulder vs. Scissors
            if BoulderForm == 0: #Base Form
                print("You played Boulder, and the CPU played Scissors. You CRITICALLY win!")
                playsound(critical_dmg)
                randomEvent = random.randint(1, 4)
                if randomEvent == 1: #25% to turn cracked
                    print("However, your Boulder became cracked! It can now break if used again.")
                    playsound(activation)
                    BoulderForm = 1
            elif BoulderForm == 1: #Cracked Form
                print("You played a cracked Boulder, and the CPU played Scissors. You CRITICALLY win!")
                playsound(critical_dmg)
                print("Your Boulder is now broken and reverts back to Rock.")
                playsound(activation)
                userWeapons.remove("BOULDER") #Remove Boulder from the user's hand weapons
                userWeapons.append("ROCK") #Add Rock back into the user's hand weapons
                newWeapons.append("GEODE") #Add Geode back into the pool
                newWeapons.append("BOULDER") #Add Boulder back into the pool
            CPUHealth -= 2
            score += 6
        elif choiceInput.upper() == "BOULDER" and CPUchoice == "Finger Gun": #Boulder vs. Finger Gun
            if BoulderForm == 0: #Base Form
                print("You played Boulder, and the CPU played Finger Gun. Tie.")
                playsound(tie)
            elif BoulderForm == 1: #Cracked Form
                print("You played a cracked Boulder, and the CPU played Finger Gun. Tie.")
                playsound(tie)
                print("Your Boulder is now broken and reverts back to Rock.")
                playsound(activation)
                userWeapons.remove("BOULDER") #Remove Boulder from the user's hand weapons
                userWeapons.append("ROCK") #Add Rock back into the user's hand weapons
                newWeapons.append("GEODE") #Add Geode back into the pool
                newWeapons.append("BOULDER") #Add Boulder back into the pool
        elif choiceInput.upper() == "BOULDER" and CPUchoice == "Rubber Band Gun": #Boulder vs. Rubber Band Gun
            if BoulderForm == 0: #Base Form
                print("You played Boulder, and the CPU played Rubber Band Gun. You win!")
                playsound(win)
                randomEvent = random.randint(1, 4)
                if randomEvent == 1: #25% to turn cracked
                    print("However, your Boulder became cracked! It can now break if used again.")
                    playsound(activation)
                    BoulderForm = 1
            elif BoulderForm == 1: #Cracked Form
                print("You played a cracked Boulder, and the CPU played Rubber Band Gun. You win!")
                playsound(win)
                print("Your Boulder is now broken and reverts back to Rock.")
                playsound(activation)
                userWeapons.remove("BOULDER") #Remove Boulder from the user's hand weapons
                userWeapons.append("ROCK") #Add Rock back into the user's hand weapons
                newWeapons.append("GEODE") #Add Geode back into the pool
                newWeapons.append("BOULDER") #Add Boulder back into the pool
            CPUHealth -= 1
            score += 3
        elif choiceInput.upper() == "BOULDER" and CPUchoice == "Silent Fox": #Boulder vs. Silent Fox
            if BoulderForm == 0: #Base Form
                print("You played Boulder, and the CPU played Silent Fox. You win!")
                playsound(win)
                randomEvent = random.randint(1, 4)
                if randomEvent == 1: #25% to turn cracked
                    print("However, your Boulder became cracked! It can now break if used again.")
                    playsound(activation)
                    BoulderForm = 1
            elif BoulderForm == 1: #Cracked Form
                print("You played a cracked Boulder, and the CPU played Silent Fox. You win!")
                playsound(win)
                print("Your Boulder is now broken and reverts back to Rock.")
                playsound(activation)
                userWeapons.remove("BOULDER") #Remove Boulder from the user's hand weapons
                userWeapons.append("ROCK") #Add Rock back into the user's hand weapons
                newWeapons.append("GEODE") #Add Geode back into the pool
                newWeapons.append("BOULDER") #Add Boulder back into the pool
            CPUHealth -= 1
            score += 3
        elif choiceInput.upper() == "BOULDER" and CPUchoice == "Thumbs Up": #Boulder vs. Thumbs Up
            if BoulderForm == 0: #Base Form
                print("You played Boulder, and the CPU played Thumbs Up. You win!")
                playsound(win)
                randomEvent = random.randint(1, 4)
                if randomEvent == 1: #25% to turn cracked
                    print("However, your Boulder became cracked! It can now break if used again.")
                    playsound(activation)
                    BoulderForm = 1
            elif BoulderForm == 1: #Cracked Form
                print("You played a cracked Boulder, and the CPU played Thumbs Up. You win!")
                playsound(win)
                print("Your Boulder is now broken and reverts back to Rock.")
                playsound(activation)
                userWeapons.remove("BOULDER") #Remove Boulder from the user's hand weapons
                userWeapons.append("ROCK") #Add Rock back into the user's hand weapons
                newWeapons.append("GEODE") #Add Geode back into the pool
                newWeapons.append("BOULDER") #Add Boulder back into the pool
            CPUHealth -= 1
            score += 3
        elif choiceInput.upper() == "BOULDER" and CPUchoice == "Telephone": #Boulder vs. Telephone
            if BoulderForm == 0: #Base Form
                print("You played Boulder, and the CPU played Telephone. You win!")
                playsound(win)
                randomEvent = random.randint(1, 4)
                if randomEvent == 1: #25% to turn cracked
                    print("However, your Boulder became cracked! It can now break if used again.")
                    playsound(activation)
                    BoulderForm = 1
            elif BoulderForm == 1: #Cracked Form
                print("You played a cracked Boulder, and the CPU played Telephone. You win!")
                playsound(win)
                print("Your Boulder is now broken and reverts back to Rock.")
                playsound(activation)
                userWeapons.remove("BOULDER") #Remove Boulder from the user's hand weapons
                userWeapons.append("ROCK") #Add Rock back into the user's hand weapons
                newWeapons.append("GEODE") #Add Geode back into the pool
                newWeapons.append("BOULDER") #Add Boulder back into the pool
            CPUHealth -= 1
            score += 3
        elif choiceInput.upper() == "BOULDER" and CPUchoice == "Hook": #Boulder vs. Hook
            if BoulderForm == 0: #Base Form
                if HookActiveCPU == 0: #Ability Not Active
                    print("You played Boulder, and the CPU played Hook. You win! However, the CPU's Hook can now CRITICALLY win for it's next win.")
                    playsound(win)
                    playsound(activation)
                    HookActiveCPU = 1
                elif HookActiveCPU == 1: #Ability Active
                    print("You played Boulder, and the CPU played Hook. You win!")
                    playsound(win)
                randomEvent = random.randint(1, 4)
                if randomEvent == 1: #25% to turn cracked
                    print("However, your Boulder became cracked! It can now break if used again.")
                    playsound(activation)
                    BoulderForm = 1
            elif BoulderForm == 1: #Cracked Form
                if HookActiveCPU == 0: #Ability Not Active
                    print("You played a cracked Boulder, and the CPU played Hook. You win! However, the CPU's Hook can now CRITICALLY win for it's next win.")
                    playsound(win)
                    playsound(activation)
                    HookActiveCPU = 1
                elif HookActiveCPU == 1: #Ability Active
                    print("You played a cracked Boulder, and the CPU played Hook. You win!")
                    playsound(win)
                print("Your Boulder is now broken and reverts back to Rock.")
                playsound(activation)
                userWeapons.remove("BOULDER") #Remove Boulder from the user's hand weapons
                userWeapons.append("ROCK") #Add Rock back into the user's hand weapons
                newWeapons.append("GEODE") #Add Geode back into the pool
                newWeapons.append("BOULDER") #Add Boulder back into the pool
            CPUHealth -= 1
            score += 3
        elif choiceInput.upper() == "BOULDER" and CPUchoice == "Devil Horns": #Boulder vs. Devil Horns
            if BoulderForm == 0: #Base Form
                print("You played Boulder, and the CPU played Devil Horns. Tie.")
                playsound(tie)
                if DevilActive == 0: #Ability Not Active
                    randomEvent = random.randint(1, 2) #50% of Curse
                    if randomEvent == 1: #Curse
                        print("However, your Boulder got cursed by the CPU's Devil Horns! Throughout this game, when you play Boulder again it now has a 25% chance that you'll hurt yourself for 1 damage!")
                        playsound(curse)
                        DevilActive = 1
                        DevilCursedWeapon = choiceInput.upper()
                        DevilHappen = 1
            elif BoulderForm == 1: #Cracked Form
                print("You played a cracked Boulder, and the CPU played Devil Horns. Tie.")
                playsound(tie)
                print("Your Boulder is now broken and reverts back to Rock.")
                playsound(activation)
                userWeapons.remove("BOULDER") #Remove Boulder from the user's hand weapons
                userWeapons.append("ROCK") #Add Rock back into the user's hand weapons
                newWeapons.append("GEODE") #Add Geode back into the pool
                newWeapons.append("BOULDER") #Add Boulder back into the pool
                if DevilActive == 1 and DevilCursedWeapon == "BOULDER": #Removing Curse on Boulder
                    DevilActive = 0
                    DevilCursedWeapon = ""
    
    #Sandpaper Matchups
        elif choiceInput.upper() == "SANDPAPER" and CPUchoice == "Rock": #Sandpaper vs. Rock
            print("You played Sandpaper, and the CPU played Rock. You CRITICALLY win!")
            playsound(critical_dmg)
            CPUHealth -= 2
            score += 6
        elif choiceInput.upper() == "SANDPAPER" and CPUchoice == "Paper": #Sandpaper vs. Paper
            print("You played Sandpaper, and the CPU played Paper. You win!")
            playsound(win)
            CPUHealth -= 1
            score += 3
        elif choiceInput.upper() == "SANDPAPER" and CPUchoice == "Scissors": #Sandpaper vs. Scissors
            print("You played Sandpaper, and the CPU played Scissors. You lost...")
            playsound(lose)
            userHealth -= 1
            score -= 2
        elif choiceInput.upper() == "SANDPAPER" and CPUchoice == "Finger Gun": #Sandpaper vs. Finger Gun
            print("You played Sandpaper, and the CPU played Finger Gun. You lost...")
            playsound(lose)
            userHealth -= 1
            score -= 2
        elif choiceInput.upper() == "SANDPAPER" and CPUchoice == "Rubber Band Gun": #Sandpaper vs. Rubber Band Gun
            print("You played Sandpaper, and the CPU played Rubber Band Gun. You got stunned!")
            playsound(stun)
            UserActiveStun = 1
        elif choiceInput.upper() == "SANDPAPER" and CPUchoice == "Silent Fox": #Sandpaper vs. Silent Fox
            print("You played Sandpaper, and the CPU played Silent Fox. You win!")
            playsound(win)
            CPUHealth -= 1
            score += 3
        elif choiceInput.upper() == "SANDPAPER" and CPUchoice == "Thumbs Up": #Sandpaper vs. Thumbs Up
            print("You played Sandpaper, and the CPU played Thumbs Up. You win!")
            playsound(win)
            CPUHealth -= 1
            score += 3
        elif choiceInput.upper() == "SANDPAPER" and CPUchoice == "Telephone": #Sandpaper vs. Telephone
            randomEvent = random.randint(1, 2) #50% for User Stun
            if randomEvent == 1: #No Stun
                print("You played Sandpaper, and the CPU played Telephone. You lost...")
                playsound(lose)
            elif randomEvent == 2: #Stun
                print("You played Sandpaper, and the CPU played Telephone. You lost and got stunned!")
                playsound(lose)
                playsound(telephoneStun)
                playsound(stun)
                UserActiveStun = 1
            userHealth -= 1
            score -= 2
        elif choiceInput.upper() == "SANDPAPER" and CPUchoice == "Hook": #Sandpaper vs. Hook
            if HookActiveCPU == 0: #Ability Not Active
                print("You played Sandaper, and the CPU played Hook. You win! However, the CPU's Hook can now CRITICALLY win for it's next win.")
                playsound(win)
                playsound(activation)
                HookActiveCPU = 1
            elif HookActiveCPU == 1: #Ability Active
                print("You played Sandaper, and the CPU played Hook. You win!")
                playsound(win)
            CPUHealth -= 1
            score += 3
        elif choiceInput.upper() == "SANDPAPER" and CPUchoice == "Devil Horns": #Sandpaper vs. Devil Horns
            print("You played Sandpaper, and the CPU played Devil Horns. Tie.")
            playsound(tie)
            if DevilActive == 0: #Ability Not Active
                randomEvent = random.randint(1, 2) #50% of Curse
                if randomEvent == 1: #Curse
                    print("However, your Sandpaper got cursed by the CPU's Devil Horns! Throughout this game, when you play Sandpaper again it now has a 25% chance that you'll hurt yourself for 1 damage!")
                    playsound(curse)
                    DevilActive = 1
                    DevilCursedWeapon = choiceInput.upper()
                    DevilHappen = 1
    
    #Aluminum Foil Matchups
        elif choiceInput.upper() == "ALUMINUM FOIL" and CPUchoice == "Rock": #Aluminum Foil vs. Rock
            print("You played Aluminum Foil, and the CPU played Rock. You win!")
            playsound(win)
            CPUHealth -= 1
            score += 3
        elif choiceInput.upper() == "ALUMINUM FOIL" and CPUchoice == "Paper": #Aluminum Foil vs. Paper
            print("You played Aluminum Foil, and the CPU played Paper. You win!")
            playsound(win)
            CPUHealth -= 1
            score += 3
        elif choiceInput.upper() == "ALUMINUM FOIL" and CPUchoice == "Scissors": #Aluminum Foil vs. Scissors
            print("You played Aluminum Foil, and the CPU played Scissors. You lost...")
            playsound(lose)
            userHealth -= 1
            score -= 2
        elif choiceInput.upper() == "ALUMINUM FOIL" and CPUchoice == "Finger Gun": #Aluminum Foil vs. Finger Gun
            print("You played Aluminum Foil, and the CPU played Finger Gun. Tie.")
            playsound(tie)
        elif choiceInput.upper() == "ALUMINUM FOIL" and CPUchoice == "Rubber Band Gun": #Aluminum Foil vs. Rubber Band Gun
            print("You played Aluminum Foil, and the CPU played Rubber Band Gun. You reflected the shot and stunned the CPU!")
            playsound(deflect)
            playsound(stun)
            CPUActiveStun = 1
        elif choiceInput.upper() == "ALUMINUM FOIL" and CPUchoice == "Silent Fox": #Aluminum Foil vs. Silent Fox
            print("You played Aluminum Foil, and the CPU played Silent Fox. Tie.")
            playsound(tie)
        elif choiceInput.upper() == "ALUMINUM FOIL" and CPUchoice == "Thumbs Up": #Aluminum Foil vs. Thumbs Up
            print("You played Aluminum Foil, and the CPU played Thumbs Up. Tie, but the CPU heals 1 HP.")
            playsound(tie)
            playsound(heal)
            CPUHealth += 1
        elif choiceInput.upper() == "ALUMINUM FOIL" and CPUchoice == "Telephone": #Aluminum Foil vs. Telephone
            print("You played Aluminum Foil, and the CPU played Telephone. You win!")
            playsound(win)
            CPUHealth -= 1
            score += 3
        elif choiceInput.upper() == "ALUMINUM FOIL" and CPUchoice == "Hook": #Aluminum Foil vs. Hook
            if HookActiveCPU == 0: #Ability Not Active
                print("You played Aluminum Foil, and the CPU played Hook. You lost...")
                playsound(lose)
                userHealth -= 1
                score -= 2
            elif HookActiveCPU == 1: #Ability Active
                print("You played Aluminum Foil, and the CPU played Hook. You CRITICALLY lost... The CPU's Hook now reverts back to regular wins.")
                playsound(critical_dmg)
                playsound(activation)
                HookActiveCPU = 0
                userHealth -= 2
                score -= 3
        elif choiceInput.upper() == "ALUMINUM FOIL" and CPUchoice == "Devil Horns": #Aluminum Foil vs. Devil Horns
            print("You played Aluminum Foil, and the CPU played Devil Horns. You lost...")
            playsound(lose)
            userHealth -= 1
            score -= 2
    
    #Claw Matchups
        elif choiceInput.upper() == "CLAW" and CPUchoice == "Rock": #Claw vs. Rock
            print("You played Claw, and the CPU played Rock. You CRITICALLY lost... Owchie!")
            playsound(critical_dmg)
            userHealth -= 2
            score -= 3
        elif choiceInput.upper() == "CLAW" and CPUchoice == "Paper": #Claw vs. Paper
            print("You played Claw, and the CPU played Paper. You win!")
            playsound(win)
            CPUHealth -= 1
            score += 3
        elif choiceInput.upper() == "CLAW" and CPUchoice == "Scissors": #Claw vs. Scissors
            print("You played Claw, and the CPU played Scissors. You win!")
            playsound(win)
            CPUHealth -= 1
            score += 3
        elif choiceInput.upper() == "CLAW" and CPUchoice == "Finger Gun": #Claw vs. Finger Gun 
            print("You played Claw, and the CPU played Finger Gun. You win!")
            playsound(win)
            CPUHealth -= 1
            score += 3
        elif choiceInput.upper() == "CLAW" and CPUchoice == "Rubber Band Gun": #Claw vs. Rubber Band Gun
            print("You played Claw, and the CPU played Rubber Band Gun. You win!")
            playsound(win)
            CPUHealth -= 1
            score += 3
        elif choiceInput.upper() == "CLAW" and CPUchoice == "Silent Fox": #Claw vs. Silent Fox
            print("You played Claw, and the CPU played Silent Fox. You win!")
            playsound(win)
            CPUHealth -= 1
            score += 3
        elif choiceInput.upper() == "CLAW" and CPUchoice == "Thumbs Up": #Claw vs. Thumbs Up
            print("You played Claw, and the CPU played Thumbs Up. You win!")
            playsound(win)
            CPUHealth -= 1
            score += 3
        elif choiceInput.upper() == "CLAW" and CPUchoice == "Telephone": #Claw vs. Telephone
            randomEvent = random.randint(1, 2) #50% for User Stun
            if randomEvent == 1: #No Stun
                print("You played Claw, and the CPU played Telephone. You CRITICALLY lost... Owchie!")
                playsound(critical_dmg)
            elif randomEvent == 2: #Stun
                print("You played Claw, and the CPU played Telephone. You CRITICALLY lost and got stunned!")
                playsound(critical_dmg)
                playsound(telephoneStun)
                playsound(stun)
                UserActiveStun = 1
            userHealth -= 2
            score -= 3
        elif choiceInput.upper() == "CLAW" and CPUchoice == "Hook": #Claw vs. Hook
            print("You played Claw, and the CPU played Hook. Tie.")
            playsound(tie)
        elif choiceInput.upper() == "CLAW" and CPUchoice == "Devil Horns": #Claw vs. Devil Horns
            print("You played Claw, and the CPU played Devil Horns. You win!")
            playsound(win)
            CPUHealth -= 1
            score += 3
    
    #Paper Shredder Matchups
        elif choiceInput.upper() == "PAPER SHREDDER" and CPUchoice == "Rock": #Paper Shredder vs. Rock
            if PaperShredderForm == 0:
                print("You played Paper Shredder, and the CPU played Rock. You lost...")
                playsound(lose)
                randomEvent = random.randint(1, 10)
                if randomEvent == 1: #10% of being Jammed
                    print("Also, your Paper Shredder became jammed! It is now useless for the duration of this game match.")
                    playsound(activation)
                    PaperShredderForm = 1
            elif PaperShredderForm == 1:
                print("You played a jammed Paper Shredder, and the CPU played Rock. You lost...")
                playsound(lose)
            userHealth -= 1
            score -= 2
        elif choiceInput.upper() == "PAPER SHREDDER" and CPUchoice == "Paper": #Paper Shredder vs. Paper
            if PaperShredderForm == 0:
                print("You played Paper Shredder, and the CPU played Paper. You MEGA CRITICALLY win!")
                playsound(mega_critical)
                CPUHealth -= 3
                score += 9
            elif PaperShredderForm == 1:
                print("You played a jammed Paper Shredder, and the CPU played Paper. You lost...")
                playsound(lose)
                userHealth -= 1
                score -= 2
        elif choiceInput.upper() == "PAPER SHREDDER" and CPUchoice == "Scissors": #Paper Shredder vs. Scissors
            if PaperShredderForm == 0:
                print("You played Paper Shredder, and the CPU played Scissors. You win!")
                playsound(win)
                CPUHealth -= 1
                score += 3
                randomEvent = random.randint(1, 10)
                if randomEvent == 1: #10% of being Jammed
                    print("However, your Paper Shredder became jammed! It is now useless for the duration of this game match.")
                    playsound(activation)
                    PaperShredderForm = 1
            elif PaperShredderForm == 1:
                print("You played a jammed Paper Shredder, and the CPU played Scissors. You lost...")
                playsound(lose)
                userHealth -= 1
                score -= 2
        elif choiceInput.upper() == "PAPER SHREDDER" and CPUchoice == "Finger Gun": #Paper Shredder vs. Finger Gun 
            if PaperShredderForm == 0:
                print("You played Paper Shredder, and the CPU played Finger Gun. You lost...")
            elif PaperShredderForm == 1:
                print("You played a jammed Paper Shredder, and the CPU played Finger Gun. You lost...")
            playsound(lose)
            userHealth -= 1
            score -= 2
        elif choiceInput.upper() == "PAPER SHREDDER" and CPUchoice == "Rubber Band Gun": #Paper Shredder vs. Rubber Band Gun
            if PaperShredderForm == 0:
                print("You played Paper Shredder, and the CPU played Rubber Band Gun. You got stunned!")
            elif PaperShredderForm == 1:
                print("You played a jammed Paper Shredder, and the CPU played Rubber Band Gun. You got stunned!")
            playsound(stun)
            UserActiveStun = 1
        elif choiceInput.upper() == "PAPER SHREDDER" and CPUchoice == "Silent Fox": #Paper Shredder vs. Silent Fox
            if PaperShredderForm == 0:
                print("You played Paper Shredder, and the CPU played Silent Fox. Tie.")
                playsound(tie)
            elif PaperShredderForm == 1:
                print("You played a jammed Paper Shredder, and the CPU played Silent Fox. You lost...")
                playsound(lose)
                userHealth -= 1
                score -= 2
        elif choiceInput.upper() == "PAPER SHREDDER" and CPUchoice == "Thumbs Up": #Paper Shredder vs. Thumbs Up
            if PaperShredderForm == 0:
                print("You played Paper Shredder, and the CPU played Thumbs Up. You win!")
                playsound(win)
                CPUHealth -= 1
                score += 3
                randomEvent = random.randint(1, 10)
                if randomEvent == 1: #10% of being Jammed
                    print("However, your Paper Shredder became jammed! It is now useless for the duration of this game match.")
                    playsound(activation)
                    PaperShredderForm = 1
            elif PaperShredderForm == 1:
                print("You played a jammed Paper Shredder, and the CPU played Thumbs Up. You lost...")
                playsound(lose)
                userHealth -= 1
                score -= 2
        elif choiceInput.upper() == "PAPER SHREDDER" and CPUchoice == "Telephone": #Paper Shredder vs. Telephone
            if PaperShredderForm == 0:
                print("You played Paper Shredder, and the CPU played Telephone. Tie.")
                playsound(tie)
            elif PaperShredderForm == 1:
                randomEvent = random.randint(1, 2) #50% for User Stun
                if randomEvent == 1: #No Stun
                    print("You played a jammed Paper Shredder, and the CPU played Telephone. You lost...")
                    playsound(lose)
                elif randomEvent == 2: #Stun
                    print("You played a jammed Paper Shredder, and the CPU played Telephone. You lost and got stunned!")
                    playsound(lose)
                    playsound(telephoneStun)
                    playsound(stun)
                    UserActiveStun = 1
                userHealth -= 1
                score -= 2
        elif choiceInput.upper() == "PAPER SHREDDER" and CPUchoice == "Hook": #Paper Shredder vs. Hook
            if PaperShredderForm == 0:
                if HookActiveCPU == 0: #Ability Not Active
                    print("You played Paper Shredder, and the CPU played Hook. You lost...")
                    playsound(lose)
                    userHealth -= 1
                    score -= 2
                elif HookActiveCPU == 1: #Ability Active
                    print("You played Paper Shredder, and the CPU played Hook. You CRITICALLY lost... The CPU's Hook now reverts back to regular wins.")
                    playsound(critical_dmg)
                    playsound(activation)
                    HookActiveCPU = 0
                    userHealth -= 2
                    score -= 3
            elif PaperShredderForm == 1:
                if HookActiveCPU == 0: #Ability Not Active
                    print("You played a jammed Paper Shredder, and the CPU played Hook. You lost...")
                    playsound(lose)
                    userHealth -= 1
                    score -= 2
                elif HookActiveCPU == 1: #Ability Active
                    print("You played a jammed Paper Shredder, and the CPU played Hook. You CRITICALLY lost... The CPU's Hook now reverts back to regular wins.")
                    playsound(critical_dmg)
                    playsound(activation)
                    HookActiveCPU = 0
                    userHealth -= 2
                    score -= 3
        elif choiceInput.upper() == "PAPER SHREDDER" and CPUchoice == "Devil Horns": #Paper Shredder vs. Devil Horns
            if PaperShredderForm == 0:
                print("You played Paper Shredder, and the CPU played Devil Horns. Tie.")
                playsound(tie)
                if DevilActive == 0: #Ability Not Active
                    randomEvent = random.randint(1, 2) #50% of Curse
                    if randomEvent == 1: #Curse
                        print("However, your Paper Shredder got cursed by the CPU's Devil Horns! Throughout this game, when you play Paper Shredder again it now has a 25% chance that you'll hurt yourself for 1 damage!")
                        playsound(curse)
                        DevilActive = 1
                        DevilCursedWeapon = choiceInput.upper()
                        DevilHappen = 1
            elif PaperShredderForm == 1:
                print("You played a jammed Paper Shredder, and the CPU played Devil Horns. You lost...")
                playsound(lose)
                userHealth -= 1
                score -= 2

    #Finger Gun Matchups
        elif choiceInput.upper() == "FINGER GUN" and CPUchoice == "Rock": #Finger Gun vs. Rock
            print("You played Finger Gun, and the CPU played Rock. You win!")
            playsound(win)
            CPUHealth -= 1
            score += 3
        elif choiceInput.upper() == "FINGER GUN" and CPUchoice == "Paper": #Finger Gun vs. Paper
            print("You played Finger Gun, and the CPU played Paper. You CRITICALLY win!")
            playsound(critical_dmg)
            CPUHealth -= 2
            score += 6
        elif choiceInput.upper() == "FINGER GUN" and CPUchoice == "Scissors": #Finger Gun vs. Scissors
            randomEvent = random.randint(1, 2) #50% of Tie
            if randomEvent == 1: #Win
                print("You played Finger Gun, and the CPU played Scissors. The CPU tried to deflect the attack, but you win!")
                playsound(win)
                CPUHealth -= 1
                score += 3
            elif randomEvent == 2: #Tie
                print("You played Finger Gun, and the CPU played Scissors. The CPU deflected the attack, tie!")
                playsound(deflect)
        elif choiceInput.upper() == "FINGER GUN" and CPUchoice == "Finger Gun": #Finger Gun vs. Finger Gun 
            print("You played Finger Gun, and the CPU played Finger Gun. Tie.")
            playsound(tie)
        elif choiceInput.upper() == "FINGER GUN" and CPUchoice == "Rubber Band Gun": #Finger Gun vs. Rubber Band Gun
            print("You played Finger Gun, and the CPU played Rubber Band Gun. You got stunned!")
            playsound(stun)
            UserActiveStun = 1
        elif choiceInput.upper() == "FINGER GUN" and CPUchoice == "Silent Fox": #Finger Gun vs. Silent Fox
            if SilentActive == 0: #No Disabled Weapon
                randomEvent = random.randint(1, 2) #50% for User Disable
                if randomEvent == 1: #Disable
                    print("You played Finger Gun, and the CPU played Silent Fox. You win! However, Silent Fox disabled your Finger Gun for two rounds!")
                    playsound(win)
                    playsound(disable)
                    SilentDisabledWeapon = choiceInput.upper()
                    userWeapons.remove(SilentDisabledWeapon)
                    SilentActive = 1
                else:
                    print("You played Finger Gun, and the CPU played Silent Fox. You win!")
                    playsound(win)
            else:
                print("You played Finger Gun, and the CPU played Silent Fox. You win!")
                playsound(win)
            CPUHealth -= 1
            score += 3
        elif choiceInput.upper() == "FINGER GUN" and CPUchoice == "Thumbs Up": #Finger Gun vs. Thumbs Up
            print("You played Finger Gun, and the CPU played Thumbs Up. Tie, but the CPU heals 1 HP.")
            playsound(tie)
            playsound(heal)
            CPUHealth += 1
        elif choiceInput.upper() == "FINGER GUN" and CPUchoice == "Telephone": #Finger Gun vs. Telephone
            randomEvent = random.randint(1, 2) #50% for User Stun
            if randomEvent == 1: #No Stun
                print("You played Finger Gun, and the CPU played Telephone. You lost...")
                playsound(lose)
            elif randomEvent == 2: #Stun
                print("You played Finger Gun, and the CPU played Telephone. You lost and got stunned!")
                playsound(lose)
                playsound(telephoneStun)
                playsound(stun)
                UserActiveStun = 1
            userHealth -= 1
            score -= 2
        elif choiceInput.upper() == "FINGER GUN" and CPUchoice == "Hook": #Finger Gun vs. Hook
            if HookActiveCPU == 0: #Ability Not Active
                print("You played Finger Gun, and the CPU played Hook. You lost...")
                playsound(lose)
                userHealth -= 1
                score -= 2
            elif HookActiveCPU == 1: #Ability Active
                print("You played Finger Gun, and the CPU played Hook. You CRITICALLY lost... The CPU's Hook now reverts back to regular wins.")
                playsound(critical_dmg)
                playsound(activation)
                HookActiveCPU = 0
                userHealth -= 2
                score -= 3
        elif choiceInput.upper() == "FINGER GUN" and CPUchoice == "Devil Horns": #Finger Gun vs. Devil Horns
            print("You played Finger Gun, and the CPU played Devil Horns. You win!")
            playsound(win)
            CPUHealth -= 1
            score += 3

    #Gunslinger Matchups
        elif choiceInput.upper() == "GUNSLINGER" and CPUchoice == "Rock": #Gunslinger vs. Rock
            randomEvent = random.randint(1, 2) #50% of Tie
            if randomEvent == 1: #Lose
                print("You played Gunslinger, and the CPU played Rock. You tried to deflect the attack, but you lost...")
                playsound(lose)
                userHealth -= 1
                score -= 2
            elif randomEvent == 2: #Tie
                print("You played Gunslinger, and the CPU played Rock. You deflected the attack, tie!")
                playsound(deflect)
        elif choiceInput.upper() == "GUNSLINGER" and CPUchoice == "Paper": #Gunslinger vs. Paper
            print("You played Gunslinger, and the CPU played Paper. You CRITICALLY win!")
            playsound(critical_dmg)
            CPUHealth -= 2
            score += 6
        elif choiceInput.upper() == "GUNSLINGER" and CPUchoice == "Scissors": #Gunslinger vs. Scissors
            randomEvent = random.randint(1, 2) #50% of Tie
            if randomEvent == 1: #Win
                print("You played Gunslinger, and the CPU played Scissors. The CPU tried to deflect the attack, but you win!")
                playsound(win)
                CPUHealth -= 1
                score += 3
            elif randomEvent == 2: #Tie
                print("You played Gunslinger, and the CPU played Scissors. The CPU deflected the attack, tie!")
                playsound(deflect)
        elif choiceInput.upper() == "GUNSLINGER" and CPUchoice == "Finger Gun": #Gunslinger vs. Finger Gun 
            print("You played Gunslinger, and the CPU played Finger Gun...")
            time.sleep(1.5)
            print("\nReady...")
            playsound(ding)
            print("Set...")
            playsound(ding)
            print("Draw!")
            playsound(shot)
            randomEvent = random.randint(1, 2) #50% of Win / Lose
            if randomEvent == 1: #Win
                print("\nYou win!")
                playsound(win)
                CPUHealth -= 1
                score += 3
            elif randomEvent == 2: #Lose
                print("\nYou lost...")
                playsound(lose)
                userHealth -= 1
                score -= 2
        elif choiceInput.upper() == "GUNSLINGER" and CPUchoice == "Rubber Band Gun": #Gunslinger vs. Rubber Band Gun
            print("You played Gunslinger, and the CPU played Rubber Band Gun. You got stunned!")
            playsound(stun)
            UserActiveStun = 1
        elif choiceInput.upper() == "GUNSLINGER" and CPUchoice == "Silent Fox": #Gunslinger vs. Silent Fox
            print("You played Gunslinger, and the CPU played Silent Fox. You CRITICALLY win!")
            playsound(critical_dmg)
            CPUHealth -= 2
            score += 6
        elif choiceInput.upper() == "GUNSLINGER" and CPUchoice == "Thumbs Up": #Gunslinger vs. Thumbs Up
            print("You played Gunslinger, and the CPU played Thumbs Up. You win!")
            playsound(win)
            CPUHealth -= 1
            score += 3
        elif choiceInput.upper() == "GUNSLINGER" and CPUchoice == "Telephone": #Gunslinger vs. Telephone
            randomEvent = random.randint(1, 2) #50% for User Stun
            if randomEvent == 1: #No Stun
                print("You played Gunslinger, and the CPU played Telephone. You lost...")
                playsound(lose)
            elif randomEvent == 2: #Stun
                print("You played Gunslinger, and the CPU played Telephone. You lost and got stunned!")
                playsound(lose)
                playsound(telephoneStun)
                playsound(stun)
                UserActiveStun = 1
            userHealth -= 1
            score -= 2
        elif choiceInput.upper() == "GUNSLINGER" and CPUchoice == "Hook": #Gunslinger vs. Hook
            print("You played Gunslinger, and the CPU played Hook. Tie.")
            playsound(tie)
        elif choiceInput.upper() == "GUNSLINGER" and CPUchoice == "Devil Horns": #Gunslinger vs. Devil Horns
            print("You played Gunslinger, and the CPU played Devil Horns. Tie.")
            playsound(tie)
            if DevilActive == 0: #Ability Not Active
                randomEvent = random.randint(1, 2) #50% of Curse
                if randomEvent == 1: #Curse
                    print("However, your Gunslinger got cursed by the CPU's Devil Horns! Throughout this game, when you play Gunslinger again it now has a 25% chance that you'll hurt yourself for 1 damage!")
                    playsound(curse)
                    DevilActive = 1
                    DevilCursedWeapon = choiceInput.upper()
                    DevilHappen = 1

    #Thumbs Up Matchups
        elif choiceInput.upper() == "THUMBS UP" and CPUchoice == "Rock": #Thumbs Up vs. Rock
            print("You played Thumbs Up, and the CPU played Rock. Tie, but you heal 1 HP!")
            playsound(tie)
            playsound(heal)
            userHealth += 1
        elif choiceInput.upper() == "THUMBS UP" and CPUchoice == "Paper": #Thumbs Up vs. Paper
            print("You played Thumbs Up, and the CPU played Paper. You lost...")
            playsound(lose)
            userHealth -= 1
            score -= 2
        elif choiceInput.upper() == "THUMBS UP" and CPUchoice == "Scissors": #Thumbs Up vs. Scissors
            print("You played Thumbs Up, and the CPU played Scissors. You lost...")
            playsound(lose)
            userHealth -= 1
            score -= 2
        elif choiceInput.upper() == "THUMBS UP" and CPUchoice == "Finger Gun": #Thumbs Up vs. Finger Gun 
            print("You played Thumbs Up, and the CPU played Finger Gun. Tie, but you heal 1 HP!")
            playsound(tie)
            playsound(heal)
            userHealth += 1
        elif choiceInput.upper() == "THUMBS UP" and CPUchoice == "Rubber Band Gun": #Thumbs Up vs. Rubber Band Gun
            print("You played Thumbs Up, and the CPU played Rubber Band Gun. You got stunned!")
            playsound(stun)
            UserActiveStun = 1
        elif choiceInput.upper() == "THUMBS UP" and CPUchoice == "Silent Fox": #Thumbs Up vs. Silent Fox
            print("You played Thumbs Up, and the CPU played Silent Fox. You lost...")
            playsound(lose)
            userHealth -= 1
            score -= 2
        elif choiceInput.upper() == "THUMBS UP" and CPUchoice == "Thumbs Up": #Thumbs Up vs. Thumbs Up
            print("You played Thumbs Up, and the CPU played Thumbs Up. Tie, but you and the CPU heal 1 HP!")
            playsound(tie)
            playsound(heal)
            playsound(heal)
            userHealth += 1
            CPUHealth += 1
        elif choiceInput.upper() == "THUMBS UP" and CPUchoice == "Telephone": #Thumbs Up vs. Telephone
            print("You played Thumbs Up, and the CPU played Telephone. Tie, but you heal 1 HP!")
            playsound(tie)
            playsound(heal)
            userHealth += 1
        elif choiceInput.upper() == "THUMBS UP" and CPUchoice == "Hook": #Thumbs Up vs. Hook
            print("You played Thumbs Up, and the CPU played Hook. Tie, but you heal 1 HP!")
            playsound(tie)
            playsound(heal)
            userHealth += 1
        elif choiceInput.upper() == "THUMBS UP" and CPUchoice == "Devil Horns": #Thumbs vs. Devil Horns
            print("You played Thumbs Up, and the CPU played Devil Horns. You lost...")
            playsound(lose)
            userHealth -= 1
            score -= 2
    
    #Thumbs Down Matchup
        elif choiceInput.upper() == "THUMBS DOWN" and CPUchoice == "Rock": #Thumbs Down vs. Rock
            randomEvent = random.randint(1, 2) #50% for DMG and Heal
            if randomEvent == 1:
                print("You played Thumbs Down, and the CPU played Rock. Tie, but you deal 1 damage to the CPU and you heal 1 HP!")
                playsound(tie)
                playsound(win)
                playsound(heal)
                CPUHealth -= 1
                userHealth += 1
                score += 1
            elif randomEvent == 2:
                print("You played Thumbs Down, and the CPU played Rock. Tie.")
                playsound(tie)
        elif choiceInput.upper() == "THUMBS DOWN" and CPUchoice == "Paper": #Thumbs Down vs. Paper
            print("You played Thumbs Down, and the CPU played Paper. You win!")
            playsound(win)
            CPUHealth -= 1
            score += 3
        elif choiceInput.upper() == "THUMBS DOWN" and CPUchoice == "Scissors": #Thumbs Down vs. Scissors
            print("You played Thumbs Down, and the CPU played Scissors. You lost...")
            playsound(lose)
            userHealth -= 1
            score -= 2
        elif choiceInput.upper() == "THUMBS DOWN" and CPUchoice == "Finger Gun": #Thumbs Down vs. Finger Gun 
            randomEvent = random.randint(1, 2) #50% for DMG
            if randomEvent == 1:
                print("You played Thumbs Down, and the CPU played Finger Gun. Tie, but you deal 1 damage to the CPU and heal 1 HP!")
                playsound(tie)
                playsound(win)
                playsound(heal)
                CPUHealth -= 1
                userHealth += 1
                score += 1
            elif randomEvent == 2:
                print("You played Thumbs Down, and the CPU played Finger Gun. Tie.")
                playsound(tie)
        elif choiceInput.upper() == "THUMBS DOWN" and CPUchoice == "Rubber Band Gun": #Thumbs Down vs. Rubber Band Gun
            print("You played Thumbs Down, and the CPU played Rubber Band Gun. You got stunned!")
            playsound(stun)
            UserActiveStun = 1
        elif choiceInput.upper() == "THUMBS DOWN" and CPUchoice == "Silent Fox": #Thumbs Down vs. Silent Fox
            randomEvent = random.randint(1, 2) #50% for DMG
            if randomEvent == 1:
                print("You played Thumbs Down, and the CPU played Silent Fox. Tie, but you deal 1 damage to the CPU and heal 1 HP!")
                playsound(tie)
                playsound(win)
                playsound(heal)
                CPUHealth -= 1
                userHealth += 1
                score += 1
            elif randomEvent == 2:
                print("You played Thumbs Down, and the CPU played Silent Fox. Tie.")
                playsound(tie)
        elif choiceInput.upper() == "THUMBS DOWN" and CPUchoice == "Thumbs Up": #Thumbs Down vs. Thumbs Up
            print("You played Thumbs Down, and the CPU played Thumbs Up. You lost...")
            playsound(lose)
            userHealth -= 1
            score -= 2
        elif choiceInput.upper() == "THUMBS DOWN" and CPUchoice == "Telephone": #Thumbs Down vs. Telephone
            print("You played Thumbs Down, and the CPU played Telephone. You win!")
            playsound(win)
            CPUHealth -= 1
            score += 3
        elif choiceInput.upper() == "THUMBS DOWN" and CPUchoice == "Hook": #Thumbs Down vs. Hook
            randomEvent = random.randint(1, 2) #50% for DMG
            if randomEvent == 1:
                print("You played Thumbs Down, and the CPU played Hook. Tie, but you deal 1 damage to the CPU and heal 1 HP!")
                playsound(tie)
                playsound(win)
                playsound(heal)
                CPUHealth -= 1
                userHealth += 1
                score += 1
            elif randomEvent == 2:
                print("You played Thumbs Down, and the CPU played Hook. Tie.")
                playsound(tie)
        elif choiceInput.upper() == "THUMBS DOWN" and CPUchoice == "Devil Horns": #Thumbs Down vs. Devil Horns
            print("You played Thumbs Down, and the CPU played Devil Horns. You win!")
            playsound(win)
            CPUHealth -= 1
            score += 3
    
    #Telephone Matchup
        elif choiceInput.upper() == "TELEPHONE" and CPUchoice == "Rock": #Telephone vs. Rock
            print("You played Telephone, and the CPU played Rock. You lost...")
            playsound(lose)
            userHealth -= 1
            score -= 2
        elif choiceInput.upper() == "TELEPHONE" and CPUchoice == "Paper": #Telephone vs. Paper
            print("You played Telephone, and the CPU played Paper. Tie.")
            playsound(tie)
        elif choiceInput.upper() == "TELEPHONE" and CPUchoice == "Scissors": #Telephone vs. Scissors
            randomEvent = random.randint(1, 2) #50% for CPU Stun
            if randomEvent == 1: #No Stun
                print("You played Telephone, and the CPU played Scissors. You win!")
                playsound(win)
            elif randomEvent == 2: #Stun
                print("You played Telephone, and the CPU played Scissors. You win and stunned the CPU!")
                playsound(win)
                playsound(telephoneStun)
                playsound(stun)
                CPUActiveStun = 1
            CPUHealth -= 1
            score += 3
        elif choiceInput.upper() == "TELEPHONE" and CPUchoice == "Finger Gun": #Telephone vs. Finger Gun 
            randomEvent = random.randint(1, 2) #50% for CPU Stun
            if randomEvent == 1: #No Stun
                print("You played Telephone, and the CPU played Finger Gun. You win!")
                playsound(win)
            elif randomEvent == 2: #Stun
                print("You played Telephone, and the CPU played Finger Gun. You win and stunned the CPU!")
                playsound(win)
                playsound(telephoneStun)
                playsound(stun)
                CPUActiveStun = 1
            CPUHealth -= 1
            score += 3
        elif choiceInput.upper() == "TELEPHONE" and CPUchoice == "Rubber Band Gun": #Telephone vs. Rubber Band Gun
            print("You played Telephone, and the CPU played Rubber Band Gun. You got stunned!")
            playsound(stun)
            UserActiveStun = 1
        elif choiceInput.upper() == "TELEPHONE" and CPUchoice == "Silent Fox": #Telephone vs. Silent Fox
            print("You played Telephone, and the CPU played Silent Fox. You CRITICALLY lost... Owchie!")
            playsound(critical_dmg)
            userHealth -= 2
            score -= 3
        elif choiceInput.upper() == "TELEPHONE" and CPUchoice == "Thumbs Up": #Telephone vs. Thumbs Up
            print("You played Telephone, and the CPU played Thumbs Up. Tie, but the CPU heals 1 HP.")
            playsound(tie)
            playsound(heal)
            CPUHealth += 1
        elif choiceInput.upper() == "TELEPHONE" and CPUchoice == "Telephone": #Telephone vs. Telephone
            print("You played Telephone, and the CPU played Telephone. Tie.")
            playsound(tie)
        elif choiceInput.upper() == "TELEPHONE" and CPUchoice == "Hook": #Telephone vs. Hook 
            randomEvent = random.randint(1, 2) #50% for CPU Stun
            if randomEvent == 1 and HookActiveCPU == 0: #No Stun and Ability Not Active
                print("You played Telephone, and the CPU played Hook. You win! But, the CPU's Hook will now CRITICALLY win for it's next win!")
                playsound(win)
                playsound(activation)
                HookActiveCPU = 1
            elif randomEvent == 2 and HookActiveCPU == 0: #Stun and Ability Not Active
                print("You played Telephone, and the CPU played Hook. You win and stunned the CPU! But, the CPU's Hook will now CRITICALLY win for it's next win!")
                playsound(win)
                playsound(telephoneStun)
                playsound(stun)
                playsound(activation)
                CPUActiveStun = 1
                HookActiveCPU = 1
            elif randomEvent == 1 and HookActiveCPU == 1: #No Stun and Ability Active
                print("You played Telephone, and the CPU played Hook. You win!")
                playsound(win)
            elif randomEvent == 2 and HookActiveCPU == 1: #Stun and Ability Active
                print("You played Telephone, and the CPU played Hook. You win and stunned the CPU!")
                playsound(win)
                playsound(telephoneStun)
                playsound(stun)
                CPUActiveStun = 1
            CPUHealth -= 1
            score += 3
        elif choiceInput.upper() == "TELEPHONE" and CPUchoice == "Devil Horns": #Telephone vs. Devil Horns
            print("You played Telephone, and the CPU played Devil Horns. You lost...")
            playsound(lose)
            userHealth -= 1
            score -= 2

    #Remote Matchup
        elif choiceInput.upper() == "REMOTE" and CPUchoice == "Rock": #Remote vs. Rock
            if RemoteActive == 0: #No Disabled Hand Weapon
                randomEvent = random.randint(1, 3) #33% for CPU Hand Weapon Disable
                if randomEvent == 1: #Disable
                    print("You played Remote, and the CPU played Rock. You CRITICALLY lost... But Remote disabled the CPU's Rock for five rounds!")
                    playsound(critical_dmg)
                    playsound(disable)
                    RemoteDisabledWeapon = CPUchoice
                    CPUWeapons.remove(RemoteDisabledWeapon)
                    RemoteActive = 1
                else: #No Disable
                    print("You played Remote, and the CPU played Rock. You CRITICALLY lost... Owchie!")
                    playsound(critical_dmg)
            elif RemoteActive == 1: #Disabled Hand Weapon Active
                print("You played Remote, and the CPU played Rock. You CRITICALLY lost... Owchie!")
                playsound(critical_dmg)
            userHealth -= 2
            score -= 3
        elif choiceInput.upper() == "REMOTE" and CPUchoice == "Paper": #Remote vs. Paper
            if RemoteActive == 0: #No Disabled Hand Weapon
                randomEvent = random.randint(1, 3) #33% for CPU Hand Weapon Disable
                if randomEvent == 1: #Disable
                    print("You played Remote, and the CPU played Paper. Tie, but Remote disabled the CPU's Paper for five rounds!")
                    playsound(tie)
                    playsound(disable)
                    RemoteDisabledWeapon = CPUchoice
                    CPUWeapons.remove(RemoteDisabledWeapon)
                    RemoteActive = 1
                else: #No Disable
                    print("You played Remote, and the CPU played Paper. Tie.")
                    playsound(tie)
            elif RemoteActive == 1: #Disabled Hand Weapon Active
                print("You played Remote, and the CPU played Paper. Tie.")
                playsound(tie)
        elif choiceInput.upper() == "REMOTE" and CPUchoice == "Scissors": #Remote vs. Scissors
            if RemoteActive == 0: #No Disabled Hand Weapon
                randomEvent = random.randint(1, 3) #33% for CPU Hand Weapon Disable
                if randomEvent == 1: #Disable
                    print("You played Remote, and the CPU played Scissors. You win and disabled the CPU's Scissors for five rounds!")
                    playsound(win)
                    playsound(disable)
                    RemoteDisabledWeapon = CPUchoice
                    CPUWeapons.remove(RemoteDisabledWeapon)
                    RemoteActive = 1
                else: #No Disable
                    print("You played Remote, and the CPU played Scissors. You win!")
                    playsound(win)
            elif RemoteActive == 1: #Disabled Hand Weapon Active
                print("You played Remote, and the CPU played Scissors. You win!")
                playsound(win)
            CPUHealth -= 1
            score += 3
        elif choiceInput.upper() == "REMOTE" and CPUchoice == "Finger Gun": #Remote vs. Finger Gun 
            if RemoteActive == 0: #No Disabled Hand Weapon
                randomEvent = random.randint(1, 3) #33% for CPU Hand Weapon Disable
                if randomEvent == 1: #Disable
                    print("You played Remote, and the CPU played Finger Gun. You win and disabled the CPU's Finger Gun for five rounds!")
                    playsound(win)
                    playsound(disable)
                    RemoteDisabledWeapon = CPUchoice
                    CPUWeapons.remove(RemoteDisabledWeapon)
                    RemoteActive = 1
                else: #No Disable
                    print("You played Remote, and the CPU played Finger Gun. You win!")
                    playsound(win)
            elif RemoteActive == 1: #Disabled Hand Weapon Active
                print("You played Remote, and the CPU played Finger Gun. You win!")
                playsound(win)
            CPUHealth -= 1
            score += 3
        elif choiceInput.upper() == "REMOTE" and CPUchoice == "Rubber Band Gun": #Remote vs. Rubber Band Gun
            if RemoteActive == 0: #No Disabled Hand Weapon
                randomEvent = random.randint(1, 3) #33% for CPU Hand Weapon Disable
                if randomEvent == 1: #Disable
                    print("You played Remote, and the CPU played Rubber Band Gun. You got stunned, but Remote disabled the CPU's Rubber Band Gun for five rounds!")
                    playsound(stun)
                    playsound(disable)
                    RemoteDisabledWeapon = CPUchoice
                    CPUWeapons.remove(RemoteDisabledWeapon)
                    RemoteActive = 1
                else: #No Disable
                    print("You played Remote, and the CPU played Rubber Band Gun. You got stunned!")
                    playsound(stun)
            elif RemoteActive == 1: #Disabled Hand Weapon Active
                print("You played Remote, and the CPU played Rubber Band Gun. You got stunned!")
                playsound(stun)
            UserActiveStun = 1
        elif choiceInput.upper() == "REMOTE" and CPUchoice == "Silent Fox": #Remote vs. Silent Fox
            if RemoteActive == 0: #No Disabled Hand Weapon
                randomEvent = random.randint(1, 3) #33% for CPU Hand Weapon Disable
                if randomEvent == 1: #Disable
                    print("You played Remote, and the CPU played Silent Fox. Tie, but Remote disabled the CPU's Silent Fox for five rounds!")
                    playsound(tie)
                    playsound(disable)
                    RemoteDisabledWeapon = CPUchoice
                    CPUWeapons.remove(RemoteDisabledWeapon)
                    RemoteActive = 1
                else: #No Disable
                    print("You played Remote, and the CPU played Silent Fox. Tie.")
                    playsound(tie)
            elif RemoteActive == 1: #Disabled Hand Weapon Active
                print("You played Remote, and the CPU played Silent Fox. Tie.")
                playsound(tie)
        elif choiceInput.upper() == "REMOTE" and CPUchoice == "Thumbs Up": #Remote vs. Thumbs Up
            if RemoteActive == 0: #No Disabled Hand Weapon
                randomEvent = random.randint(1, 3) #33% for CPU Hand Weapon Disable
                if randomEvent == 1: #Disable
                    print("You played Remote, and the CPU played Thumbs Up. You lost... But Remote disabled the CPU's Thumbs Up for five rounds!")
                    playsound(lose)
                    playsound(disable)
                    RemoteDisabledWeapon = CPUchoice
                    CPUWeapons.remove(RemoteDisabledWeapon)
                    RemoteActive = 1
                else: #No Disable
                    print("You played Remote, and the CPU played Thumbs Up. You lost...")
                    playsound(lose)
            elif RemoteActive == 1: #Disabled Hand Weapon Active
                print("You played Remote, and the CPU played Thumbs Up. You lost...")
                playsound(lose)
            userHealth -= 1
            score -= 2
        elif choiceInput.upper() == "REMOTE" and CPUchoice == "Telephone": #Remote vs. Telephone
            if RemoteActive == 0: #No Disabled Hand Weapon
                randomEvent = random.randint(1, 3) #33% for CPU Hand Weapon Disable
                if randomEvent == 1: #Disable
                    print("You played Remote, and the CPU played Telephone. You win and disabled the CPU's Telephone for five rounds!")
                    playsound(win)
                    playsound(disable)
                    RemoteDisabledWeapon = CPUchoice
                    CPUWeapons.remove(RemoteDisabledWeapon)
                    RemoteActive = 1
                else: #No Disable
                    print("You played Remote, and the CPU played Telephone. You win!")
                    playsound(win)
            elif RemoteActive == 1: #Disabled Hand Weapon Active
                print("You played Remote, and the CPU played Telephone. You win!")
                playsound(win)
            CPUHealth -= 1
            score += 3
        elif choiceInput.upper() == "REMOTE" and CPUchoice == "Hook": #Remote vs. Hook
            if RemoteActive == 0: #No Disabled Hand Weapon
                randomEvent = random.randint(1, 3) #33% for CPU Hand Weapon Disable
                if randomEvent == 1: #Disable
                    print("You played Remote, and the CPU played Hook. Tie, but Remote disabled the CPU's Hook for five rounds!")
                    playsound(tie)
                    playsound(disable)
                    RemoteDisabledWeapon = CPUchoice
                    CPUWeapons.remove(RemoteDisabledWeapon)
                    RemoteActive = 1
                else: #No Disable
                    print("You played Remote, and the CPU played Hook. Tie.")
                    playsound(tie)
            elif RemoteActive == 1: #Disabled Hand Weapon Active
                print("You played Remote, and the CPU played Hook. Tie.")
                playsound(tie)
        elif choiceInput.upper() == "REMOTE" and CPUchoice == "Devil Horns": #Remote vs. Devil Horns
            if RemoteActive == 0: #No Disabled Hand Weapon
                randomEvent = random.randint(1, 3) #33% for CPU Hand Weapon Disable
                if randomEvent == 1: #Disable
                    print("You played Remote, and the CPU played Devil Horns. You win and disabled the CPU's Devil Horns for five rounds!")
                    playsound(win)
                    playsound(disable)
                    RemoteDisabledWeapon = CPUchoice
                    CPUWeapons.remove(RemoteDisabledWeapon)
                    RemoteActive = 1
                else: #No Disable
                    print("You played Remote, and the CPU played Devil Horns. You win!")
                    playsound(win)
            elif RemoteActive == 1: #Disabled Hand Weapon Active
                print("You played Remote, and the CPU played Devil Horns. You win!")
                playsound(win)
            CPUHealth -= 1
            score += 3
    
    #Hook Matchups
        elif choiceInput.upper() == "HOOK" and CPUchoice == "Rock": #Hook vs. Rock
            if HookActiveUser == 0: #Ability Not Active
                print("You played Hook, and the CPU played Rock. You win!")
                playsound(win)
                CPUHealth -= 1
                score += 3
            elif HookActiveUser == 1: #Ability Active
                print("You played Hook, and the CPU played Rock. You CRITICALLY win! Your Hook now reverts back to regular wins.")
                playsound(critical_dmg)
                playsound(activation)
                HookActiveUser = 0
                CPUHealth -= 2
                score += 6
        elif choiceInput.upper() == "HOOK" and CPUchoice == "Paper": #Hook vs. Paper
            if HookActiveUser == 0: #Ability Not Active
                print("You played Hook, and the CPU played Paper. You lost... But, your Hook will now CRITICALLY win for it's next win!")
                playsound(lose)
                playsound(activation)
                HookActiveUser = 1
            elif HookActiveUser == 1: #Ability Active
                print("You played Hook, and the CPU played Paper. You lost...")
                playsound(lose)
            userHealth -= 1
            score -= 2
        elif choiceInput.upper() == "HOOK" and CPUchoice == "Scissors": #Hook vs. Scissors
            print("You played Hook, and the CPU played Scissors. Tie.")
            playsound(tie)
        elif choiceInput.upper() == "HOOK" and CPUchoice == "Finger Gun": #Hook vs. Finger Gun 
            if HookActiveUser == 0: #Ability Not Active
                print("You played Hook, and the CPU played Finger Gun. You win!")
                playsound(win)
                CPUHealth -= 1
                score += 3
            elif HookActiveUser == 1: #Ability Active
                print("You played Hook, and the CPU played Finger Gun. You CRITICALLY win! Your Hook now reverts back to regular wins.")
                playsound(critical_dmg)
                playsound(activation)
                HookActiveUser = 0
                CPUHealth -= 2
                score += 6
        elif choiceInput.upper() == "HOOK" and CPUchoice == "Rubber Band Gun": #Hook vs. Rubber Band Gun
            print("You played Hook, and the CPU played Rubber Band Gun. You got stunned!")
            playsound(stun)
            UserActiveStun = 1
        elif choiceInput.upper() == "HOOK" and CPUchoice == "Silent Fox": #Hook vs. Silent Fox
            if SilentActive == 0: #No Disabled Weapon
                randomEvent = random.randint(1, 2) #50% for User Disable
                if randomEvent == 1 and HookActiveUser == 0: #Disable and Ability Not Active
                    print("You played Hook, and the CPU played Silent Fox. You win! However, Silent Fox disabled your Hook for two rounds!")
                    playsound(win)
                    playsound(disable)
                    SilentDisabledWeapon = choiceInput.upper()
                    userWeapons.remove(SilentDisabledWeapon)
                    SilentActive = 1
                    CPUHealth -= 1
                    score += 3
                elif randomEvent == 1 and HookActiveUser == 1: #Disable and Ability Active
                    print("You played Hook, and the CPU played Silent Fox. You CRITICALLY win! Your Hook reverts back to regular wins. However, Silent Fox disabled your Hook for two rounds!")
                    playsound(critical_dmg)
                    playsound(activation)
                    playsound(disable)
                    SilentDisabledWeapon = choiceInput.upper()
                    userWeapons.remove(SilentDisabledWeapon)
                    SilentActive = 1
                    HookActiveUser = 0
                    CPUHealth -= 2
                    score += 6
                else: #No Disable
                    if HookActiveUser == 0: #Ability Not Active
                        print("You played Hook, and the CPU played Silent Fox. You win!")
                        playsound(win)
                        CPUHealth -= 1
                        score += 3
                    elif HookActiveUser == 1: #Ability Active
                        print("You played Hook, and the CPU played Silent Fox. You CRITICALLY win! Your Hook now reverts back to regular wins.")
                        playsound(critical_dmg)
                        playsound(activation)
                        HookActiveUser = 0
                        CPUHealth -= 2
                        score += 6
            else: #Disabled Weapon
                if HookActiveUser == 0: #Ability Not Active
                    print("You played Hook, and the CPU played Silent Fox. You win!")
                    playsound(win)
                    CPUHealth -= 1
                    score += 3
                elif HookActiveUser == 1: #Ability Active
                    print("You played Hook, and the CPU played Silent Fox. You CRITICALLY win! Your Hook now reverts back to regular wins.")
                    playsound(critical_dmg)
                    playsound(activation)
                    HookActiveUser = 0
                    CPUHealth -= 2
                    score += 6
        elif choiceInput.upper() == "HOOK" and CPUchoice == "Thumbs Up": #Hook vs. Thumbs Up
            print("You played Hook, and the CPU played Thumbs Up. Tie, but the CPU heals 1 HP.")
            playsound(tie)
            playsound(heal)
            CPUHealth += 1
        elif choiceInput.upper() == "HOOK" and CPUchoice == "Telephone": #Hook vs. Telephone
            randomEvent = random.randint(1, 2) #50% for User Stun
            if randomEvent == 1 and HookActiveUser == 0: #No Stun and Ability Not Active
                print("You played Hook, and the CPU played Telephone. You lost... But, your Hook will now CRITICALLY win for it's next win!")
                playsound(lose)
                playsound(activation)
                HookActiveUser = 1
            elif randomEvent == 2 and HookActiveUser == 0: #Stun and Ability Not Active
                print("You played Hook, and the CPU played Telephone. You lost and got stunned! But, your Hook will now CRITICALLY win for it's next win!")
                playsound(lose)
                playsound(telephoneStun)
                playsound(stun)
                playsound(activation)
                UserActiveStun = 1
                HookActiveUser = 1
            elif randomEvent == 1 and HookActiveUser == 1: #No Stun and Ability Active
                print("You played Hook, and the CPU played Telephone. You lost...")
                playsound(lose)
            elif randomEvent == 2 and HookActiveUser == 1: #Stun and Ability Active
                print("You played Hook, and the CPU played Telephone. You lost and got stunned!")
                playsound(lose)
                playsound(telephoneStun)
                playsound(stun)
                UserActiveStun = 1
            userHealth -= 1
            score -= 2
        elif choiceInput.upper() == "HOOK" and CPUchoice == "Hook": #Hook vs. Hook
            print("You played Hook, and the CPU played Hook. Tie.")
            playsound(tie)
        elif choiceInput.upper() == "HOOK" and CPUchoice == "Devil Horns": #Hook vs. Devil Horns
            print("You played Hook, and the CPU played Devil Horns. Tie.")
            playsound(tie)
            if DevilActive == 0: #Ability Not Active
                randomEvent = random.randint(1, 2) #50% of Curse
                if randomEvent == 1: #Curse
                    print("However, your Hook got cursed by the CPU's Devil Horns! Throughout this game, when you play Hook again it now has a 25% chance that you'll hurt yourself for 1 damage!")
                    playsound(curse)
                    DevilActive = 1
                    DevilCursedWeapon = choiceInput.upper()
                    DevilHappen = 1

    #Harpoon Matchups
        elif choiceInput.upper() == "HARPOON" and CPUchoice == "Rock": #Harpoon vs. Rock
            if HarpoonActive == 0: #Ability Not Active
                print("You played Harpoon, and the CPU played Rock. Tie.")
                playsound(tie)
            elif HarpoonActive == 1: #Ability Active
                print("You played Harpoon, and the CPU played Rock. Tie, and your Harpoon now reverts back to regular wins.")
                playsound(tie)
                playsound(activation)
                HarpoonActive = 0
        elif choiceInput.upper() == "HARPOON" and CPUchoice == "Paper": #Harpoon vs. Paper
            if HarpoonActive == 0: #Ability Not Active
                print("You played Harpoon, and the CPU played Paper. You win!")
                playsound(win)
                CPUHealth -= 1
                score += 3
            elif HarpoonActive == 1: #Ability Active
                print("You played Harpoon, and the CPU played Paper. You MEGA CRITICALLY win! Your Harpoon now reverts back to regular wins.")
                playsound(mega_critical)
                playsound(activation)
                HarpoonActive = 0
                CPUHealth -= 3
                score += 9
        elif choiceInput.upper() == "HARPOON" and CPUchoice == "Scissors": #Harpoon vs. Scissors
            if HarpoonActive == 0: #Ability Not Active
                print("You played Harpoon, and the CPU played Scissors. You lost... But, your Harpoon will now MEGA CRITICALLY win for it's next win!")
                playsound(lose)
                playsound(activation)
                HarpoonActive = 1
            elif HarpoonActive == 1: #Ability Active
                print("You played Harpoon, and the CPU played Scissors. You lost...")
                playsound(lose)
            userHealth -= 1
            score -= 2
        elif choiceInput.upper() == "HARPOON" and CPUchoice == "Finger Gun": #Harpoon vs. Finger Gun 
            if HarpoonActive == 0: #Ability Not Active
                print("You played Harpoon, and the CPU played Finger Gun. You win!")
                playsound(win)
                CPUHealth -= 1
                score += 3
            elif HarpoonActive == 1: #Ability Active
                print("You played Harpoon, and the CPU played Finger Gun. You MEGA CRITICALLY win! Your Harpoon now reverts back to regular wins.")
                playsound(mega_critical)
                playsound(activation)
                HarpoonActive = 0
                CPUHealth -= 3
                score += 9
        elif choiceInput.upper() == "HARPOON" and CPUchoice == "Rubber Band Gun": #Harpoon vs. Rubber Band Gun
            print("You played Harpoon, and the CPU played Rubber Band Gun. You got stunned!")
            playsound(stun)
            UserActiveStun = 1
        elif choiceInput.upper() == "HARPOON" and CPUchoice == "Silent Fox": #Harpoon vs. Silent Fox
            if HarpoonActive == 0: #Ability Not Active
                print("You played Harpoon, and the CPU played Silent Fox. You win!")
                playsound(win)
                CPUHealth -= 1
                score += 3
            elif HarpoonActive == 1: #Ability Active
                print("You played Harpoon, and the CPU played Silent Fox. You MEGA CRITICALLY win! Your Harpoon now reverts back to regular wins.")
                playsound(mega_critical)
                playsound(activation)
                HarpoonActive = 0
                CPUHealth -= 3
                score += 9
        elif choiceInput.upper() == "HARPOON" and CPUchoice == "Thumbs Up": #Hook vs. Thumbs Up
            if HarpoonActive == 0: #Ability Not Active
                print("You played Harpoon, and the CPU played Thumbs Up. You win!")
                playsound(win)
                CPUHealth -= 1
                score += 3
            elif HarpoonActive == 1: #Ability Active
                print("You played Harpoon, and the CPU played Thumbs Up. You MEGA CRITICALLY win! Your Harpoon now reverts back to regular wins.")
                playsound(mega_critical)
                playsound(activation)
                HarpoonActive = 0
                CPUHealth -= 3
                score += 9
        elif choiceInput.upper() == "HARPOON" and CPUchoice == "Telephone": #Hook vs. Telephone
            if HarpoonActive == 0: #Ability Not Active
                print("You played Harpoon, and the CPU played Telephone. Tie.")
                playsound(tie)
            elif HarpoonActive == 1: #Ability Active
                print("You played Harpoon, and the CPU played Telephone. Tie, and your Harpoon now reverts back to regular wins.")
                playsound(tie)
                playsound(activation)
                HarpoonActive = 0
        elif choiceInput.upper() == "HARPOON" and CPUchoice == "Hook": #Hook vs. Hook
            if HookActiveCPU == 0: #CPU Ability Not Active
                if HarpoonActive == 0: #Ability Not Active
                    print("You played Harpoon, and the CPU played Hook. You lost... But, your Harpoon will now MEGA CRITICALLY win for it's next win!")
                    playsound(lose)
                    playsound(activation)
                    HarpoonActive = 1
                elif HarpoonActive == 1: #Ability Active
                    print("You played Harpoon, and the CPU played Hook. You lost...")
                    playsound(lose)
                userHealth -= 1
                score -= 2
            elif HookActiveCPU == 1: #CPU Ability Active
                if HarpoonActive == 0: #Ability Not Active
                    print("You played Harpoon, and the CPU played Hook. You CRITICALLY lost... But, your Harpoon will now MEGA CRITICALLY win for it's next win! The CPU's Hook now reverts back to regular wins.")
                    playsound(critical_dmg)
                    playsound(activation)
                    HarpoonActive = 1
                elif HarpoonActive == 1: #Ability Active
                    print("You played Harpoon, and the CPU played Hook. You CRITICALLY lost... Owchie! The CPU's Hook now reverts back to regular wins.")
                    playsound(critical_dmg)
                HookActiveCPU = 0
                userHealth -= 2
                score -= 3
        elif choiceInput.upper() == "HARPOON" and CPUchoice == "Devil Horns": #Harpoon vs. Devil Horns
            if HarpoonActive == 0: #Ability Not Active
                print("You played Harpoon, and the CPU played Devil Horns. You win!")
                playsound(win)
                CPUHealth -= 1
                score += 3
            elif HarpoonActive == 1: #Ability Active
                print("You played Harpoon, and the CPU played Devil Horns. You MEGA CRITICALLY win! Your Harpoon now reverts back to regular wins.")
                playsound(mega_critical)
                playsound(activation)
                HarpoonActive = 0
                CPUHealth -= 3
                score += 9

    if "BOULDER" in userWeapons and BoulderForm == 1: #Check If User Didn't Play Boulder Again
        if previousInput.upper() == "BOULDER" and choiceInput.upper() != "BOULDER":
            print("Your Boulder has recovered from it's crack! It can be used regularly again!")
            playsound(activation)
            BoulderForm = 0
    
    if SilentActive == 1: #Check If Silent Fox's Disable Ability Works or Not
        if SilentActiveRounds == 2: #Two rounds has passed
            print("Your " + SilentDisabledWeapon.capitalize() + " isn't disabled anymore!")
            playsound(disable_off)
            SilentActive = 0
            SilentActiveRounds = 0
            userWeapons.append(SilentDisabledWeapon)
            SilentDisabledWeapon = ""
        else:
            SilentActiveRounds += 1

    if RemoteActive == 1: #Check If Remote's Disable Ability Works or Not
        if RemoteActiveRounds == 5: #Five rounds has passed
            print("The CPU's " + RemoteDisabledWeapon + " isn't disabled anymore!")
            playsound(disable_off)
            RemoteActive = 0
            RemoteActiveRounds = 0
            CPUWeapons.append(RemoteDisabledWeapon)
            RemoteDisabledWeapon = ""
        else:
            RemoteActiveRounds += 1
    
    if DevilActive == 1 and DevilHappen == 0: #Check If Devil Horns' Curse Ability Works or Not
        if choiceInput.upper() == DevilCursedWeapon.upper(): #Check if user's hand weapon played is cursed
            randomEvent = random.randint(1, 4) #25% of Self Damage
            if randomEvent == 1: #Damage
                print("The curse embedded in your " + choiceInput.capitalize() + " has dealt 1 damage to you!")
                playsound(curse_activate)
                playsound(lose)
                userHealth -= 1
    DevilHappen = 0

    round_num += 1 #Adds 1 to the Rounds
    
    #User and CPU Overhealing Prevention Check
    if CPUHealth > maxCPUHealth:
        CPUHealth = maxCPUHealth
    if userHealth > maxUserHealth:
        userHealth = maxUserHealth
    randomEvent = 0 #Reset random events

#New Hand Weapon for User
def new_User_weapons():
    global score #Only for no more new hand weapons
    
    #Hand Weapon Descriptions
    weapon_descriptions = {
        "GEODE": "Wins: Rock, Scissors, Finger Gun, Devil Horns\nLoses: Paper, Silent Fox, Telephone\nTies: Thumbs Up, Hook\nAbility: Upgrades from Rock. If Geode goes against Rock, Geode is able to win against Paper throughout a game.",
        "BOULDER": "Wins: Rock, Scissors, Rubber Band Gun, Silent Fox, Thumbs Up, Telephone, Hook\nLoses: Paper\nTies: Finger Gun, Devil Horns\nAbility: Upgrades from Rock. Critically wins against Scissors. Whenever this wins against the opponent's hand weapon, this has a 25% chance to crack. If the Boulder is used again while cracked, it reverts back to Rock. Boulder recovers from the crack if it isn't played for one round.",
        "SANDPAPER": "Wins: Rock, Paper, Silent Fox, Thumbs Up, Hook\nLoses: Scissors, Finger Gun, Telephone\nTies: Devil Horns\nAbility: Upgrades from Paper. Critically wins against Rock.",
        "ALUMINUM FOIL": "Wins: Rock, Paper, Telephone\nLoses: Scissors, Hook, Devil Horns\nTies: Finger Gun, Silent Fox, Thumbs Up\nAbility: Upgrades from Paper. This can reflect stuns from the CPU's Rubber Band Gun.",
        "CLAW": "Wins: Paper, Scissors, Finger Gun, Rubber Band Gun, Silent Fox, Thumbs Up, Devil Horns\nLoses: Rock, Telephone\nTies: Hook\nAbility: Upgrades from Scissors. Critically wins when the CPU is stunned. Critically loses against Rock and Telephone.",
        "PAPER SHREDDER": "Wins: Paper, Scissors, Thumbs Up\nLoses: Rock, Finger Gun, Hook\nTies: Silent Fox, Telephone, Devil Horns\nAbility: Upgrades from Scissors. MEGA Critically wins against Paper. When against Rock, Scissors, or Thumbs Up, this has a 10% chance to become jammed and be useless throughout a game.",
        "FINGER GUN": "Wins: Rock, Paper, Scissors, Silent Fox, Devil Horns\nLoses: Telephone, Hook\nTies: Finger Gun, Thumbs Up\nAbility: Critically wins against Paper. Has a 50% chance to tie against Scissors.",
        "GUNSLINGER": "Wins: Paper, Scissors, Finger Gun, Silent Fox, Thumbs Up\nLoses: Rock, Finger Gun, Telephone\nTies: Hook, Devil Horns\nAbility: Upgrades from Finger Gun. Critically wins against Paper and Silent Fox. Has a 50% chance to tie against Rock and Scissors, and either win or lose against Finger Gun.",
        "THUMBS UP": "Wins: None\nLoses: Paper, Scissors, Silent Fox, Devil Horns\nTies: Rock, Finger Gun, Thumbs Up, Telephone, Hook\nAbility: Whenever this ties against the opponent's hand weapon, heal 1 HP to the owner.",
        "THUMBS DOWN": "Wins: Paper, Telephone, Devil Horns\nLoses: Scissors, Thumbs Up\nTies: Rock, Finger Gun, Silent Fox, Hook\nAbility: Upgrades from Thumbs Up. Whenever this ties against the CPU's hand weapon, this has a 50% chance to deal 1 DMG to the CPU and heal 1 HP to you.",
        "TELEPHONE": "Wins: Scissors, Finger Gun, Hook\nLoses: Rock, Silent Fox, Devil Horns\nTies: Paper, Thumbs Up, Telephone\nAbility: Critically loses against Silent Fox. Whenever this wins against the opponent's hand weapon, this has a 50% chance to stun the opponent.",
        "REMOTE": "Wins: Scissors, Finger Gun, Telephone, Devil Horns\nLoses: Rock, Thumbs Up\nTies: Paper, Silent Fox, Hook\nAbility: Upgrades from Telephone. Critically loses against Rock. When this is played this has a 33% chance to disable the opponent's played hand weapon for five rounds. Only one opposing hand weapon can be disabled at a time.",
        "HOOK": "Wins: Rock, Finger Gun, Silent Fox\nLoses: Paper, Telephone\nTies: Scissors, Thumbs Up, Hook, Devil Horns\nAbility: Whenever this loses against the opponent's hand weapon, the next win against the opponent's hand weapon will become a critical win instead. Reverts back to a regular win after the critical win is used.",
        "HARPOON": "Wins: Paper, Finger Gun, Silent Fox, Thumbs Up, Devil Horns\nLoses: Scissors, Hook\nTies: Rock, Telephone\nAbility: Upgrades from Hook. Whenever this loses against the CPU's hand weapon, the next win against the CPU's hand weapon will become a MEGA critical win instead. But, if this ties against the CPU's hand weapon this will lose it's MEGA critical win. Reverts back to a regular win after the MEGA critical win is used or this ties."
    }    

    #New Hand Weapon RNG
    if len(newWeapons) == 0: #No more hand weapons left
        print("No more new hand weapons available. Instead, gain 5 extra points to your score!")
        score += 5
        time.sleep(1.5)
        return
    elif len(newWeapons) >= 3: #At least 3 available hand weapons
        random_offerings = random.sample(newWeapons, 3)
    elif len(newWeapons) == 2: #Only 2 available hand weapons
        random_offerings = random.sample(newWeapons, 2)
    elif len(newWeapons) == 1: #Only 1 available hand weapon left
        random_offerings = random.sample(newWeapons, 1)
    print("Choose your new hand weapon:")
    print("")
    for index, weapon in enumerate(random_offerings):
        print(f"{index+1}. {weapon}")
        if weapon in weapon_descriptions:
            print(f"{weapon_descriptions[weapon]}")
            playsound(gleam)
            print("")
    print("Your current hand weapons: " + str(userWeapons))
    print("")

    #User Input Check
    while True:
        try:
            choice = int(input("Enter a number of your pick: "))
            if 1 <= choice <= len(random_offerings):
                chosen_weapon = random_offerings[choice - 1]
                break
            else:
                print("Invalid choice. Please select a hand weapon from the given options.")
                playsound(invalid)
        except ValueError:
            print("Invalid input. Please enter a number.")
            playsound(invalid)
        print("")

    #Removing future options based on the chosen hand weapon
    if chosen_weapon == "GEODE": #Geode Pick
        newWeapons.remove("BOULDER")
        userWeapons.remove("ROCK")
        playsound(acquire_upgrade)
    elif chosen_weapon == "BOULDER": #Boulder Pick
        newWeapons.remove("GEODE")
        userWeapons.remove("ROCK")
        playsound(acquire_upgrade)
    elif chosen_weapon == "SANDPAPER": #Sandpaper Pick
        newWeapons.remove("ALUMINUM FOIL")
        userWeapons.remove("PAPER")
        playsound(acquire_upgrade)
    elif chosen_weapon == "ALUMINUM FOIL": #Aluminum Foil Pick
        newWeapons.remove("SANDPAPER")
        userWeapons.remove("PAPER")
        playsound(acquire_upgrade)
    elif chosen_weapon == "CLAW": #Claw Pick
        newWeapons.remove("PAPER SHREDDER")
        userWeapons.remove("SCISSORS")
        playsound(acquire_upgrade)
    elif chosen_weapon == "PAPER SHREDDER": #Paper Shredder Pick
        newWeapons.remove("CLAW")
        userWeapons.remove("SCISSORS")
        playsound(acquire_upgrade)
    elif chosen_weapon == "FINGER GUN": #Finger Gun Pick
        newWeapons.append("GUNSLINGER") #Adding the upgrade to Finger Gun
        playsound(acquire_new)
    elif chosen_weapon == "GUNSLINGER": #Gunslinger Pick
        userWeapons.remove("FINGER GUN")
        playsound(acquire_upgrade)
    elif chosen_weapon == "THUMBS UP": #Thumbs Up Pick
        newWeapons.append("THUMBS DOWN") #Adding the upgrade to Thumbs Up
        playsound(acquire_new)
    elif chosen_weapon == "THUMBS DOWN": #Thumbs Down Pick
        userWeapons.remove("THUMBS UP")
        playsound(acquire_upgrade)
    elif chosen_weapon == "TELEPHONE": #Telephone Pick
        newWeapons.append("REMOTE") #Adding the upgrade to Telephone
        playsound(acquire_new)
    elif chosen_weapon == "REMOTE": #Remote Pick
        userWeapons.remove("TELEPHONE")
        playsound(acquire_upgrade)
    elif chosen_weapon == "HOOK": #Hook Pick
        newWeapons.append("HARPOON") #Adding the upgrade to Hook
        playsound(acquire_new)
    elif chosen_weapon == "HARPOON": #Harpoon Pick
        userWeapons.remove("HOOK")
        playsound(acquire_upgrade)
    
    #Add the chosen weapon to the user's hand
    userWeapons.append(chosen_weapon.upper())
    newWeapons.remove(chosen_weapon.upper())

#New weapon for the CPU
def choose_CPU_weapon():
    if len(newCPUWeapons) >= 1: #Available hand weapons
        CPUchoice = random.choice(newCPUWeapons)
        CPUWeapons.append(CPUchoice)
        newCPUWeapons.remove(CPUchoice)
    else: #No more hand weapons left
        return

#Introduction and Instructions
print("Welcome to Rock Paper Scissors Ultra Deluxe, a roguelike twist to the classic 'Rock Paper Scissors' game.")
print("\nFor every game win you do against the CPU, you get to pick between three new different 'hand weapons' to make yourself stronger for the next game. The CPU also gets stronger too through it's new 'hand weapon' pick as well. Note that some 'hand weapons' are exclusive between you and the CPU, so finding the right 'hand weapon' counters will increase your chances of winning. Plus, they each have different interactions and abilities, so make sure to choose wisely!")
print("\nThe goal is for you to win five games without losing, along with getting the highest score possible. You will always start with 10 HP, and the CPU's HP will scale up each game, starting off with 5 HP. Good luck, and have fun!")
print("")
print("Here are the starting hand weapons you will always start and use with:")
print("")
print("1. ROCK\nWins: Scissors, Telephone\nLoses: Paper, Finger Gun, Silent Fox, Hook\nTies: Rock, Thumbs Up, Devil Horns\nAbility: None\n")
print("2. PAPER\nWins: Rock, Thumbs Up, Hook\nLoses: Scissors, Finger Gun, Devil Horns\nTies: Paper, Silent Fox, Telephone\nAbility: Critically loses against Finger Gun.\n")
print("3. SCISSORS\nWins: Paper, Silent Fox, Thumbs Up, Devil Horns\nLoses: Rock, Finger Gun, Telephone\nTies: Scissors, Rubber Band Gun, Hook\nAbility: Critically wins when the CPU is stunned. Has a 50% to tie against Finger Gun.\n")
print("Type 'start' when you are ready to play.")
playsound(meow)
startInput = input()

#Intro User Input Check
while startInput.lower() != "start":
    if startInput.lower() == "start":
        print("")
        print("Alright, let's do this!")
    else:
        print("")
        print("We don't have any other options to select, so just type 'start' whenever you're ready.")
        playsound(invalid)
        startInput = input()

#Games
while game_number <= 5: #Edit how many games User plays
    CPUHealth = game_number * 5 #CPU gains 5 HP per game played
    maxCPUHealth = game_number * 5 #No overhealing, CPU gains 5 max HP per game played
    round_num = 1 #Counting rounds per game.
    playsound(game_start)
    while True:
        print("")
        print("--------------------------------------")
        print("")
        print("Game " + str(game_number) + ", Round " + str(round_num))
        print("Score: " + str(score))
        print("")
        print("Your Health: " + str(userHealth))
        print("CPU Health: " + str(CPUHealth))
        print("")
        print("What is your move?")
        print(userWeapons)

    #User Stun Check and Message
        if UserActiveStun == 1:
            print("You are stunned, your move is skipped.")
            time.sleep(1.5)
        else:

    #User Input Check
            while choiceInput.upper() not in userWeapons:
                choiceInput = input()
                if choiceInput.upper() not in userWeapons:
                    print("")
                    print("That is not one of your hand weapons. Try again.")
                    print(userWeapons)
                    playsound(invalid)
    
    #CPU Weapon Pick
        CPUlength = len(CPUWeapons)
        CPUchoice = CPUWeapons[random.randint(0, CPUlength - 1)]

    #Duel Section
        print("")
        chant()
        logic(choiceInput, CPUchoice)
        previousInput = choiceInput.upper()
        choiceInput = "" #Reset User Choice Inputs
        CPUchoice = "" #Reset CPU Choice Inputs

    #Check HPs
        if userHealth <= 0 and CPUHealth <= 0:
            print("Both you and the CPU has died at the same time... In this case, redo the round again!")
            playsound(invalid)
            userHealth = 1
            CPUHealth = 1
        elif userHealth <= 0:
            print("")
            print("--------------------------------------")
            print("")
            print("Game Over.")
            print("")
            print("Final score: " + str(score))
            print("Your hand weapons: " + str(userWeapons))
            print("")
            playsound(game_over)
            quit()
        elif CPUHealth <= 0:
            break

    #Reset Weapon Activations
    GeodeActive = 0
    BoulderForm = 0
    PaperShredderForm = 0
    if RemoteActive == 1:
        CPUWeapons.append(RemoteDisabledWeapon)
    RemoteActive = 0
    RemoteActiveRounds = 0
    RemoteDisabledWeapon = ""
    HookActiveUser = 0
    HookActiveCPU = 0
    HarpoonActive = 0
    if SilentActive == 1:
        userWeapons.append(SilentDisabledWeapon)
    SilentActive = 0
    SilentActiveRounds = 0
    SilentDisabledWeapon = ""
    DevilActive = 0
    DevilCursedWeapon = ""
    DevilHappen = 0

    print("")
    print("--------------------------------------")
    print("")
    print("You win Game " + str(game_number) + "!")
    game_number += 1
    if game_number <= 5:
        print("Current score: " + str(score))
        playsound(winner)
        if "GEODE" in userWeapons or "BOULDER" in userWeapons or "PAPER SHREDDER" in userWeapons or "REMOTE" in userWeapons or "HOOK" in userWeapons or "HARPOON" in userWeapons:
            print("")
            print("All hand weapon active abilites and forms have been reset!")
            playsound(activation)
        print("")
        print("Now pick your next new hand weapon reward!")
        playsound(new)
        print("")
        new_User_weapons()
        choose_CPU_weapon()
        userHealth = 10 #Full Heal
        print("")
        print("Time for Game " + str(game_number) + "!")
    else:
        print("")
        print("You win Rock Paper Scissors Ultra Deluxe!! Congrats!!")
        print("")
        print("Final score: " + str(score))
        print("Your hand weapons: " + str(userWeapons))
        playsound(good_game)
        quit()