def is_balanced(expression):
    stack = []
    opening = "{(["
    closing = "])}"
    for c in "{([])}":
        for x in expression:
            if x == c:
                stack.append(x)
    return stack


print(is_balanced("{[()]}"))       # Nested correctly
print(is_balanced("{[}]"))         # Incorrect nesting order
print(is_balanced("(]"))           # Mismatched types
print(is_balanced("((()))"))       # Simple nesting
print(is_balanced("print(list[0])")) # Code with text (valid)
print(is_balanced("((("))          # Unclosed
print(is_balanced("]"))            # Closing without opening