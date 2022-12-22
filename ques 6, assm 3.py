x = int (input("Enter number of times questions asked: "))
i = 1
ls = list()
ls2 = list()
ls3 = list()
while i <= x:
    a = input("Enter Y for yes and N for no: ")
    if a == "Y":
        name = input("Enter your name: ")
        sid = input("Enter your SID: ")
        b= {
            name:sid
        }
        tup = (name)
        ls.append(tup)
        tup2 = (sid)
        ls2.append(tup2)
        tup3 = (name, sid)
        ls3.append(tup3)
        
    i += 1

print ("a)", ls3)
print ("b)",sorted(ls))
print ("c)",sorted(ls2))
print ("d)", b.index[sid])

    


    


