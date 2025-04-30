def check_string(s):
    count_a = s.count('a')
    count_b = s.count('b')

    if count_a % 2 == 0 and count_b % 2 == 1:
        return "YES"
    else:
        return "NO"


input_str = input("Enter a string: ")
result = check_string(input_str)
print(result)
