"""
3396. Minimum Number of Operations to Make Elements in Array Distinct

You are given an integer array `nums`. You need to ensure that the elements in
the array are distinct. To achieve this, you can perform the following
operation any number of times:
    Remove 3 elements from the beginning of the array. If the array has fewer
        than 3 elements, remove all remaining elements.

Note that an empty array is considered to have distinct elements. Return the
minimum number of operations needed to make the elements in the array
distinct.
"""

class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        """O(n) time, O(1) space solution"""
        counts = [0] * 101  # 1 <= nums[i] <= 100
        for n in nums:
            counts[n] += 1
        
        result = 0
        while any(count > 1 for count in counts):
            # print(nums)
            # print([(i, counts[i]) for i in range(len(counts)) if counts[i] > 0])
            for _ in range(min(3, len(nums))):
                counts[nums[0]] -= 1
                del nums[0]
            result += 1
        
        return result

    def minimumOperations(self, nums: List[int]) -> int:
        """SLOWER"""
        nums = nums[::-1]  # reverse `nums` to make deletion faster

        counts = [0] * 101  # 1 <= nums[i] <= 100
        for n in nums:
            counts[n] += 1
        
        result = 0
        while any(count > 1 for count in counts):
            for i in range(min(3, len(nums))):
                counts[nums[len(nums) - i - 1]] -= 1
            nums = nums[:len(nums) - 3]
            result += 1
        
        return result

    def minimumOperations(self, nums: List[int]) -> int:
        """O(n) time, O(n) space solution; FASTEST"""
        q, r = divmod(len(nums), 3)
        offset = len(nums) - r
        elems = set(nums[offset:])
        if len(elems) < r:
            return q + 1
        # print(elems)
        for i in range(1, q + 1):
            s = set(nums[offset - 3*i:offset - 3*(i - 1)])
            # print("\t", s)
            if (len(s) < 3) or (s & elems):
                # print("\t returned from inside loop")
                return q - i + 1
            else:
                elems |= s
        return 0