# What is the largest prime factor of the number 600851475143 ?

import math

number = 600851475143
print("The largest prime factor of " + str(number) + " is ", end="")
largestFactor = 2

# Once a prime factor is found, keep dividing 'number' by that factor so multiples of that prime factor
# aren't considered during division.
while number % 2 == 0:
    number = number / 2
# All prime numbers other than 2 are odd
for primeFactor in range(3, int(math.sqrt(number)) + 1, 2):
    if number % primeFactor == 0:
        number = number / primeFactor
        largestFactor = primeFactor

print(largestFactor)
