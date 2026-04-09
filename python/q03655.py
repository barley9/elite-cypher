"""
3655. XOR After Range Multiplication Queries II

You are given an integer array `nums` of length `n` and a 2D integer array
`queries` of size `q`, where `queries[i] = [li, ri, ki, vi]`.

For each query, you must apply the following operations in order:
    Set `idx = l_i`.
    While `idx <= r_i`:
        Update: `nums[idx] = (nums[idx] * vi) % (10^9 + 7)`.
        Set idx += ki.

Return the bitwise XOR of all elements in nums after processing all queries.
"""

class Solution:
    def xorAfterQueries(self, nums: List[int], queries: List[List[int]]) -> int:
        """
        O(n * (q + 1)) time, O(1) space solution, where n = len(nums) and
        q = len(queries).
        
        TOO SLOW
        """
        N = 10**9 + 7

        for start, stop, step, mul in queries:
            for i in range(start, stop + 1, step):
                nums[i] *= mul
        
        result = 0
        for n in nums:
            result ^= n % N
        return result


    def xorAfterQueries(self, nums: List[int], queries: List[List[int]]) -> int:
        """
        O(n * (q + 3)) time, O(sodding terrible) space solution

        OUT OF MEMORY ERROR
        """
        N = 10**9 + 7  # modulo divisor

        factors = [[1] for _ in nums]

        for start, stop, step, mul in queries:
            for i in range(start, stop + 1, step):
                factors[i].append(mul)
        
        # print(factors)

        for i in range(len(nums)):
            for f in factors[i]:
                nums[i] = (nums[i] * f) % N
        
        result = 0
        for n in nums:
            result ^= n
        return result

    def xorAfterQueries(self, nums: List[int], queries: List[List[int]]) -> int:
        """
        https://cp-algorithms.com/algebra/montgomery_multiplication.html
        """
        N = 10**9 + 7
        R = 2 ** 32  # R > N (I checked)

        for i in range(len(nums)):
            nums[i] = (nums[i] * R) >> 32  # tranform into Montgomery space; a mod 2^k == a >> k
        
        # I don't care enough...

    def xorAfterQueries(self, nums: List[int], queries: List[List[int]]) -> int:
        """
        TOO SLOW

        (This problem requires a hybrid approach which I don't care enough to implement)
        """
        N = 10**9 + 7  # modulo divisor

        q_dict = {}
        for start, stop, step, mul in queries:
            if (start, stop, step) in q_dict:
                q_dict[(start, stop, step)] = (q_dict[(start, stop, step)] * mul) % N
            else:
                q_dict[(start, stop, step)] = mul % N
        
        for (start, stop, step), mul in q_dict.items():
            for i in range(start, stop + 1, step):
                nums[i] = (nums[i] * mul) % N
        
        result = 0
        for n in nums:
            result ^= n
        return result