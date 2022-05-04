def split_and_join(line: str):
    line_split = line.strip().split()
    line_join = "-".join(line_split)
    return line_join


if __name__ == '__main__':
    print(split_and_join(input()))
