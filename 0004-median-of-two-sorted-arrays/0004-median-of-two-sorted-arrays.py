class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        new_arr = nums1 + nums2  # Concatenate two lists
        new_arr.sort()  # Sort the combined list

        n = len(new_arr)
        if n % 2 != 0:  # If the length is odd
            return float(new_arr[n // 2])
        else:  # If the length is even
            return float((new_arr[n // 2 - 1] + new_arr[n // 2]) / 2)

        