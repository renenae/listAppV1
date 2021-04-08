"""

Program Goals:
1. Get the input from the usser!
2. Convert that input to an INT
3. Add that input to a list
4. Pull values from specific index positions
"""

#create functions that will perfrom those actions above
import random
myList = []
unique_list = []

def mainProgram():
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
            if choice == "1":
                addToList()
            elif choice == "2":
                returnValue()
            elif choice == "3":
                addABunch()
            elif choice == "4":
                randomSearch(myList)
            elif choice == "5":
                linearSearch()
            elif choice == "6":
                sortList()
            elif choice == "7":
                printLists()
            elif choice == "8":
                searchItem = input("What are you looking for?  ")
                recursiveBinarySearch(unique_list, 0, len(unique_list)-1, int(searchItem))
                
            else:
                break
        except:
            print("An error ocurred")
    
def addToList():
    newItem = input("Please type an integer!   ")
    myList.append(int(newItem))
    print(myList)

def addABunch():
    print("We're gonna add a bunch of numbers!")
    numToAdd = input ("How many integers do you want to add?   ")
    numRange = input("How high whould you like these numbers to go?   ")
    for x in range(0, int(numToAdd)):
        myList.append(random.randint(0, int(numRange)))
    print("Your list is now complete!")


def sortList(myList):
    for x in myList:
        if x not in unique_list:
            unique_list.append(x)
    unique_list.sort()
    showMe = input("Wanna see your new list? Y/N   ")
    if showMe.lower() == "y":
        print(unique_list)

    
def indexValues():
    indexPos = input("At what index position would you like to look?   ")
    print(myList[int(indexPos)])

def randomSearch():
   print("Here's a random value from your list!")
   print(myList[random.randint(0, len(myList)-1)])

def linearSearch():
    print("We're going to search the list IN THE WORST WAY POSSIBLE!")
    searchItem = input("What are you looking for? Number-wise?   ")
    for x in range (len(myList)):
        if myList [x] == int(searchItem):
            print("Your item is at index {}".format(x))
    print(indexcount)

def recursiveBinarySearch(unique_list, low, high, x):
    if high >= low:
        mid = (high + low) // 2

        if uniqeue_list[mid] ==x:
            print("Oh, what luck. Your number is at position {}".format(mid))
            return mid 
        elif unique_list[mid] > x:
            return recursiveBinarySearch(unique_list, low, mid - 1, x)
        else:
            return recursiveBinarySearch(unique_list, mid + 1, high, x)    
    else:
        print("Your number isn't here!")

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

def indexValues():
    print("At what index position do you want to search?")
    indexPos = input("Type an index position here:  ")
    print (myList[int(indexPos)])




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
