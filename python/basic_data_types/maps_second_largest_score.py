# if __name__ == "__main__":
#     numbers = input()
#     print(numbers.strip().split())
#     arr = map(int, numbers.strip().split())
#     # print(arr)
#     # print(list(arr))
#     score_arr = list(arr)
#
#     temp = score_arr.copy()
#     if max()
#     temp.remove(max(temp))
#     print(max(temp))

if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())

    score_arr = list(arr)
    largest = max(score_arr)

    while max(score_arr) == largest:
        score_arr.remove(max(score_arr))

    print(max(score_arr))