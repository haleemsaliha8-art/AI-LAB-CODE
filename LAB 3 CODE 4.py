def match_strings(str1, str2):
    """Function to check if two strings match exactly"""
    if str1 == str2:
        return True
    else:
        return False


# Taking input from the user
string1 = input("Enter the first string: ")
string2 = input("Enter the second string: ")

# Calling the function
if match_strings(string1, string2):
    print("✅ The strings match exactly!")
else:
    print("❌ The strings do not match.")
