age = input("What is your age? : ")
age = int(age)

if age < 5:
    print("You're too young for movies! Enjoy cartoons.")
elif age >= 5 and age <= 12:
    print( "G-rated and PG-rated movies are suitable for you.")
elif age >= 13 and age <= 17:
    print("PG-13 and R-rated movies are suitable for you(with parental guidance).")
else:
    print("Any movie is suitable for you.")

likes_action = input("Do you like action movies? (yes/no): ").lower()

if age >= 18 and likes_action == "yes":
    print("You should watch Colony!")