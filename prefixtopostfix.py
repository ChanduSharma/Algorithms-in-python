from collections import deque

def prefix_to_postfix(line):

    stack = deque()

    for char in reversed(line):

        if char not in "+-*/":
            stack.append(char)
        else:

            stack.append(stack.pop()+stack.pop()+char)

    print("".join(stack.pop()))


test = "*+AB-CD"

prefix_to_postfix(test)
