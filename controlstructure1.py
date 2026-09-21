 
nilai = int(input("masukkan nilai terbesar: "))

if nilai >= 90:
    print("kinerja sangat baik")
elif nilai >= 80:
    print("kinerja baik")
elif nilai >= 70:
    print("kinerja cukup")
elif nilai >= 60:
    print("kinerja rata-rata")
else:
    print("kinerja kurang")


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

n = int(input("Enter n: "))

a = 0
b = 1

for i in range(n):
    print(a, end=" ")
    c = a + b
    a = b
    b = c

n = int(input("Enter n: "))

for i in range(1, n + 1):
    if i % 2 != 0:
        print(i, end=" ")

n = int(input("Enter n: "))

for i in range(1, n + 1):
    for j in range(i):
        print(i, end=" ")
    print()