class Power:
    def __init__(self, x, n):
        self.x = x
        self.n = n

    # Method to calculate power manually
    def pow(self):
        result = 1
        for _ in range(abs(self.n)):
            result *= self.x

        # Handle negative exponents
        if self.n < 0:
            result = 1 / result
        return result


# Example usage
if __name__ == "__main__":
    # Create a Power object
    obj = Power(2, 5)  # You can change the numbers (x=2, n=5)
    
    print(f"{obj.x} raised to the power {obj.n} is: {obj.pow()}")
