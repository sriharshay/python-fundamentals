films = {
    "Finding Dory":{"age":3,"seats":5},
    "Bourne":{"age":18, "seats":5},
    "Tarzan":{"age":15, "seats":5},
    "Ghost Busters":{"age":12,"seats":5}
    }
while True:
    choice = input("What film would you like to watch?:").strip().title()

    if choice in films:
        age = int(input("How old are you?:").strip())

        # Check user age
        if age >= films[choice]["age"]:

            # Check enough seats
            if films[choice]["seats"] > 0:
                films[choice]["seats"] = films[choice]["seats"] - 1
                print("Enjoy the film!")
            else:
                print("Sorry, we are sold out!")

        else:
            print("You are too young to watch {}!".format(choice)) 

    else:
        print("We don't have the film...")
