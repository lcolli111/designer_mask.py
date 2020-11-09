def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
n=int(input("Input a number to compute the factiorial : "))
print(factorial(n))


def getNumber():
      num = int(input("Please input whole a number under eleven: "))
      if (num <= 10):
            return num
      
      else:
            print ("Sorry wrong number!")
            return -1
getNumber()

#def ask_again():
      #ans = str(input("Do you want to put another number in y/n?  "))
      
      #if ans == 'y':
            #return num

      #else:

            #quit
#ask_again()   
# ('y', 'n') 
      
            
      #else:
            #if ans == 'n':

                  #print ("Good bye!")
                  #quit

                
#while True:
      #result = -1
      #while (result < 0):
            #result = getNumber()
      #fact = factorial(result)
      #print("Factorial of ", result, "is", fact)