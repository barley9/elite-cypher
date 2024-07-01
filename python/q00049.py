"""
49. Group Anagrams

Given an array of strings `strs`, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.
"""

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        orda = ord('a')
        result = {}

        for word in strs:
            # Create counter "hash" of `word`
            counter = [0] * 26
            for c in word:
                counter[ord(c) - orda] += 1
            counter = tuple(counter)  # make immutable

            # Group words with same counter
            if counter in result:
                result[counter].append(word)
            else:
                result[counter] = [word]
        
        return list(result.values())

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = {}

        for word in strs:
            s = ''.join(sorted(word))  # different hashing idea
            if s in result:
                result[s].append(word)
            else:
                result[s] = [word]
        
        return list(result.values())