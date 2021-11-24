def reverseWords(s):
    sp = s.split(" ")
    for i in range(len(sp)):
        sp[i] = sp[i][::-1]

    return " ".join(sp)
        




s = "Let's take LeetCode contest"
print(reverseWords(s))