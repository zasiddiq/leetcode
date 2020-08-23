# https://leetcode.com/problems/group-anagrams/

def groupAnagrams(strs):
    anagram_dict = {}
    for i in strs:
        if ''.join(sorted(i)) in anagram_dict:
            anagram_dict[''.join(sorted(i)) ].append(i)
        else:
            anagram_dict[''.join(sorted(i)) ] = list()
            anagram_dict[''.join(sorted(i)) ].append(i) 

    return_list = list()
    for d in anagram_dict.values():
        return_list.append(d)

    return return_list


if __name__ == '__main__':
    print ( groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]) )
#     [
#   ["ate","eat","tea"],
#   ["nat","tan"],
#   ["bat"]
# ]