"""input = input(">")
while input.upper() == 'HELP':
    print('start - to start the car')
    print('stop - to stop the car')
    print('quit - to exit')
    break # dont forget to write it to stop the indefinite loop
if input.upper() == 'START'
    print('Car started...Ready to go!')
if input.upper() == 'STOP'
    print('Car stopped')
if input.upper() == 'QUIT'"""
#answer:
#command = "" #defining empty command of the user
"""command.lower() != 'quit': #we want to run this code till the user type quit.
    command = input("> ")
    if command.lower() == 'start':
        print("Car started...")
    elif command.lower() == 'stop':
        print("Car stopped")"""
command = ""
while True: # instead of next hash condition the loop will be executed till break#command != 'quit':  # we want to run this code till the user type quit.
    command = input("> ").lower()
    if command == 'start':
        print("Car started...")
    elif command == 'stop':
        print("Car stopped")
    elif command == 'help':
        print("""
start - to start the car
stop - to stop the car
quit - to exit
            """)
    elif command == 'quit': # written to delete the next message when quitting
        break
    else:
        print("Sorry, I don't understand that!")

