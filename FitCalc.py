weight=float(input("Enter Your Weight (kg):"))
height=float(input("Enter Your Height (0.0):"))
bmi=weight/(height **2)
print(f"Your BMİ is: {bmi}")
if bmi < 18.5:
    print("Category: UnderWeight")
elif 18.5<=bmi < 25:
    print("Category: Normal Weight")
elif 25<=bmi < 30:
    print("Category: Overweight")
else:
    print("Category: Obese")