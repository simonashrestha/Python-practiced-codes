a = int(input("Please enter your first number: "))
b = int(input("Please enter your second number: "))
c = int(input("Please enter your third number: "))
if a>b and a>c:
    print("The largest number is ",a)

elif (b>a) and (b>c):
    print("The largest number is ",b)
else:
    print("The largest number is ",c)
