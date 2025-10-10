sample_list = ['abc', 'xyz', 'aba', '1221', 'xyzzyx', 'aa', '122']
count = 0
for word in sample_list:
    if len(word) >= 2 and word[0] == word[-1]:
        count += 1
print("Count of strings with same first and last character:", count)
