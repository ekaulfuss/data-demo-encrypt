"""
Author: Edison Kaulfuss, Corey Bock, Brian Mellino

This Password system will create and save passwords, usernames, and websites using 2 data structures.
First is a simple list that will store the three aforementioned pieces of data.
The second is a map that will store a simplified version of the website name as a key and the list as a value.
I.e. - The key would be "google" whereas "https://accounts.google.com/InteractiveLogin/signinchooser" would be
stored in the list.
Additionally, all data will be encrypted before storage and stored on a local file

"""
import random
import os

# Local Modules

from LoginInfo import LoginInfo

# Imported Modules


# user_dict would be built with {String: LoginInfo Obect}
user_dict = dict()


def main():
    """
    Main function to run the password system.

    :returns: None
    """
    print("Getting everything set up.")
    fillDict()
    while True:
        print("1: Add a new entry.")
        print("2: Look up an entry by its key.")
        print("3: Display all keys.")
        print("4: Save all changes")
        print("5: Exit (Don't forget to save!)")
        choice = input("Please choose an option: ")
        match choice:
            case "1":
                addNew()
            case "2":
                getOne(input("What key are you looking for? "))
            case "3":
                displayKeys()
            case "4":
                saveDict()
            case "5":
                break
            case _:
                print("Invalid selection, please try again.")
        cls()


def addNew():
    """
    Function to add a new entry to the password system.

    :returns: None
    """
    while True:
        easy_key = inputCheck("What is the shorthand key you'd like to use?")
        if easy_key not in user_dict:
            break
        else:
            print("Sorry, that key is already in use. You'll have to choose another. \n"
                  "If you have another login to the same site try adding a number after the name.")
    site = inputCheck("Copy and paste the login site here: ")
    username = inputCheck("What username did you choose? ")
    password = recomender()
    print("The following password has been chosen: " + password)
    cls()
    newLogin = LoginInfo(site, username, password)
    user_dict[easy_key] = newLogin


def inputCheck(query):
    """
    Function to check user input.

    :param query: The query prompt for user input.
    :returns: The validated user input.
    """
    while True:
        returner = input(query)
        if returner:
            break
        else:
            print("Invalid entry, please try again.")
    return returner


def fillDict():
    """
    Function to fill the dictionary from a file.

    :returns: None
    """
    try:
        pwFile = open("info.psd", "r")
        readString = pwFile.read()
        readString = readString.split('||')
        for current in readString:
            workingInfo = LoginInfo()
            current = current.split('|')
            nameHolder = current[0]
            workingInfo.setLoginSite(current[1], False)
            workingInfo.setUsername(current[2], False)
            workingInfo.setPassword(current[3], False)
            user_dict[nameHolder] = workingInfo
        pwFile.close()
    except:
        pass
    finally:
        pass


def saveDict():
    """
    Function to save the dictionary to a file.

    :returns: None
    """
    if len(user_dict) > 0:
        pwFile = open("info.psd", "w")
        for key in user_dict:
            pwFile.write(key + "|" + user_dict[key].dumpForSave())
            if not key == list(user_dict)[-1]:
                pwFile.write("||")
        pwFile.close()


def getOne(thisOne):
    """
    Function to retrieve one entry from the dictionary.

    :param thisOne: The key of the entry to retrieve.
    :returns: None
    """
    if thisOne in user_dict:
        print("Login Info for " + thisOne + "______________________")
        print("Login Site: " + user_dict[thisOne].getLoginSite())
        print("Username: " + user_dict[thisOne].getUsername())
        print("Password: " + user_dict[thisOne].getPassword())
    else:
        print("Login information could not be found using that key.")


def displayKeys():
    """
    Function to display all keys in the dictionary.

    :returns: None
    """
    for key in user_dict:
        print(key)


def recomender():
    """
    Function to generate a potential password.

    :returns: Generated password string.
    """
    returner = ["", "", "", "", "", "", "", "", "", ""]
    pwFrame = []
    while len(pwFrame) < 10:
        r = random.randint(0, 9)
        if r not in pwFrame:
            pwFrame.append(r)
    if random.randint(1, 2) == 1:
        returner[pwFrame[0]] = "!"
    else:
        returner[pwFrame[0]] = "@"
    returner[pwFrame[1]] = str(random.randint(0, 9))
    returner[pwFrame[2]] = chr(random.randint(65, 90))
    returner[pwFrame[3]] = chr(random.randint(97, 122))
    for x in range(4, 9):
        kind = random.randint(1, 3)
        if kind == 1:
            returner[pwFrame[x]] = str(random.randint(0, 9))
        elif kind == 2:
            returner[pwFrame[x]] = chr(random.randint(65, 90))
        elif kind == 3:
            returner[pwFrame[x]] = chr(random.randint(97, 122))
    return "".join(returner)


def cls():
    """
    Function to clear the screen.

    :returns: None
    """
    input("Press Enter to clear the screen and continue.")
    os.system('cls||clear')


if __name__ == "__main__":
    main()
