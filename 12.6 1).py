user_input = input("Enter a positive integer: ")

try:
    if int(user_input) >= 0:
        print("The number is positive.")
except ValueError:
    print("Please enter an integer")
else:
    if int(user_input) < 0:
        print("Please enter an positive integer")
finally:
    print("Thank you!")

