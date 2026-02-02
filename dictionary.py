# 1. Create and print a dictionary
student = {"name": "Alice", "age": 20, "city": "New York"}
print(student)
print(student["name"], student["age"], student["city"])
# 2. Iterate through dictionary
info = {"brand": "Toyota", "model": "Corolla", "year": 2020}
for k in info: print("Key:", k)
for v in info.values(): print("Value:", v)
# 3. Capital finder
capitals = {"India": "New Delhi", "USA": "Washington", "France": "Paris", "Japan": "Tokyo", "Germany": "Berlin"}
country = input("Enter country: ")
print("Capital:", capitals.get(country, "Not Found"))