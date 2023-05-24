# By considering the terms in the Fibonacci sequence whose values do not exceed four million,
# find the sum of the even-valued terms.

nextFibonacciNumber = 2
prevFibonacciNumber = 1
fibSum = 0
while nextFibonacciNumber <= 4000000:
    temp = nextFibonacciNumber
    nextFibonacciNumber = nextFibonacciNumber + prevFibonacciNumber
    prevFibonacciNumber = temp
    if prevFibonacciNumber % 2 == 0:
        fibSum += prevFibonacciNumber

print("Sum of even-valued terms in Fibonacci sequence (values less than four million)")
print(fibSum)
