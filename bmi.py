weight=float(input("Enter the weight in pounds: "))
height=float(input("Enter the height in inches: "))
bmi=weight/(height**2)*703
print(bmi)
if(bmi<=5):
    print("under weight")
elif(bmi>5 and bmi<=85):
    print("normal weight")
else:
    print("over weight")