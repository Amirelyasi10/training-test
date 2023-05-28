from pyfiglet import figlet_format

print(figlet_format("odd  numbers"))

number = int(input("Enter a number: "))

for num in range(1, number):
    if num % 2 != 0:
        print(num)