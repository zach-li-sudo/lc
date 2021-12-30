def addStrings(num1, num2):
    # elementary math
    if num1 is None:
        return num2
    elif num2 is None:
        return num1

    p1 = len(num1) - 1
    p2 = len(num2) - 1

    carry = 0
    res = []

    while p1 >= 0 or p2 >= 0:
        x1 = ord(num1[p1]) - ord('0') if p1 >= 0 else 0
        x2 = ord(num2[p2]) - ord('0') if p2 >= 0 else 0
        value = (x1 + x2 + carry) % 10
        carry = (x1 + x2 + carry) // 10
        res.append(value)
        p1 -= 1
        p2 -= 1
    
    if carry:
        res.append(carry)
    
    return "".join(str(x) for x in res[::-1])
        


num1 = "1789"
num2 = "15"
addStrings(num1, num2)