print('''___________                                                   .___           .___.__                      .___
\__    ___/______   ____ _____    ________ _________   ____   |   | ______ __| _/|  | _____    _____    __| _/
  |    |  \_  __ \_/ __ \\__  \  /  ___/  |  \_  __ \_/ __ \  |   |/  ___// __ | |  | \__  \  /     \  / __ | 
  |    |   |  | \/\  ___/ / __ \_\___ \|  |  /|  | \/\  ___/  |   |\___ \/ /_/ | |  |__/ __ \|  Y Y  \/ /_/ | 
  |____|   |__|    \___  >____  /____  >____/ |__|    \___  > |___/____  >____ | |____(____  /__|_|  /\____ | 
                       \/     \/     \/                   \/           \/     \/           \/      \/      \/ ''')


print("Welcome to Treasure Island!")
print("Your mission is to find the treasure.")

choice1 = input("You\'re at a crossroad, where dop you want to go? Type 'left' or 'right'.\n").lower()

if choice1 == "left":
    choice2 = input("You\'ve come to a lake. There is an island in the middle of the lake. Type 'wait' to wait for a boat. Type 'swim' to swim across.\n").lower()
    if choice2 == "wait":
        choice3 = input("You arrive at the island unharmed. There is a house with 3 doors - red, yellow, blue. Which colour do you choose?\n").lower()
        if choice3 == "red":
          print("It's a room full of fire. Gamne Over.")
        elif choice3 == "yellow":
          print("You found the treasure! Congratulations!")
        elif choice3 == "blue":
          print("You enter a room of beasts. Game Over.")
        else:
         print("You chose a door that doesn't exist. Game Over.")
    else:
        print("You swam across and were eaten by an alligator!")
else:
     print("You fell into a hole. Game Over.")