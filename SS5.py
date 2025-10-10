digit_to_word = {
    '0': 'Zero', '1': 'One', '2': 'Two', '3': 'Three',
    '4': 'Four', '5': 'Five', '6': 'Six', '7': 'Seven',
    '8': 'Eight', '9': 'Nine'
}

number = input("Enter a number: ")  # e.g. 1234
in_words = ' '.join(digit_to_word[d] for d in number if d in digit_to_word)
print("In words:", in_words)
