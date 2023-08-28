def most_frequent(input_string):
    char_frequency = {}
    for char in input_string:
        if char.isalpha():
            char = char.lower()
            if char in char_frequency:
                char_frequency[char] += 1
            else:
                char_frequency[char] = 1

    sorted_chars = sorted(char_frequency.keys(), key=lambda char: char_frequency[char], reverse=True)
    print("Letters in decreasing order of frequency:")
    for char in sorted_chars:
        print(f"'{char}': {char_frequency[char]}")

try:
    input_string = input("Enter a string: ")
    most_frequent(input_string)
except Exception as e:
    print("An error occurred:", e)
