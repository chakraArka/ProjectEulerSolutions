# By considering the terms in the Fibonacci sequence whose values do not exceed four million,
# find the sum of the even-valued terms.

nextFibonacciNumber = 2
prevFibonacciNumber = 1
fibSum = 0
maxValue = 4000000
while nextFibonacciNumber <= maxValue:
    temp = nextFibonacciNumber
    nextFibonacciNumber = nextFibonacciNumber + prevFibonacciNumber
    prevFibonacciNumber = temp
    if prevFibonacciNumber % 2 == 0:
        fibSum += prevFibonacciNumber

print("Sum of even-valued terms in Fibonacci sequence (values less than " + str(maxValue) + ") = ", end="")
print(fibSum)
