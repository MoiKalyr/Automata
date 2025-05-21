def octal_to_binary(octal_str):
    try:
        # octal to integer
        decimal_value = int(octal_str, 8)
        # integer to binary
        binary_str = bin(decimal_value)[2:]
        return binary_str
    except ValueError:
        return "Invalid octal number."

if __name__ == "__main__":
    user_input = input("Enter an octal number: ").strip()
    result = octal_to_binary(user_input)
    print("Binary output:", result)
