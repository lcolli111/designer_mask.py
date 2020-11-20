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
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10'] #user is informed of how many numbers
x = len(numbers)
print("There are", len(numbers), "from which to choose.")

def ask_user1():

      while True:
            n = int(input("Input a number under eleven:  "))
            while not input_valid(n):
                  n = int(input("Input a number under eleven:  "))
                  #x = len(numbers.append(n))
                  #print(x)
            numbers.append(n)
            print("The factorial of", n, "is:", factorial(n)) #Prints the resulting factorial
            user_input1 = input("Do you want to enter another number: (y or n) ?")
            if user_input1 != 'y':
                  print("Goodbye!")
                  break
            if user_input1 != 'n':
                  numbers.append(n)
                  print("Continue: ")
                  continue
            
ask_user1()







    	







       
      #elif n > 10:
            #print("Too loud!")
            #return False
      #return True
                  
                   

            #def ask_again():
                  #ans = ''
                  #while ans not in('y', 'n'):
                        #ans = input("Would you like to input another number in y/n?").lower()
                        #if ans == 'y':
                              #return True
                        #print("Goodbye!")
                        #return False 
            #numbers = []
            #while True:
                  #n = int(input("Input a number under eleven: "))
                  #while not input_valid(n):
                        #n = int(input("Input a number under eleven: "))
                        #numbers.append(n)

                        #print("The factorial of", n, "is: ", factorial(n))

                        #if not again():
                              #break
                  #print("")
                  #print("The first number you entered was " + str(numbers[]) + ".")
                  #print("The factorial is " + str(factorial(numbers[0])) + ".")









      

