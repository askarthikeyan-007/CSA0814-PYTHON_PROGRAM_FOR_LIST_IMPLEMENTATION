try:
    num1 = int(input("Enter the first four-digit number: "))
    num2 = int(input("Enter the second four-digit number: "))
    if not (1000 <= num1 <= 9999) or not (1000 <= num2 <= 9999):
        print("Both numbers must be four-digit numbers.")
    else:   
        mul = num1 * num2
        r = str(mul)
        if r == r[::-1]:
            print("True")
        else:
            print("False")
except Exception as e:
    print("An error occurred:", e)
