import textwrap


def wrap(string, max_width):
    a = 0
    width = max_width
    strNew = ""
    for i in range(len(string)//width+1):
        strWrap = string[a:max_width] + "\n"
        # print(strWrap)
        strNew += strWrap
        a += width
        max_width += width
    return strNew


if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)
