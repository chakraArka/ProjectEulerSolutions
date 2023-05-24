# What is the smallest positive number that is evenly divisible by all of the numbers
# from 1 to 20?

# Start with the current minimum number = 2,
# since it is common knowledge that 2 is divisible by both 2 and 1.
currMinNum = 2
# nextNum represents the next integer that currMinNum has to be divisible by.
nextNum = 3
while nextNum <= 20:
    temp = currMinNum
    addInt = nextNum - 1
    while(currMinNum % temp != 0 or currMinNum % nextNum != 0):
        currMinNum += addInt
    nextNum += 1
print("Smallest Positive Number that is evenly divisible by all numbers from 1 to 20 :")
print(currMinNum)
