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
def getNumberFromUser():
      num = input("Please input whole a number under eleven: ")
      if (num <= 10):
            return num
      else:
            print ("Sorry wrong number!")
            return -1


            
while True:
      result = -1
      while (result < 0):
            result = getNumberFromUser()
      fact = factorial(result)
      print("Factorial of ", result, "is", fact)
def ask_again():
      ans = input("Do you want to put another number in? ")
      

while True:
      result = -1
      while (result < 0):
            result = getNumberFromUser()
      fact *= n
      fact = factorial(result)
      
      print("Factorial of ", result, "is", fact)

getNumberFromUser()













            
       
            

            #input("Enter yes/no to continue")
            

                  
      
            
      

    
      

      

       

    
        
   

      


      
   
    
		    
	  

      #ans = input("Another one? yes/no")
#while ans.lower() not in ("yes","no"):
        #ans = input("Another one? yes/no")
        #if input != "yes":
            #break
        #else:
              #pass






    #if n == 0:
        #return 1
    #else:
        #return n * factorial(n-1)

  


#num=int(input("Input the first number to compute the factorial : "))
#print("The first factorial is: ".format(num))
#print(factorial(num))
#num=int(input("Input the second number to compute the factorial : "))
#print("The second factorial is: ".format(num))
#print(factorial(num))
#num=int(input("Input the third number to compute the factorial : "))
#print("The third factorial is: ".format(num))
#print(factorial(num))


 

    #choice = input("Enter choice(1/2/3/4):")

    #num1 = int(input("Enter first number: "))
    #num2 = int(input("Enter second number: "))

    #if choice == '1':
       #print(num1,"+",num2,"=", (num1 + num2))

    #elif choice == '2':
       #print(num1,"-",num2,"=", (num1 - num2))

    #elif choice == '3':
       #print(num1,"*",num2,"=", (num1 * num2))

    #elif choice == '4':
       #print(num1,"/",num2,"=", (num1 / num2))
    #else:
       #print("Invalid input")
    #cont = input("Continue?y/n:")
    #if cont == "y":
      #print("Input another number: ")        
  


           
           
      







#def factorial(n):
      #if n <= 0:
            #return 0
      #elif n == 1:
            #return 1
      #else:
            #fact = 1
            #while(n > 1):
                  #fact *= n
                  #n -= 1
            #return fact

#def getNumber():
     # num = int(input("Input a number under 11: "))
      #if (num<= 10):
            #return num
      #else:
            #print("Sorry, the number is over 11. Please try again!")
            #return = -1

      #while True:
            #result != -1
            #while(result = 0):
                  #result = 
      #getNumber()

           # fact = factorial(result)
            #print("Factorial of", result, "is", fact)

            #again = input("Do you want to input another number? (y/n)").lower()
            #if again != "y":
                  #break

         


#print(factorial(num))
#How can I use a range to limit input numbers from 1 to 10?

#for num in range(5):
      #print(factorial(num))

#Simple calculator for factorials

#num = 2
#print("Factorial of", num, "is", factorial(num))
#for num in range(11):
    #print(num * 2)






 





 