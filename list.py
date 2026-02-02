# Q.1 
a = [10, 20, 30, 40, 50]
print(a[:3])
# Q.2
b = [25, 10, 5, 100, 50]
print(sorted(b))
print(sorted(b, reverse=True))
# Q.3
c = [1, 5, 3, 2, 4, 3, 5, 3, 4, 5]
print(c.count(3))
# Q.4
list1 = [12, 45, 2, 56, 9]
list2 = [45, 78, 23, 90]
print(list1 + list2)
d = list1.copy(); d.extend(list2)
print(d)
# Q.5 
e = [30, 45, 23, 78, 90, -1, 0]
print(max(e), min(e))
# Q.6
f = [12, 7, 9, 14, 5, 6, 3, 2]
print([x for x in f if x % 2 != 0])
