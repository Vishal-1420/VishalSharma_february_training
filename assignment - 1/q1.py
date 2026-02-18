
name = input("Enter student name: ")
age = int(input("Enter age: "))
percentage = float(input("Enter percentage: "))
income = float(input("Enter family income: "))
rural_input = input("Is the student from a rural area? (True/False): ")


rural = rural_input.strip().lower() == "true"


eligible = False

if age <= 25:
    if percentage > 90:
        eligible = True
    elif percentage > 85 and income < 300000:
        eligible = True
    elif rural and percentage > 80 and income < 300000:
        eligible = True

# Result
result = "Eligible for scholarship" if eligible else "Not eligible"

# Output
print("\nStudent Details:")
print(f"Name: {name}")
print(f"Age: {age}")
print(f"Percentage: {percentage}")
print(f"Family Income: {income}")
print(f"Rural Area: {rural}")
print(f"Scholarship Status: {result}")
