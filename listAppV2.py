"""
Program Goals:
1. Get the input from the usser!
2. Convert that input to an INT
3. Add that input to a list
4. Pull values from specific index positions
"""

#create functions that will perform those actions above
import random
myList = []
unique_list = []


def listTutorial():
        tutChoice = input("Would you like a tutorial? Y/N")
        if tutChoice.lower() == 'y':
                 print("""   Okay then, let's get this started! This app is used to create lists.
To make a list or add to it just press 2 once you enter the main menu!
The next number 2 returns the number you have previously used and displays it for you.
3 adds well, a bunch of random numbers. Random search searches for a number randomly
Linear search searches for a number in a line pattern going one by one through the list.
Sort list sorts through the list. Print lists displays your list. And last but not least Recursive Binary Search,
it searches for things but more efficently and faster!   """)

"""
The code above is what asks the user wehter they want to do the tutorial or not. If they put in "Y" Then the code
starts printing the text above. If they say "N" then the code directly goes to the menu.
"""


def mainProgram():
    listTutorial()
    while True:
        try:
            print("Hello, there! Let's work with lists!")
            print("Choose one of the following options. Type a number ONLY!")
            choice = input("""1. Add to list,
2. Return a value in a list
3. Add a bunch of numbers!
4. Random Search 
5. Linear Search 
6. Sort List 
7. Print Lists
8. Recursive Binary Search
9. Quit   """)

            if choice == "tut":
                listTutorial()
            elif choice == "1":
                addToList()
            elif choice == "2":
                indexValues()
            elif choice == "3":
                addABunch()
            elif choice == "4":
                randomSearch(myList)
            elif choice == "5":
                linearSearch()
            elif choice == "6":
                sortList(myList)    
            elif choice == "7":
                printLists()
            elif choice == "8":
                searchItem = input("What are you looking for?  ")
                recursiveBinarySearch(unique_list, 0, len(unique_list)-1, int(searchItem))
                
            else:
                break
        except:
            print("An error ocurred")
"""
This is the menu and the functions. When the user presses one of the numbers assigned to a function,
the code immediatly executes it and does the action corresponding to it. If something goes wrong,
then it prints "An error occured"
"""

"""
Add to list well makes a new list and adds an integer to it.
"""

def addToList():
    newItem = input("Please type an integer!   ")
    myList.append(int(newItem))
    print(myList)
"""
adds a bunch of numbers -_-
"""

def addABunch():
    print("We're gonna add a bunch of numbers!")
    numToAdd = input ("How many integers do you want to add?   ")
    numRange = input("How high whould you like these numbers to go?   ")
    for x in range(0, int(numToAdd)):
        myList.append(random.randint(0, int(numRange)))
    print("Your list is now complete!")

def multipleIndividuals(y):
        for x in range (y):
                newNum = input("What number do you want to add?   ")
                myList.append(int(newNum))
"""
Checks through your lists
"""
def sortList(myList):
    for x in myList:
        if x not in unique_list:
            unique_list.append(x)
    unique_list.sort()
    showMe = input("Wanna see your new list? Y/N   ")
    if showMe.lower() == "y":
        print(unique_list)

"""
Looks through a specific index position
"""
def indexValues():
    indexPos = input("At what index position would you like to look?   ")
    print(myList[int(indexPos)])
"""
randomly searches and chooses a value from your list
"""
def randomSearch():
   print("Here's a random value from your list!")
   print(myList[random.randint(0, len(myList)-1)])
"""
a bad way of searching for something
"""
def linearSearch():
    print("We're going to search the list IN THE WORST WAY POSSIBLE!")
    searchItem = input("What are you looking for? Number-wise?   ")
    for x in range (len(myList)):
        if myList [x] == int(searchValue):
            print("Your item is at index {}".format(x))
    print(indexcount)
"""
premium way of searching for a value in a list
"""
def recursiveBinarySearch(unique_list, low, high, x):
    if high >= low:
        mid = (high + low) // 2
        if unique_list[mid] == x:
            print("Your number is at position {}".format(mid))
            return mid 
        elif unique_list[mid] > x:
            return recursiveBinarySearch(unique_list, low, mid - 1, x)
        else:
            return recursiveBinarySearch(unique_list, mid + 1, high, x)    
    else:
        print("Your number isn't here!")
"""
recursive binary search but make it spicier
"""
def iterativeBinarySearch(unique_list, x):
    low = 0
    high = len(unique_list)-1
    mid = 0

    while low <= high:
        mid = (high + low) // 2

        if unique_list[mid] < x:
            low = mid + 1
        elif unique_list[mid] > x:
            high = mid - 1
        else:
            return mid
    return -1
"""
lets you choose where you want to look in an index position
"""
def indexValues():
    print("At what index position do you want to search?")
    indexPos = input("Type an index position here:  ")      
    print (myList[int(indexPos)])
"""
shows you your lists
"""
def printLists():
    if len(unique_list) == 0:
        print(myList)
    else:
        whichOne = input("Which list? Sorted or un-sorted?   ")
        if whichOne.lower() == "sorted":
            print(unique_list)
        else:
            print(myList)
            
if __name__ == "__main__":
    mainProgram()
