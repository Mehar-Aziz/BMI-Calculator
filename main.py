height = input("Enter your Height in meters(m): ")
weight = input("Enter you Weight in kilagrams(kg): ")
BMI = int(weight) / float(height) ** 2
result = int(BMI)
print(result)
print("Your BMI is " + str(result)) #if want to write in the string