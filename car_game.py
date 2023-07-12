command = ""
started = False
stopped = False
while True :
    command = input("> ")
    if command.upper() == "START":
        if started :
            print("Car is already Started")
        else :
            started = True
        print("Ready to Go....")

    elif command.upper() == "STOP" :
        print("Engine Stopped ")

    elif command.upper() == ("HELP") :
        print("""
Start -> To Go
Stop -> To Stop
Quit -> To Quit
              """)
    elif command.upper() == ("QUIT") :
        break
    else :
        print("I dont undeerstand that. Type Help for assistance")

#This is a car game, run this game in your termianl and type HELP for assistance.