# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.

numDict = {}
for i in range(1, 1001):
    numDict[i] = i ** 2

for a in range(1, 1001):
    for b in range(1, 1001):
        c = 1000 - (a + b)
        if c in numDict:
            cSq = numDict.get(c)
            if a ** 2 + b ** 2 == cSq:
                print("a = " + str(a) + ", b = " + str(b) + ", c = " + str(c))
                print("a*b*c = " + str(a * b * c))
                exit()
