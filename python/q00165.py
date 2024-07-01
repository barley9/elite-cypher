"""
165. Compare Version Numbers

Given two version strings, `version1` and `version2`, compare them. A version
string consists of revisions separated by dots '.'. The value of the revision is
its integer conversion ignoring leading zeros.

To compare version strings, compare their revision values in left-to-right
order. If one of the version strings has fewer revisions, treat the missing
revision values as `0`.

Return the following:
    If `version1 < version2`, return `-1`.
    If `version1 > version2`, return `1`.
    Otherwise, return `0`.
"""

class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        # Split strings to tuples of ints
        v1 = tuple(int(n) for n in version1.split('.'))
        v2 = tuple(int(n) for n in version2.split('.'))

        # Strip off trailing zeros
        lastNonZero = 0
        for i in range(len(v1)):
            if v1[i] != 0:
                lastNonZero = i
        v1 = v1[:lastNonZero + 1]
        # print(v1, v2)

        lastNonZero = 0
        for i in range(len(v2)):
            if v2[i] != 0:
                lastNonZero = i
        v2 = v2[:lastNonZero + 1]
        # print(v1, v2)

        return 0 if v1 == v2 else 2 * (v1 > v2) - 1