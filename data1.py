users = [("Ali", 20), ("Sara", 17), ("Omar", 25), ("Laila", 15)]

for user in users:
    name, age = user
    if age >= 18:
        print(f"{name} is allowed to vote.")
    else:
        print(f"{name} is not allowed to vote.")