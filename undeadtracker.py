import d20
#important!
#instald20 https://pypi.org/project/d20/


#class for zombie and skelleton info
class zom:
    hp = 22
    ac = 8
    str = 13
    strmod = 1
    dex = 6
    dexmod = -2
    con = 16
    conmod = 3
    int = 3
    intmod = -4
    wis = 6
    wismod = -2
    cha = 5
    chamod = -3

class skel:
    hp = 13
    ac = 8
    str = 10
    strmod = 0
    dex = 14
    dexmod = 2
    con = 15
    conmod = 2
    int = 6
    intmod = -2
    wis = 8
    wismod = -1
    cha = 5
    chamod = -3



#d20 handler class
def diceroll():
    print("ready to roll?")
    print("enter roll statement")
    roll = input("> ")
    if roll == "exit" or "leave":
        start()
    else:
        print(d20.roll(roll))
        diceroll()
    


#direct command function
def commander():
    print("what do you wish to do?")
    command = input("> ")
    exec(command)
    print("continue?")
    command = input("> ")
    if command == "y" or "yes":
        commander()
    else:
        print("as you wish")

#what do i even want to do?
#create a specified number of undead
#track health
#roll saves, attacks and damage

class undead:
    def initzom(zhorde):
        print("undead still in development")
        looper = 1
        while looper <= zhorde:
            print("loop " + str(looper))
            looper +=1

    def initskel(shorde):
        print("skeleton not done comeback later")

    def init():
        print("how many Zombies?")
        Zhorde = int(input("> "))
        print("how many Skeletons")
        Shorde = int(input("> "))
        print(str(Zhorde) + " zombies and " + str(Shorde) + " skeletons?")
        answer = input("> ")
        if answer == "yes" or "y":
            print("ok")
            undead.revive(Zhorde, Shorde)

        else:
            print("didt get that, start over")
            start()


    def revive(znum, snum):
        print("raising the dead")
        undead.initzom(znum)
        undead.initskel(snum)
        undead.track()

    def track():
        print("not done")





#start

def start():
    print("hello")
    print("what would you like to do?")
    print("a- Roll")
    print("b- raise undead")
    print("c- command")
    print("d- leave")

    choice = input("> ")
    if choice == "a":
        diceroll()
    elif choice == "b":
        undead.init()
    elif choice == "c":
        commander()
    elif choice == "d":
        print("goodbye")
    else:
        print("invalid choice!")
        print("try again")
        start()


#actually start the program
start()
print("program ended")
