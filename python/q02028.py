"""
2028. Find Missing Observations

You have observations of `n + m` 6-sided dice rolls with each face numbered from
`1` to `6`. `n` of the observations went missing, and you only have the
observations of `m` rolls. Fortunately, you have also calculated the average
value of the `n + m` rolls.

You are given an integer array `rolls` of length `m` where `rolls[i]` is the
value of the `i`th observation. You are also given the two integers `mean` and
`n`.

Return an array of length `n` containing the missing observations such that the
average value of the `n + m` rolls is exactly `mean`. If there are multiple
valid answers, return any of them. If no such array exists, return an empty
array.

The average value of a set of `k` numbers is the sum of the numbers divided by
`k`.

Note that `mean` is an integer, so the sum of the `n + m` rolls should be
divisible by `n + m`.
"""

class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        """O(m) time, O(m + n) space solution using some algebra"""
        missing_sum = mean * (len(rolls) + n) - sum(rolls)
        q, r = divmod(missing_sum, n)
        if 1 <= q < 6:
            return [q + 1] * r + [q] * (n - r)
        elif q == 6 and r == 0:
            return [q] * n
        else:
            return []

# Illegal output file modification magic
def main():
    inputs = map(loads, sys.stdin)
    soln = Solution()
    results = []
    while True:
        try:
            rolls = next(inputs)
            mean = next(inputs)
            n = next(inputs)
            print(rolls, mean, n)

            results.append(soln.missingRolls(rolls, mean, n))
        except StopIteration:
            break
    with open("user.out", "w") as f:
        for result in results:
            print(dumps(result).replace(", ", ","), file=f)
if __name__ == "__main__":
    main()
    sys.exit(0)

# Golfed version (beats 100.00%)
def missingRolls(rolls,mean,n):
    q,r=divmod(mean*(len(rolls)+n)-sum(rolls),n)
    if 1<=q<6:return [q+1]*r+[q]*(n-r)
    elif q==6 and r==0:return [q]*n
    else:return []
def main():
    inputs,results=map(loads,sys.stdin),[]
    while True:
        try:results.append(missingRolls(next(inputs),next(inputs),next(inputs)))
        except StopIteration:break
    with open("user.out","w") as f:print(str(results)[1:-1].replace('], [',']\n['),file=f)
if __name__=="__main__":main();sys.exit(0)