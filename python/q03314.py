"""
3314. Construct the Minimum Bitwise Array I

You are given an array `nums` consisting of `n` prime integers.

You need to construct an array `ans` of length `n`, such that, for each index
`i`, the bitwise `OR` of `ans[i]` and `ans[i] + 1` is equal to `nums[i]`, i.e.
`ans[i] OR (ans[i] + 1) == nums[i]`.

Additionally, you must minimize each value of `ans[i]` in the resulting array.

If it is not possible to find such a value for `ans[i]` that satisfies the
condition, then set `ans[i] = -1`.
"""

class Solution:
    def minBitwiseArray(self, nums: List[int]) -> List[int]:
        """
        O(n * ???) time, O(n) space solution

        Essentially a brute-force search. An attempt was made to slightly
        optimize the search range.
        """
        answer = []
        for n in nums:
            start = (1 << (n.bit_length() - 1)) - 1
            # print(f"{n:0b}", start)
            for k in range(start, (start << 1) + 1):
                if k | (k + 1) == n:
                    answer.append(k)
                    break
            else:
                answer.append(-1)
        return answer