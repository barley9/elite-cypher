"""
150. Evaluate Reverse Polish Notation

You are given an array of strings tokens that represents an arithmetic expression in a Reverse Polish Notation.

Evaluate the expression. Return an integer that represents the value of the expression.

Note that:
    The valid operators are '+', '-', '*', and '/'.
    Each operand may be an integer or another expression.
    The division between two integers always truncates toward zero.
    There will not be any division by zero.
    The input represents a valid arithmetic expression in a reverse polish notation.
    The answer and all the intermediate calculations can be represented in a 32-bit integer.
"""

import operator

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = {
            '+' : operator.add,
            '-' : operator.sub,
            '*' : operator.mul,
            '/' : lambda a, b: int(operator.truediv(a, b)),
        }

        stack = []
        for t in tokens:
            if t in operators:
                op2 = stack.pop()
                op1 = stack.pop()
                stack.append(operators[t](op1, op2))
            else:
                stack.append(int(t))

        return stack.pop()
            