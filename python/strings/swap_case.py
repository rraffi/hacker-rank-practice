def swap_case(s):
    # return s.swapcase() #quick and dirty solution 1

    # solution 2
    # new_s = ''
    # for letter in s:
    #     if letter.islower():
    #         new_s += letter.upper()
    #     elif letter.isupper():
    #         new_s += letter.lower()
    #     elif not letter.isalpha():
    #         new_s += letter
    #
    # return new_s

    return "".join([letter.lower() if letter.isupper() else letter.upper() for letter in s])


if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)