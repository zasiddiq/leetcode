# https://leetcode.com/explore/interview/card/top-interview-questions-easy/127/strings/880/

def reverse(x: int) -> int:
    s = [str(x) for x in str(x)]
    start = 0
    end = len(s) - 1
    while start < end:
        if s[start] == '-':
            start += 1
            continue
        s[start], s[end] = s[end], s[start]
        start += 1
        end -= 1
    
    return_string = ''
    for s in s:
        return_string += s

    if int(return_string) > 2**31 - 1 or int(return_string) < -2**31:
        return 0
    return int(return_string)

if __name__ == '__main__':
    print( reverse(123) ) # should be 321
    print( reverse(-123) ) # should be -321
    print( reverse(120) ) # should be 120
    print( reverse(1534236469) ) # should be 0
    print( reverse(-2147483648) ) # should be 0

