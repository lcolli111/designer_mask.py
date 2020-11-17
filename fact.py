def factorial(n):
      if n == 0:
            return 1
      return n * factorial(n-1) #Recursive function used to compute the number

#def ask_again():
      #ans = ('yes', 'no')
      #while ans not in ('yes', 'no'):
            #ask_again = input("Do you want to put another number?  ").lower()
      #if ans == 'yes':
            #return True
            #print('yes')
      #if ans == 'no':
            #print("Goodbye!")
            #return False 
#ask_again()
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
            user_input = input("Do you want to enter another number y/n ?")
            if user_input != y:
                  break
                  print("Goodbye!")
ask_user()

#Below code is commented for possible future use      
#print("")
#print("The first number you entered was " + str(numbers[0]) + ".")
#print("It's factorial is " + str(factorial(numbers[0])) + ".")
#The below code is still refusing to work!

#Question = input("your question")
#if Question == ("yes")
	#print ("well done")
#elif Question == ("no")
	#print ("try again")        
#########################################            
#class SpecialString:
      #def __init__(self, cont):
    #self.cont = cont           
#########################################            
#def validate_age(age):
    #if age >=0 :
        #return True
    #return False
#########################################
#while True:
    #try:
        #age = int(raw_input("Please enter your age:"))
        #if validate_age(age): break
    #except ValueError:
        #print "Error: Invalid age."





    	







       
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
      

