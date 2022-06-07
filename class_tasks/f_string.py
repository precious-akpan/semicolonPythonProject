name = "Precious"
lang = "Java"
age = 34

fff = f"{name:<10}is a {lang} lord and {name} is {age}years old"
print(fff)

for i in range(1, 13):
    print(f"{i} Multiplication Table")
    for j in range(1, 13):
        print(f"{i} x {j:>2} = {i*j:>3}")
    print()