class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operations = {'+', '-', '*', '/'}

        for token in tokens:
            if token in operations:
            # It's an operator - do the operation
                second = stack.pop()
                first = stack.pop()
                if token == '+':
                    result = first + second
                elif token == '-':
                    result = first - second
                elif token == '*':
                    result = first * second
                elif token == '/':
                    result = int(first / second)
                stack.append(result)
            else:
            # It's a number - add to stack
                stack.append(int(token))
        
        return stack[0]

        