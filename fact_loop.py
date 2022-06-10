#Factorial of a number using for loop and range() function
num=5
factorial = 1
if num < 0:
    print("does not exist for negative numbers")
elif (num == 0):
    print("The factorial of", num, "is", factorial(num))
else:
    for i in range(1,num + 1):
            factorial = factorial*i
    print("The factorial of",num,"is",factorial)
