# 1. Set operations
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}
print("Union:", a | b)
print("Intersection:", a & b)
print("Difference:", a - b)
# 2. Input 5 numbers, convert to set, remove even numbers
nums = set(int(input("Enter number: ")) for _ in range(5))
odds = {x for x in nums if x % 2 != 0}
print("After removing even numbers:", odds)