def factorial(n):
      if n <= 0:
            return 0
      elif n == 1:
            return 1
      else:
            fact = 1
            while(n > 1):
                  fact *= n
                  n -= 1
            return fact

num = input("Please input a number: ")
print("You chose",num)
print("Factorial of", num, "is", factorial(num)) 
print(factorial(num))

#Simple calculator for factorials

#num = 3
#print("Factorial of", num, "is", factorial(num))





 





 