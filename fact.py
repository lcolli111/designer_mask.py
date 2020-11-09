def factorial(n):
      while True:

            if n == 0:
                  return 1
        
        
            elif n <= 0:
          
                  print("Too negative!")
                  ans1 = int(input("Try again: "))
                  print(ans1)
            elif n >= 10:
                
                  print("Too loud! Keep it down!")
                  ans2 = int(input("Try another number: "))
            
                   #Need to include another loop for three tries
            else:
                  return n * factorial(n-1) #Recursive function used to compute the number
                  break
n=int(input("Input a number under eleven : "))
print("The factorial of", n, "is:", factorial(n))




def num():
    
      if num <= 10:
            return num 
      

num()

#def ask_again():
      #ans = str(input("Do you want to put another number in y/n?  "))
      

