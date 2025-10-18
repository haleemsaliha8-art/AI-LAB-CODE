def show_even_numbers(n):
    even_numbers = []
    for i in range(1, n + 1):
        even_number = i * 2
        even_numbers.append(even_number)
        print(even_number, end=' ')
    print()  # for a newline
    return even_numbers

# Example usage
n = 5  # You can change this to any positive integer
evens = show_even_numbers(n)

# Calculate sum and product outside the function
sum_of_evens = sum(evens)

product_of_evens = 1
for num in evens:
    product_of_evens *= num

print("Sum of even numbers:", sum_of_evens)
print("Product of even numbers:", product_of_evens)
