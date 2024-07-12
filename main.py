height = input("Enter your Height in meters(m): ")
weight = input("Enter you Weight in kilagrams(kg): ")
BMI = int(weight) / float(height) ** 2
result = int(BMI)

if BMI < 18.5:
    category = "Underweight"
elif 18.5 <= BMI < 24.9:
    category = "Normal weight"
elif 25<= BMI <29.9:
    category = "Overweight"
else:
    category = "Obese"

print("Your BMI is " + str(result)) #if want to write in the string
print("You are categorized as: "+ category)