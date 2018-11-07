known_users = ["Harsha","Silpa","Anu","Pavan","Dad","Mom","Khaleel","Vinay"]

while True:
    print("My name is Travis")
    name = input("What is your name?:").strip().capitalize();
    if name in known_users:
        print("Hello {}!".format(name))
        remove = input("Would you like to be removed from the system (y/n)?:").strip().lower();
        if remove == "y":
            known_users.remove(name)
        elif remove == "n"
            print("No problem, I didn't want you to leave anyway!")
    else:
        print("I don't think I have met you yet {}".format(name))
        add_me = input("Would you like to be added to the system (y/s)?:").strip().lower()
        if add_me == "y":
            known_users.append(name)
        elif add_me == "n":
            print("No worries, see you around")
        
    
