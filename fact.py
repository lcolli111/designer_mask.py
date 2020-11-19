def factorial(n):
      if n == 0:
            return 1
      return n * factorial(n-1) #Recursive function used to compute the number

def input_valid(n):
      if n < 0:
            print("Too negative!")
            return False
      elif n > 10:
            print("Too loud! Keep it down!")
            return False
      return True
numbers = [] 
def ask_user():

      while True:
            n = int(input("Input a number under eleven:  "))
            while not input_valid(n):
                  n = int(input("Input a number under eleven:  "))
            numbers.append(n)
            print("The factorial of", n, "is:", factorial(n)) #Prints the resulting factorial
            user_input = input("Do you want to enter another number: ('y' or n) ?")
            if user_input != 'y':
                  
                  #user_input = input("Do you want to see a previous number? 'y/n' ")
                  print("Goodbye!")
                  break
            if user_input != 'n':
                  #user_input = input("Do you want to see a previous number? y/n ")
                  numbers.append(n)
                  print("Continue: ")
                  #print("The factorial of", n, "is:", factorial(n))
                  continue
            
ask_user()
#print(numbers = [user_input - 1])







    	







       
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









      

