def print_table(n, upto=10):
    for i in range(1, upto + 1):
        print(f"{n} × {i} = {n * i}")

def main():
    num = int(input("Enter a number for which you want the table: "))
    limit = int(input("Enter how far (e.g. up to 10): "))
    print_table(num, limit)

