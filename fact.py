def factorial(n):
      if n == 0:
            return 1
      return n * factorial(n-1) #Recursive function used to compute the number

def input_valid(n):
      if n < 0:
            print("Too negative!") #Reminds the user to follow the formula: n>=0 and loop continues
            return False
      elif n > 10:
            print("Too loud! Keep it down!") #Returns a value of "False" when number is above 10 and loop continues
            return False
      return True #Returns "True", factorial is computed, and user now can choose to continue or not.
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10'] #Array of numbers assigned to a list
x = len(numbers) #Amount of list items with array that starts at 0.
print("There are", len(numbers), "from which to choose.") #User is informed of how many numbers there are
def ask_user():

      while True:
            n = int(input("Input a number under eleven:  "))
            while not input_valid(n):
                  n = int(input("Input a number under eleven:  ")) #Number cannot go greater than 10 but relies on an array
            numbers.append(n)
            print("The factorial of", n, "is:", factorial(n)) #Prints the resulting factorial
            user_input = input("Do you want to enter another number: (y or n) ?")
            if user_input != 'y':
                  print("Goodbye!")
                  break
            if user_input != 'n':
                  numbers.append(n)
                  print("Continue: ")
                  continue
            
ask_user() 







    	







       
      









      

