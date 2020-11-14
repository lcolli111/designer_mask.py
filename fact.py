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
while True:
      n = int(input("Input a number under eleven : "))
      while not input_valid(n):
            n=int(input("Input a number under eleven : "))
      numbers.append(n)
      print("The factorial of", n, "is:", factorial(n)) #Prints the resulting factorial
#Below code is commented for possible future use      
#print("")
#print("The first number you entered was " + str(numbers[0]) + ".")
#print("It's factorial is " + str(factorial(numbers[0])) + ".")
#The below code is still refusing to work!
def yes_or_no():
      reply = str(input(question + '(y/n): ')).lower.strip()
      if reply[0] == 'y':
            return 1
      elif reply[0] == 'n':
            return 0
      else:
            return yes_or_no("Please enter (y/n) ")
yes_or_no()



answer = input("Enter yes or no: ") 
if answer == "yes": 
     pass 
elif answer == "no": 
     quit
else: 
    print("Please enter yes or no.") 
print(answer)

answer = None 
while answer not in ("yes", "no"): 
    answer = input("Enter yes or no: ") 
    if answer == "yes": 
          pass
    elif answer == "no": 
          quit 
    else: 
    	print("Please enter yes or no.") 
print(answer)

    	







       
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








#def ask_again():
      #ans = str(input("Do you want to put another number in y/n?  "))
      

