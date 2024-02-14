"""
2149. Rearrange Array Elements by Sign

You are given a 0-indexed integer array `nums` of even length consisting of an
equal number of positive and negative integers.

You should rearrange the elements of `nums` such that the modified array
follows the given conditions:
    1. Every consecutive pair of integers have opposite signs.
    2. For all integers with the same sign, the order in which they were
        present in `nums` is preserved.
    3. The rearranged array begins with a positive integer.

Return the modified array after rearranging the elements to satisfy the
aforementioned conditions.
"""

class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        # Partition `nums` into positive and negative integers
        pos = []
        neg = []
        for n in nums:
            if n >= 0:
                pos.append(n)
            else:
                neg.append(n)
        
        # Build `result` array: every even index from `pos`, every odd from `neg`
        result = [0] * len(nums)
        for i in range(len(pos)):
            result[2 * i] = pos[i]
        for i in range(len(neg)):
            result[2 * i + 1] = neg[i]
        
        return result

    def rearrangeArray(self, nums: List[int]) -> List[int]:
        result = [0] * len(nums)
        pos, neg = 0, 1  # initial indices to place positive/negative values
        
        # Because `result` must start with a positive value, every even index
        # must be positive and every odd negative. When we come across one,
        # put it in the next available slot and increment index by 2.
        for i in range(len(nums)):
            if nums[i] > 0:
                result[pos] = nums[i]
                pos += 2
            else:
                result[neg] = nums[i]
                neg += 2
        
        return result