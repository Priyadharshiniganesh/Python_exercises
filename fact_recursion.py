# Factorial of a number using recursion - By default, the maximum depth of recursion is 1000

def recur_factorial(n):
   if (n == 1 or n == 0):
       return n
   else:
       return n*recur_factorial(n-1)

num = 5

# check if the number is negative
if num < 0:
   print("does not exist for negative numbers")
else:
   print("The factorial of", num, "is", recur_factorial(num))