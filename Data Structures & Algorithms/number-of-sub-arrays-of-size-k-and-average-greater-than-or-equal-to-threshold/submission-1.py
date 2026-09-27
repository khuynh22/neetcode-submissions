class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        res = 0
        curr_sum = sum(arr[:k - 1])

        for i in range(len(arr) - k + 1):
            curr_sum += arr[i + k -1]
            if curr_sum / k >= threshold:
                res += 1
            
            curr_sum -= arr[i]

        return res        