num90 = float(input("Enter first number: "))
num80 = float(input("Enter second number: "))
num70 = float(input("Enter third number: "))
if num90 >= num80 and num90 >= num70:
    largest = num90
elif num80 >= num90 and num80 >= num70:
    largest = num80
else:
    largest = num70
print("The largest number is:", largest)