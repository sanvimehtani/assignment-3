set1 = {1,2,3,4,5}
set2 = {2,4,6,8}
set3 = {1,5,9,13,17}
print ("a)", set1^set2)
print ("b)", set1^set2^set3)
print ("c)", (set1&set2)|(set1&set3)|(set2&set3))
s1 = {1,2,3,4,5,6,7,8,9,10}
print("d)", s1-set1)
print("e)", (s1-set1)&(s1-set2)&(s1-set3))

