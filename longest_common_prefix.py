# https://leetcode.com/explore/interview/card/top-interview-questions-easy/127/strings/887/

def longest_common_prefix(strs: list) -> str:
    if len(strs) == 0:
        return ''
    for i in strs:
        if i == '':
            return ''

    check = strs[0][0:1]
    pointer = 0
    str = ''
    while True:
        for i in strs:
            if check == i[pointer]:
                add = i[pointer]
            else:
                return str
        str += add
        pointer += 1
        for i in strs:
            if pointer >= len(i):
                 return str
        check = strs[0][pointer]
        
    return str

if __name__ == '__main__':
    print( longest_common_prefix(["flower","flow","flight"]) ) # should be fl
    print( longest_common_prefix(["dog","racecar","car"]) ) # should be ''
    print( longest_common_prefix(["zain","za","z"]) ) # should be z
    print( longest_common_prefix(["z","za","z"]) ) # should be z
    print( longest_common_prefix(["zain","zain","zain"]) ) # should be zain

    print( longest_common_prefix(["a","",""]) ) # should be ''
    print (longest_common_prefix([]) ) # should be ''
