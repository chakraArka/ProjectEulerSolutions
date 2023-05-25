# Find the largest palindrome made from the product of two 3-digit numbers.

def isPalindrome(x):
    isPal = False
    if str(x) == str(x)[::-1]:
        isPal = True
    return isPal


numOfDigits = 3
minNum = 10 ** (numOfDigits - 1)
maxNum = 10 ** numOfDigits - 1
largestPalindrome = -1

# Find the largest palindrome product amongst all product combinations
while maxNum > minNum:
    for i in range(maxNum, minNum - 1, -1):
        product = i * maxNum
        if isPalindrome(product) and largestPalindrome < product:
            largestPalindrome = product

    maxNum -= 1

print("The largest palindrome product from the product of two " + str(numOfDigits) + "-digit numbers is ", end="")
print(largestPalindrome)
