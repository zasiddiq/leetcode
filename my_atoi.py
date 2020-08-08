# https://leetcode.com/explore/interview/card/top-interview-questions-easy/127/strings/884/
import re

def my_atoi(str: str) -> int:
    str = str.strip()
    str = re.findall('(^[\+\-0]*\d+)\D*', str)

    try:
        result = int(''.join(str))
        MAX_INT = 2147483647
        MIN_INT = -2147483648
        if result > MAX_INT > 0:
            return MAX_INT
        elif result < MIN_INT < 0:
            return MIN_INT
        else:
            return result
    except:
        return 0

if __name__ == '__main__':
    print( my_atoi("words and 987") )
    print( my_atoi("-91283472332") )
    print( my_atoi("-42") )
    print( my_atoi("     -42") )
    print( my_atoi("4193 with words") )
    print( my_atoi("3.14159") )
    print( my_atoi("") )
    print( my_atoi("+") )