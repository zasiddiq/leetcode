from collections import defaultdict

def groupAnagrams(strs):

    anagramDict = defaultdict(list)

    for word in strs:
        sortedWord = sorted(word)
        anagramDict[tuple(sortedWord)].append(word)

    return anagramDict.values()



strss = strs = ["eat","tea","tan","ate","nat","bat"]
print(groupAnagrams(strs))