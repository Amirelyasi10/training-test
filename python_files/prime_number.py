number = int(input("Enter number: "))

if number <=1:
    print(f"is not prime number")
else:
    for num in range(2, number):
        if number % 2 == 0:
            print(f"is not prime number")
            break
    else:
        print(f"Prime number")