command = ""
while True:
    command = input("> ").lower()
    if command == "start":
        print("Car started ...")
    elif command == "stop":
        print("Car stoped ...")
    elif command == "help":
        print("""
start - to start the car 
stop - to stop the car 
quit - quit        
""")
    elif command == "quit":
        break
    else:
        print("Sorry, I don'nt undrestand that!")