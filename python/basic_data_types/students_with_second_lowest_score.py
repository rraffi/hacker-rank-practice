if __name__ == "__main__":
    n = int(input())
    records = [[input(), float(input())] for _ in range(n)]

    second_lowest = sorted(list(set([marks for name, marks in records])))[1]

    names_with_second_lowest_score = [name for name, marks in records
                                      if marks == second_lowest]

    names_with_second_lowest_score.sort()
    print(*names_with_second_lowest_score, sep='\n')
