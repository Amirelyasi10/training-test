from pyfiglet import figlet_format

print(figlet_format("Multiple  numbers"))

number = 10

for item in range(1, number + 1):
    for data in range(1, number + 1):
        print(item * data, end="\t")
    print()