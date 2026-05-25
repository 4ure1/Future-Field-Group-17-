




def thinLine ():
    thinLine = print("-"*80)
    return thinLine

def boldLine ():
    boldLine = print("="*80)
    return boldLine

def errorMessage(message):
    (print(f"✗ ERROR : {message}"))

def succesMessage(message):
    (print(f" ✓ SUCCES : {message}"))




def appNameVersion():
    #project name and version
    boldLine()
    print(f" \n PROJECT X verison 1 \n")
    boldLine()
    return appNameVersion

def getChoice(maxchoice):
    while True:
        try:
            choice = int(input("\n  Votre choix : "))
            if 1<= choice <= maxchoice : 
                return choice 
            else :
                print (errorMessage(f"Choose beetwen 1 and {maxchoice}"))
        except ValueError:
            print (errorMessage(f"Entrer une valeur valid"))

def display_menu_options(num,option):
    return f"{num}) {option}"



while True : 
    appNameVersion()
    print("What do you need today")
    display_menu_options(1,"option1")
    display_menu_options(2,"option2")
    display_menu_options(3,"option3")
    choice = getChoice(3)

    if choice == 1:
        print("You choose option1")
    elif choice == 2:
        print("You choose option2")
    elif choice == 3:
        print("You choose option3")
        break



