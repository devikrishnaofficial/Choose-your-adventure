name = input("Type your name: ")
print("Welcome", name, "to this adventure!")

answer = input("You are on a dirt road. It has come to an end, and you can go left or right. Which way would you like to go? ").lower()

if answer == "left":
    answer = input("You come to a river. You can walk around it or swim across (swim/walk): ")
    if answer == "swim":
        print("You swam and were eaten by an alligator. Game over!")
    elif answer == "walk":
        print("You walked for many miles, ran out of water, and you lost the game.")
    else:
        print("Not a valid option. You lose.")
elif answer == "right":
    print("You chose to go right.")
    print("As you journey further, you encounter a dense forest blocking your path.")
    print("To proceed, you must find a way through the forest.")
    
    found_path = False
    while not found_path:
        search = input("Would you like to search for a path or try to cut through the forest with your machete? (search/cut): ").lower()
        if search == "search":
            print("After a thorough search, you find a hidden path that leads through the forest.")
            found_path = True
        elif search == "cut":
            print("You try to cut through the forest, but it's too dense. You're forced to turn back.")
        else:
            print("Not a valid option.")
    
    print("You successfully make your way through the forest and continue your journey.")
    print("Finally, after hours of trekking, you find a hidden treasure chest deep in a cave!")
    print("Congratulations, you won the game!")
else:
    print("Not a valid option. You lose.")
