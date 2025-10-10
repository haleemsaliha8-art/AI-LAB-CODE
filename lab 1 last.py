def is_harshad_number(num):
    # Calculate sum of digits
    digit_sum = sum(int(digit) for digit in str(num))
    
    # Avoid division by zero
    if digit_sum == 0:
        return False
    
    # Check divisibility
    return num % digit_sum == 0

# Input from user
number = int(input("Enter a number: "))

# Check and display result
if is_harshad_number(number):
    print(f"{number} is a Harshad Number.")
else:
    print(f"{number} is not a Harshad Number.")
