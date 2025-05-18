def is_in_language(w):
    # Step 1: Check if only a, b, c are used
    if not set(w).issubset({'a', 'b', 'c'}):
        return 'NO'

    # Step 2: Count a's, b's, c's in order and ensure correct order
    i = 0
    n = len(w)
    
    # Count a's
    count_a = 0
    while i < n and w[i] == 'a':
        count_a += 1
        i += 1

    # Count b's
    count_b = 0
    while i < n and w[i] == 'b':
        count_b += 1
        i += 1

    # Count c's
    count_c = 0
    while i < n and w[i] == 'c':
        count_c += 1
        i += 1

    if i != n:
        return 'NO'

    if count_a == count_b == count_c:
        return 'YES'
    else:
        return 'NO'


if __name__ == "__main__":
    user_input = input("Enter a string over {a, b, c}: ")
    result = is_in_language(user_input)
    print(result)
