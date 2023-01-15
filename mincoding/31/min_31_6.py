n = int(input())
nums = [1, 2, 3, 3, 5, 1, 0, 1, 3]
count = 0

def slidingwindow(nums, k):
    min_sum = 9999
    w_sum = 0
    start = 0

    for end in range(len(nums)):
        w_sum += nums[end]

        if end >= k-1:
            if w_sum <= min_sum:
                min_sum = w_sum

            w_sum -= nums[start]
            start += 1
    return min_sum

print(slidingwindow(nums, n))