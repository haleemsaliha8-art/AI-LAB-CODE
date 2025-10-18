def login_system(username, password):
    """Function to check user login"""
    # Stored username and password (you can change these)
    stored_username = "SALIHA QURESHI"
    stored_password = "12345"

    if username == stored_username and password == stored_password:
        return True
    else:
        return False


# Main program
print("=== User Login System ===")
user = input("Enter your username: ")
pwd = input("Enter your password: ")

if login_system(user, pwd):
    print("✅ Login successful! Welcome,", user)
else:
    print("❌ Invalid username or password. Please try again.")
