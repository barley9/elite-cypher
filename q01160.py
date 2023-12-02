"""
1160. Find Words That Can Be Formed by Characters

You are given an array of strings `words` and a string `chars`.
A string is good if it can be formed by characters from `chars` (each character can only be used once).
Return the sum of lengths of all good strings in `words`.
"""


import collections

class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        """Simple solution using a list to store character frequencies"""
        
        def getCharCounter(string: str) -> list:
            """Returns a list containing the number of occurances of each english letter in `string`"""
            counter = [0] * 26
            for c in string:
                counter[ord(c) - ord('a')] += 1
            return counter

        chr_counter = getCharCounter(chars)
        
        good_words = []
        for word in words:
            wd_counter = getCharCounter(word)
            if all(chr_counter[i] >= wd_counter[i] for i in range(26)):
                good_words.append(word)

        return sum(len(word) for word in good_words)
    
    def countCharacters(self, words: List[str], chars: str) -> int:
        """Essentially identical solution to that above, with minor optimizations"""
        orda = ord('a')

        chrcount = [0] * 26
        for c in chars:
            chrcount[ord(c) - orda] += 1

        result = 0
        wrdcount = [0] * 26
        for word in words:
            wrdcount[:] = (0 for _ in range(len(wrdcount)))  # reset all to 0
            for c in word:
                wrdcount[ord(c) - orda] += 1
            if all(chrcount[i] >= wrdcount[i] for i in range(len(wrdcount))):
                result += len(word)

        return result

    def countCharacters(self, words: List[str], chars: str) -> int:
        """
        Solution using builtin Counter objects. Time complexity O(
            len(chars) + 
            2 * sum(len(word) for word in words)
        ) and space complexity O(
            len(chars) + 
            max(len(word) for word in words)
        )
        """
        chars = collections.Counter(chars)  # implements the bag/multiset/counter data structure
        
        result = 0
        for word in words:
            wordcount = collections.Counter(word)
            if all(chars[c] >= wordcount[c] for c in wordcount):
                result += len(word)
        
        return result