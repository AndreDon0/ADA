def is_valid_brackets(expression):
    brackets = {')': '(', ']': '[', '}': '{', '>': '<'}
    stack = []

    for char in expression:
        if char in brackets.values():
            stack.append(char)
        elif char in brackets.keys():
            if not stack or brackets[char] != stack.pop():
                return "NO"

    return "YES" if not stack else "NO"


s = input()
print(is_valid_brackets(s))
