
def continued():
    while True:
        print("RUNNN")
        print("RUNNN")
        print("RUNNN")
        input("you finally catch up to him. what do you do? ")
def cool():
    while True:
        print("1 = quit, 2 = enter forest, 3 = enter cave")
        path = input("what do you want to do? ")
        if(path == "1"):
            print("okay.. see you later")
            break
        if(path == "2"):
            choice2 = input("You see a gnome. what do you say to him? ")
            if(choice2 != ""):
                print("The gnome steals your stuff. Go after him!")
                continued()
                break
            else:
                print("You have to put something bro")
        if(path == "3"):
            print("1 = Sure, 2 = Nah I'm good")
            choice3 = input("You see a chest. Do you walk towards it? ")
            if(choice3 == "1"):
                print("The chest exploded!! you died")
                break
            if(choice3 == "2"):
                print("you left. coward.")
                continue
        if(path == "4"):
            break
def vault():
    while True:
        passwordinput = input("Please enter the numerical password: ")
        if passwordinput == password:
            print("\033[92mACCESS GRANTED\033[0m\n")
            menu()
            break
        else:
            print("\033[91mACCESS DENIED\033[0m")
def delete_secret():
    secrets = load_secrets()

    if not secrets:
        print("No secrets to delete.")
        return

    print("\n--- DELETE A SECRET ---")
    for i, s in enumerate(secrets, start=1):
        print(f"{i}. {s}")

    choice = input("Which secret do you want to delete? (number) ")

    if not choice.isdigit():
        print("Invalid input.")
        return

    choice = int(choice)

    if 1 <= choice <= len(secrets):
        removed = secrets.pop(choice - 1)
        save_secrets(secrets)
        print(f"Deleted: {removed}")
    else:
        print("That number doesn't exist.")
def save_secrets(secrets):
    with open("secrets.txt", "w") as file:
        for s in secrets:
            file.write(s + "\n")
def menu():
    while True:
        choicevault = input("\n1 = load secrets, 2 = save secrets, 3 = delete a secret\nWhat would you like to do? ")
        if choicevault == "1":
            secrets = load_secrets()
            print("\n--- STORED SECRETS ---")
            if not secrets:
                print("No secrets saved yet.")
            else:
                for s in secrets:
                    print("-", s)
        elif choicevault == "2":
            new_secret = input("Type the secret you want to save: ")
            with open("secrets.txt", "a") as file:
                file.write(new_secret + "\n")
            print("Secret saved!")
        elif(choicevault == "3"):
            delete_secret()


def load_secrets():
    try:
        with open("secrets.txt", "r") as file:
            return [line.strip() for line in file.readlines()]
    except FileNotFoundError:
        return []           

name = input("What is your name? ")
print("Hello " + name + "! What do you want to do?")
x = 0
password = "5754"
while True:
    print("Welcome to the menu screen!")
    print("1 = nothing, 2 = start, 3 = enter vault")
    choice = input("I want to... ")
    if(x > 4):
        print("BRO STOP MESSING WITH THE OPTIONS!!! \nuh oh the game's gonna crash cuz of you!!!")
        break
    if(choice == "1"):
        print("oh ok then")
        break
    elif(choice == "2"):
       print("aight bet")
       cool()
       break
    elif(choice == "3"):
       print("okay sure")
       vault()
       break
    else:
       print("That's not an option lil bro")
       x += 1
