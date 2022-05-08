def swap_case(s):
    newS = ""
    for i in range(len(s)):
        if s[i].isupper():
            newS += s[i].lower()
        elif s[i].islower():
            newS += s[i].upper()
        else:
            newS += s[i]
    return newS

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)