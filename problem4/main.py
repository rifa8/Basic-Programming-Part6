def find_max_sum_sub_array(k, arr):
    Max = float('-inf')
    sum_k = 0
    for i in range(k):
        sum_k += arr[i]
    for i in range(k, len(arr)):
        Max = max(Max, sum_k)
        sum_k += arr[i]
        sum_k -= arr[i - k]
    return max(Max, sum_k)

if __name__ == '__main__':
    print(find_max_sum_sub_array(3, [2, 1, 5, 1, 3, 2])) # 9
    print(find_max_sum_sub_array(2, [2, 3, 4, 1, 5])) # 7
    print(find_max_sum_sub_array(2, [2, 1, 4, 1, 1])) # 5
    print(find_max_sum_sub_array(3, [2, 1, 4, 1, 1])) # 7
    print(find_max_sum_sub_array(4, [2, 1, 4, 1, 1])) # 8
