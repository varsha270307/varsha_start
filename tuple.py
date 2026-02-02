# 1. Count how many times 10 appears
t = (10, 40, 90, 10, 30, 10)
print(t.count(10))
# 2. Print first three elements
print(t[:3])
# 3. Concatenate two tuples
t2 = (100, 200)
print(t + t2)
# 4. Convert to list, modify, convert back to tuple
lst = list(t)
lst.append(60)
t_modified = tuple(lst)
print(t_modified)
# 5. Accept 5 numbers, store in tuple, and print average
nums = tuple(int(input(f"Enter number {i+1}: ")) for i in range(5))
print("Average:", sum(nums)/len(nums))