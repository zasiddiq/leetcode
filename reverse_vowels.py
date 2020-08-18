# Leetcode Sample Timed Interview
# https://leetcode.com/problems/reverse-vowels-of-a-string/

def is_vowel(c: str) -> bool:
    if c in ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'):
        return True
    return False

def reverseVowels(s: str) -> str:
    vowel_places = list()
    vowels = list()
    reversed_s = list(s)
    
    for place, c in enumerate(s):
        if is_vowel(c):
            vowels.append(c)
            vowel_places.append(place)
    
    while len( vowel_places ) > 0:
        reversed_s[ vowel_places[0] ] = vowels[-1]
        vowel_places.pop(0)
        vowels.pop()
    
    return_s = ''
    for i in reversed_s:
        return_s += i
    
    return return_s

if __name__ == '__main__':
    print( reverseVowels('hello') )
    print( reverseVowels('aA') )