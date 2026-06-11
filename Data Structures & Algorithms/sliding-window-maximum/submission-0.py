class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        max_list = []
        window = []

        for i in range(len(nums)):
            heapq.heappush(window, (-nums[i], i))
            if i >= k - 1:
                print(window[0][1], i - k)
                while window[0][1] <= i - k:
                    heapq.heappop(window)
                max_list.append(-window[0][0])
        
        return max_list