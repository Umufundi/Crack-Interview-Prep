class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float: 
        if len(nums1)>len(nums2):nums1,nums2=nums2, nums1
        m, n = len(nums1), len(nums2);total_len = m + n;is_even = total_len % 2 == 0;low, high = 0, m
        while low <= high:
            partition_nums1 = (low + high) // 2;partition_nums2 = (total_len + 1) // 2 - partition_nums1;max_left_nums1 = float('-inf') if partition_nums1 == 0 else nums1[partition_nums1 - 1];min_right_nums1 = float('inf') if partition_nums1 == m else nums1[partition_nums1];max_left_nums2 = float('-inf') if partition_nums2 == 0 else nums2[partition_nums2 - 1];min_right_nums2 = float('inf') if partition_nums2 == n else nums2[partition_nums2]
            if max_left_nums1 <= min_right_nums2 and max_left_nums2 <= min_right_nums1:
                if is_even:return (max(max_left_nums1, max_left_nums2) + min(min_right_nums1, min_right_nums2)) / 2
                else:return float(max(max_left_nums1, max_left_nums2))
            elif max_left_nums1 > min_right_nums2:high = partition_nums1 - 1
            else:low = partition_nums1 + 1
