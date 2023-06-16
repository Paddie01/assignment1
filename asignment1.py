birth_year = input("birth year: ")
age = 2023 - int(birth_year)
print(age)
if age >= 18:
    print("you can vote")
else: print("you can't vote")