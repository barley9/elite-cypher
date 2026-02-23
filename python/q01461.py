"""
1461. Check If a String Contains All Binary Codes of Size K

Given a binary string `s` and an integer `k`, return `true` if every binary
code of length `k` is a substring of `s`. Otherwise, return `false`.
"""

class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        """O(len(s) * 2^k) time, O(k * 2^k) space; TOO SLOW"""
        codes = [
            f"{i:0>{k}b}"
            for i in range(1 << k)
        ]
        # print(codes)

        return all(
            code in s
            for code in codes
        )

    def hasAllCodes(self, s: str, k: int) -> bool:
        """O(len(s) * k) time, O(k * 2^k) space"""
        codes = {
            f"{i:0>{k}b}"
            for i in range(1 << k)
        }
        
        for i in range(len(s) - (k - 1)):
            sub = s[i:i + k]
            # print(sub)
            if sub in codes:
                codes.remove(sub)
            
            if not codes:
                return True
        
        return False

    def hasAllCodes(self, s: str, k: int) -> bool:
        """
        O(len(s) * k) time, O(k * 2^k) space solution

        It looks like joining strings is faster than slicing them...
        """
        sub = list(s[:k])  # substring
        codes = {''.join(sub)}  # set of unique `k`-length codes
        # print(''.join(sub), codes)
        
        for i in range(k, len(s)):
            # advance sliding window
            sub.append(s[i])
            del sub[0]
            
            # add substring to set of codes
            codes.add(''.join(sub))
            
            # print(''.join(sub), codes)
        
        return len(codes) == 1 << k