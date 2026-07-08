"""
3756. Concatenate Non-Zero Digits and Multiply by Sum II

You are given a string `s` of length `m` consisting of digits. You are also
given a 2D integer array `queries`, where `queries[i] = [l_i, r_i]`.

For each `queries[i]`, extract the `s[l_i ... r_i]`. Then, perform the
following:
    Form a new integer `x` by concatenating all the non-zero digits from the
        substring in their original order. If there are no non-zero digits,
        `x = 0`.
    Let `sum` be the sum of digits in `x`. The answer is `x * sum`.

Return an array of integers `answer` where `answer[i]` is the answer to the
`i`th query.

Since the answers may be very large, return them modulo `10^9 + 7`.
"""

class Solution:
    def sumAndMultiply(self, s: str, queries: List[List[int]]) -> List[int]:
        """TOO SLOW"""
        ord0 = ord('0')
        M = 10**9 + 7
        digits = [ord(d) - ord0 for d in s]

        answers = []
        for l, r in queries:
            dig_sum, dig_val = 0, 0
            for d in digits[l:r + 1]:
                if d != 0:
                    dig_val = 10 * dig_val + d
                    dig_sum += d
            answers.append((dig_val * dig_sum) % M)
        
        return answers

    def sumAndMultiply(self, s: str, queries: List[List[int]]) -> List[int]:
        """TOO SLOW"""
        ord0 = ord('0')
        M = 10**9 + 7
        digits = [ord(d) - ord0 for d in s]

        cache = {}  # try a cache? UPDATE: useless; no repeated queries
        answers = []
        for l, r in queries:
            if (l, r) in cache:
                answers.append(cache[(l, r)])
                continue
            
            dig_sum, dig_val = 0, 0
            for d in digits[l:r + 1]:
                if d != 0:
                    dig_val = 10 * dig_val + d
                    dig_sum += d

            answers.append((dig_val * dig_sum) % M)
            cache[(l, r)] = answers[-1]
        
        return answers

    def sumAndMultiply(self, s: str, queries: List[List[int]]) -> List[int]:
        """faster, but still TOO SLOW"""
        ord0 = ord('0')
        M = 10**9 + 7
        digits = [ord(d) - ord0 for d in s]

        answers = []
        for l, r in queries:
            dig_sum, dig_val = 0, 0
            for d in digits[l:r + 1]:
                if d != 0:
                    dig_val = (10 * dig_val + d) % M  # avoid overflow/bignum?
                    dig_sum += d
            answers.append((dig_val * dig_sum) % M)
        
        return answers

    def sumAndMultiply(self, s: str, queries: List[List[int]]) -> List[int]:
        """MAX STR LEN EXCEEDED"""
        ord0 = ord('0')
        M = 10**9 + 7

        answers = []
        for l, r in queries:
            dig_sum = sum(ord(d) - ord0 for d in s[l:r + 1])
            dig_str = ''.join(
                d
                for d in s[l:r + 1]
                if d != '0'
            )
            dig_val = int(dig_str) if dig_str else 0
            answers.append((dig_val * dig_sum) % M)
        
        return answers

    def sumAndMultiply(self, s: str, queries: List[List[int]]) -> List[int]:
        """
        O(n) time, O(n) space solution
        
        Partial explanation:

        Let $A$ be a list of digits
        \\begin{align*}
            A &\\equiv [a_0, a_1, \\cdots, a_{n-1}]
        \\end{align*}
        where
        \\begin{align*}
            |A| &\\equiv n \\\\
            a_k &\\in \\{ 0, 1, 2, \\cdots, 9 \\}
        \\end{align*}
        and let $M \\equiv 10^9 + 7$ (a largish prime). Define the array $B$ as
        \\begin{align*}
            B[k] &\\equiv \\left( a_0 10^k + a_1 10^{k-1} + \\cdots + a_{k - 1} 10^1 + a_k 10^0 \\right) \\ (\\textrm{mod } M)
        \\end{align*}
        for $0 \\le k < n$. That is, $B[k]$ is the integer formed by the concatenation of the digits $a_0 a_1 \\cdots a_{k-1} a_k$ modulo $M$. If we want to calculate the integer $$(a_i a_{i+1} \\cdots a_{j-1} a_j) \\ (\\textrm{mod } M) \\quad \\textrm{where} \\quad 0 \\le i < j < n,$$ we can use the elements of $B$:
        \\begin{align*}
            (a_i a_{i+1} \\cdots a_{j-1} a_j) &= a_i 10^{j - i} + a_{i + 1} 10^{j - (i + 1)} + \\cdots + a_{j - 1} 10^{1} + a_j 10^{0} \\\\
            &= \\left( a_0 10^{j} + \\cdots + a_{i-1} 10^{j - (i - 1)} + a_i 10^{j - i} + \\cdots + a_j 10^{0} \\right) \\ - \\nonumber \\\\
            &\\qquad \\left( a_0 10^{i - 1} + \\cdots + a_{i - 1} 10^{0} \\right) \\cdot 10^{j - (i - 1)} \\\\
            &= B[j] - B[i - 1] \\cdot 10^{j - (i - 1)}
        \\end{align*}
        where all lines are assumed reduced modulo $M$. If we need to calculate $a_i \\cdots a_j$ for a large number of queries $(i, j)$, then this method and a pre-computed array $B$ is much, \\emph{much} faster than the na\\"ive approach.
        """
        ord0 = ord('0')
        M = 10 ** 9 + 7

        pref_vals = [0] * (len(s) + 1)  # running value of concatenated digits
        pref_sums = [0] * (len(s) + 1)  # running sum of digits
        pref_zero = [0] * (len(s) + 1)  # running count of zeros
        pv, ps, pz = 0, 0, 0
        for i, d in enumerate(s):
            if d != '0':
                d = ord(d) - ord0
                pv = (10 * pv + d) % M
                ps += d
            else:
                pz += 1
            pref_vals[i + 1] = pv
            pref_sums[i + 1] = ps
            pref_zero[i + 1] = pz

        answers = []
        for l, r in queries:
            x = pref_vals[r + 1] - pref_vals[l] * pow(
                    10,
                    r - (l - 1) - (pref_zero[r + 1] - pref_zero[l]),
                    M
                )
            s = pref_sums[r + 1] - pref_sums[l]
            answers.append((s * x) % M)
        
        return answers