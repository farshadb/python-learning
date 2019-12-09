command = ""
state = ""
while True:
    command = input("> ").lower()
    if command == "start" :
        if state == "started":
            print("Car already started ...")
        else:
            print("Car started ...")
            state = "started"
    elif command == "stop":
        if state == "stopped":
            print("Car already stopped ...")
        else:
            print("Car sropped ... ")
            state = "stopped"
    elif command == "help":
        print("""
start - to start the car 
stop - to stop the car 
quit - quit
help - show help        
""")
    elif command == "quit":
        break
    else:
        print("Sorry, I don'nt undrestand that!")