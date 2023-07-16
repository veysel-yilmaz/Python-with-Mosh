#  ???? better to have explanation, it doesnt work!?
command = ""
started = False # added with answer
while True:
    command = input("> ").lower()
    if command == 'start':
        if started:
            print('Car is already started!')
        else:
            started = True # thats how we stop the car
            print("Car started...")# dont forget to add indentation before print to prevent print to be shown in the result, it would be useless to write nested if and else statement.
        """if command == 'start'
            print("Car already started.")"""
    elif command == 'stop':
        if not started: #attention to 'not' here
            print('Car is already stopped!')
        else:
            started = False
            print("Car stopped")
        """if command == 'stop'
            print("Car already stopped.")"""
    elif command == 'help':
        print("""
start - to start the car
stop - to stop the car
quit - to exit
            """)
    elif command == 'quit':
        break
    else:
        print("Sorry, I don't understand that!")
