s={1,4,7,9,6}
print(s)
print(type(s))
s1=set((1,2))
print(s1)
for x in s:
    print(x)
s.add("varsha") 
print(s)   
s.update([5,1])
print(s)



set1={1,2,3,4,5}
set2={3,4,5,6,7}
set3={7,8,9,10}

print("set1 U set2: ",set1 | set2)
print("set1 I set2:", set1 & set2)
print("set1 I set2:", set1 - set2)

s1={5,10,20,9}
s2={10,30,20,50}
print("set1 U set2:",s1|s2)
print("set1 I set2:",s1&s2)