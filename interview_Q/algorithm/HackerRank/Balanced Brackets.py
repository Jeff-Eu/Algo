def isBalanced(s):
    stack = []
    for c in s:
        if c == '{' or c == '[' or c == '(':
            stack.append(c)
        else:
            if stack:
                p = stack.pop()
                if c == '}' and p != '{':
                    return "NO"
                elif c == ')' and p != '(':
                    return "NO"
                elif c == ']' and p != '[':
                    return "NO"
            else:
                return "NO"

    if not stack:
        return "YES"
    else:
        return "NO"

print isBalanced("{([])}")
print isBalanced("[](){()}")