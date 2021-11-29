def isValid(s):
    if len(s) % 2 is not 0: return False

    openings = ['{', '(', '[']
    closings = ['}', ')', ']']

    def is_paired(o, c):
        return openings.index(o) == closings.index(c)

    stack = []

    for p in s:
        if p in openings:
            stack.append(p)
        else:
            try:
                if is_paired(stack[-1], p):
                    stack.pop(-1)
                else:
                    return False
            except:
                return False
    if stack:
        return False
    return True

# s = "()"
# s = "()[]{}"
# s = "(]"
# s = "([)]"
s = "{{"
print(isValid(s))