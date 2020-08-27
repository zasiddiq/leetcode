# https://leetcode.com/problems/longest-substring-without-repeating-characters/

# https://leetcode.com/problems/longest-substring-without-repeating-characters/

def lengthOfLongestSubstring(s: str) -> int:
    charSet = set()
    res, l = 0, 0
    
    for r in range(len(s)):
        while s[r] in charSet:
            charSet.remove(s[l])
            l += 1
        charSet.add(s[r])
        res = max(res, r - l + 1)
    return res


if __name__ == "__main__":
    print( lengthOfLongestSubstring("abcabcbb") )