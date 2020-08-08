def strStr(haystack: str, needle: str) -> int:
    if len(needle) > len(haystack):
        return -1
    if haystack == needle:
        return 0
    if needle == '' and haystack == '':
        return 0
    if needle == '':
        return 0
    if haystack == '':
        return -1

    m = len(haystack)
    n = len(needle)

    for i in range(m-n+1):
        if haystack[i] == needle[0] and haystack[i:i+n] == needle:
            return i
    return -1

if __name__ == '__main__':
    print( strStr('hello', 'll') ) # 2
    print( strStr('hello', 'e') ) # 1
    print( strStr('hello', 'h') ) # 0
    print( strStr('hello', '') ) # 0
    print( strStr('aaaaa', 'bba') ) # -1
    print( strStr('mississippi', 'a') ) # -1
    print( strStr('mississippi', 'issi') ) # 1
    print( strStr('mississippi', 'issip') ) # 4
