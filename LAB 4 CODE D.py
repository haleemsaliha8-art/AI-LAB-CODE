class Power:
    def __init__(self, x, n):
        self.x = x
        self.n = n

    def pow(self):
        result = 1

        # Multiply x by itself |n| times
        for _ in range(abs(self.n)):
            result *= self.x

        # If n is negative, take reciprocal
        if self.n < 0:
            result = 1 / result

        return result


# Example usage
if __name__ == "__main__":
    # Take user input
    x = float(input("Enter the base number (x): "))
    n = int(input("Enter the exponent (n): "))

    obj = Power(x, n)
    print(f"{x} raised to the power {n} is: {obj.pow()}")
