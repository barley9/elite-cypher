"""
1684. Count the Number of Consistent Strings

You are given a string `allowed` consisting of distinct characters and an array
of strings `words`. A string is consistent if all characters in the string
appear in the string `allowed`.

Return the number of consistent strings in the array `words`.
"""

class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        allowed = set(allowed)
        return sum(len(set(word) & allowed) == len(set(word)) for word in words)

    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        allowed = set(allowed)
        return sum(all(letter in allowed for letter in word) for word in words)

    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        """O(n) time, O(1) space solution using set()"""
        allowed = set(allowed)
        return sum(set(word) <= allowed for word in words)

    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        """O(n) time, O(1) space solution using lookup array"""
        orda = ord('a')  # pre-compute because we use this a lot
        table = [False] * 26  # lookup table for allowed letters
        for c in allowed:
            table[ord(c) - orda] = True
        
        count = 0  # number of allowed words
        for word in words:
            for c in word:
                if not table[ord(c) - orda]:
                    break
            else:
                count += 1

        return count

# Illegal direct output file modification, golfed version
# using file.write() instead of print() seems to offer no measurable speedup
# using all() instead of manual for-loop break seems slower??!??!
def count_strings(allowed,words):
    orda,table,result=ord('a'),[0]*26,0
    for c in allowed:table[ord(c)-orda]=1
    for w in words:result+=all(table[ord(c)-orda] for c in w)
    return result
results = []
while 1:
    try:results.append(count_strings(loads(next(sys.stdin)),loads(next(sys.stdin))))
    except StopIteration:break
with open("user.out","w") as f:print(str(results)[1:-1].replace(', ','\n'),file=f)
sys.exit(0)

def count_strings(allowed,words):
    orda,table,result=ord('a'),[1]*26,0
    for c in allowed:table[ord(c)-orda]=0
    for w in words:
        for c in w:
            if table[ord(c)-orda]:break
        else:result+=1
    return result
results = []
while 1:
    try:results.append(count_strings(loads(next(sys.stdin)),loads(next(sys.stdin))))
    except StopIteration:break
with open("user.out","w") as f:print(str(results)[1:-1].replace(', ','\n'),file=f)
sys.exit(0)