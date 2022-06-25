# Write a function to compute 5/0 and use try/except to catch the exceptions.


while True:
    try:
        b = int(input("Enter the number that needs to divide 5: "))
        a = 5/b

    except (ZeroDivisionError) as err:
        print("Don't divide the number by 0")
        continue

    print(a)
    break
