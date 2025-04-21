def reverse_words(input_string):
    words = input_string.split()
    reversed_words = [word[::-1] for word in words]
    result = ' '.join(reversed_words)
    return result


input_string = input("Enter a sentence: ")
output_string = reverse_words(input_string)
print("Reversed words:", output_string)