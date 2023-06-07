# Q7. Calculate the factorial of a number using lambda function.


factorial = lambda n: 1 if n == 0 else n * factorial(n-1)
#my program able to give only factorial till 997
n = int(input("enter the number you want factorial take number between 1 to 997 only :"))
result = factorial(n)
print(result)