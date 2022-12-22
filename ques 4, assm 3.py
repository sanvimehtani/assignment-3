grade = int(input("Enter number between 4 and 10: "))
if grade == 4:
    a = "D"
    b = "Poor"
elif grade == 5:
    a = "C"
    b = "Below Average"
elif grade == 6:
    a = "C+"
    b = "Average"
elif grade == 7:
    a = "B"
    b = "Good"
elif grade == 8:
    a = "B+"
    b = "Very Good"
elif grade == 9:
    a = "A"
    b = "Excellent"
elif grade == 10:
    a = "A+"
    b = "Outstanding"
else:
    print ("error")
print ("Your grade is '{a}' and {b}".format(a = a, b = b))
        


