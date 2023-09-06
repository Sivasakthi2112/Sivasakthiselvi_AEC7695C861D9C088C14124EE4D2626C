#1.Implement a recursive function to find the factorial of a number
def fact(n):
  if (n == 1):
    return (1)
  else:
    return (n * fact(n - 1))


m = int(input("Enter the number to check Factorial:"))
print("factorial value:", fact(m))
