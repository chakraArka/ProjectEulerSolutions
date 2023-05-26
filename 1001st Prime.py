# What is the 10001st prime number?

n = 10001

if n == 1:
    print("The 1st prime number is 2")
elif n == 2:
    print("The 2nd prime number is 3")
elif n == 3:
    print("The 3rd prime number is 5")
else:
    # All prime numbers other than 2 are odd.
    primeList = [3, 5]
    num = 7
    isPrime = True
    while len(primeList) + 1 < n:
        for primeNum in primeList:
            if num % primeNum == 0:
                isPrime = False
                break
        if isPrime:
            primeList.append(num)
        else:
            isPrime = True
        num += 2
    print("The " + str(n) + "th prime number is ", end="")
    print(num - 2)
