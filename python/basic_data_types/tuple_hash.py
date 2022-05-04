if __name__ == '__main__':
    input_list = input().strip().split()
    int_list = [int(x) for x in input_list]

    t = tuple(int_list)
    print(hash(t))