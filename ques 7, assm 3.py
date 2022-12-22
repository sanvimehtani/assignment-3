
def sum1(n):
    if n <= 0:
        return 0
    fib = [0]*(n+1)
    fib[1]= 1
    sum2 = fib[0] + fib[1]
    for i in range (2, n-1):
        fib[i] = fib[i-1] + fib[i-2]
        sum2 = sum2 + fib[i]
    return sum2
n = int(input("Enter number of terms "))
n1 = 0
n2 = 1
count = 0
if n <= 0:
   print("Please enter a positive integer")
elif n == 1:
   print("Fibonacci sequence upto",n,":")
   print(n1)
else:
   print("Fibonacci sequence:")
   while count < n:
       print(n1)
       nth = n1 + n2
       n1 = n2
       n2 = nth
       count += 1
print ("The average is: ", (sum1(n)/n))



 
