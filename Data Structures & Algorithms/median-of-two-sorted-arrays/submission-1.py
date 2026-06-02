class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        a, b = nums1, nums2
        total = len(nums1) + len(nums2)
        half = total // 2

        if len(b) < len(a):
            a, b = b, a
        
        l, r = 0, len(a) - 1
        while True:
            mid_a = (l + r) // 2
            mid_b = half - mid_a - 2
        
            a_left = a[mid_a] if mid_a >= 0 else float("-infinity")
            a_right = a[mid_a + 1] if (mid_a + 1) < len(a) else float("infinity")
            b_left = b[mid_b] if mid_b >= 0 else float("-infinity")
            b_right = b[mid_b + 1] if (mid_b + 1) < len(b) else float("infinity")

            if a_left <= b_right and b_left <= a_right:
                if total % 2:
                    return min(a_right, b_right)
                return (max(a_left, b_left) + min(a_right, b_right)) / 2
            elif a_left > b_right:
                r = mid_a - 1
            else:
                l = mid_a + 1