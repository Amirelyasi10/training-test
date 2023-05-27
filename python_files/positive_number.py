from pyfiglet import figlet_format

print(figlet_format("Positive  number"))
number = int(input("Enter number: "))

if number > 0:
    print("Positive number")
elif number < 0:
    print("Negative number")
else:
    print("Zero")