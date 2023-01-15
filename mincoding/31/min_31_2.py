n = int(input())
nums = list(map(int, input().split()))


def minSlidingWindow(nums, k):
    min_sum = 9999
    window_sum = 0
    start = 0

    for end in range(len(nums)):
        window_sum += nums[end]

        if end >= k - 1:
            # 0~k-1 까지 더한 값이 최소값보다 작다면, 최소값을 갱신
            if window_sum <= min_sum:
                min_sum = window_sum

            # 윈도우에 포함된 맨 앞자리 수를 제거
            window_sum -= nums[start]
            # 윈도우 시작 인덱스를 하나 증가
            start += 1
    return min_sum

print(minSlidingWindow(nums, 4))