import operator

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = {
            "+": operator.add,
            "-": operator.sub,
            "*": operator.mul,
            "/": operator.truediv
        }

        for t in tokens:
            if t in operators:
                second = stack.pop()
                first = stack.pop()
                stack.append(int(operators[t](first, second)))
            else:
                stack.append(int(t))
        
        return stack[-1]


                    
                