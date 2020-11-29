def Fibonacci(n):
    a = 0
    b = 1
    if n<=0:
        print("Try again")
    # First Fibonacci number is 0
    elif n==1:
        return 0
    # Second Fibonacci number is 1
    elif n==2:
        return b
    else:
        for i in range(2, n):
            c = a + b
            a = b
            b = c
        return b
n_terms = int(input("How many terms? "))
n1, n2 = 0, 1
count = 0

if n_terms<=0:
    print("Enter a positive integer: ")
elif n_terms == 1:
    print("Fibonacci sequence up to", n_terms, ":") #User determines the first few terms
    print(n1)
else:
    print("Fibonacci sequence: ")
    while count < n_terms:
        print(n1)
        nth = n1 + n2
        n1 = n2
        n2 = nth
        count += 1


 
# Driver Program
 
#print(Fibonacci(n))
 