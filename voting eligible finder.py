total_count = 0
eligible_count = 0
male_eligible_count = 0
female_eligible_count = 0

while True:
    name = input("Enter the person's name (or 'done' to stop): ")
    if name == 'done':
        break
    age = int(input("Enter the person's age: "))
    gender = input("Enter the person's gender (male or female): ")
    total_count += 1
    if age >= 18:
        eligible_count += 1
        if gender == "male":
            male_eligible_count += 1
        elif gender == "female":
            female_eligible_count += 1

total_population = total_count
percentage = eligible_count / total_population * 100

print("=" * 40)
print("Election Results")
print("=" * 40)
print(f"Total population: {total_population}")
print(f"Percentage of population eligible to vote: {percentage:.2f}%")
print(f"Percentage of male population eligible to vote: {male_eligible_count:.2f}%")
print(f"Percentage of female population eligible to vote: {female_eligible_count:.2f}%")
print("=" * 40)
