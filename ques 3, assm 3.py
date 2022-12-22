lr = int(input("Enter lower limit: "))
ur = int(input("Enter upper limit: "))
a = [(x,x**2) for x in range(lr,ur+1)]
print (a)
