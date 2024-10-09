"""
921. Minimum Add to Make Parentheses Valid

A parentheses string is valid if and only if:
    It is the empty string,
    It can be written as `AB` (`A` concatenated with `B`), where `A` and `B`
        are valid strings, or
    It can be written as `(A)`, where `A` is a valid string.

You are given a parentheses string `s`. In one move, you can insert a
parenthesis at any position of the string.
    For example, if s = "()))", you can insert an opening parenthesis to be
        "(()))" or a closing parenthesis to be "())))".

Return the minimum number of moves required to make `s` valid.
"""

class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        """O(n) time, O(n) space solution using a stack"""
        stack = []
        unmatched = 0
        for c in s:
            if c == '(':
                stack.append(c)
            elif stack:
                if stack[-1] == '(':
                    stack.pop()  # we found a matched pair; pop() and don't increment
                else:
                    unmatched += 1
            else:
                unmatched += 1
        return unmatched + len(stack)

    def minAddToMakeValid(self, s: str) -> int:
        stack = []
        unmatched = 0
        for c in s:
            if c == '(':
                stack.append(c)
            else:
                if stack and stack[-1] == '(':
                    stack.pop()
                else:
                    unmatched += 1
        return unmatched + len(stack)

    def minAddToMakeValid(self, s: str) -> int:
        stack,unmatched=[None],0  # `None` sentinel to obviate checking empty stack case
        for c in s:
            if c=='(':stack.append(c)
            else:
                if stack[-1]=='(':del stack[-1]
                else:unmatched+=1
        return unmatched+len(stack)-1

    def minAddToMakeValid(self,s):
        """O(n) time, O(1) space solution using counters"""
        count_left,unmatched=0,0
        for c in s:
            if c=='(':count_left+=1
            else:
                count_left-=1
                if count_left<0:count_left=0;unmatched+=1
        return unmatched+count_left

# Output file manipulation magic (still only beats 65%?!?)
def minAddToMakeValid(s):
    stack,unmatched=[None],0
    for c in s:
        if c=='(':stack.append(c)
        else:
            if stack[-1]=='(':del stack[-1]
            else:unmatched+=1
    return unmatched+len(stack)-1
inputs,results=map(loads,sys.stdin),[]
while True:
    try:results.append(minAddToMakeValid(loads(next(sys.stdin))))
    except StopIteration:break
with open("user.out",'w') as f:f.write(str(results)[1:-1].replace(', ','\n')+'\n')
sys.exit(0)