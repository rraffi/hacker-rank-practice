# arr = [-3, 1, -8, 4, -1, 2, 1, -5, 5]
# arr = [-2, -3, 4, -1, -2, 1, 5, -3]
arr = [-1, -2, -3, -4]

max_subarray_sum = 0
start = 0
end = 0

for i in range(len(arr)):
    running_sum = 0

    for j in range(i, len(arr)):
        running_sum += arr[j]

        if running_sum > max_subarray_sum:
            max_subarray_sum = running_sum
            start = i
            end = j

print(f"Found max subarray between index {start} and {end}")
print(arr[start:end+1])
print(max_subarray_sum)