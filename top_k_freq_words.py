# https://leetcode.com/problems/top-k-frequent-words/
from collections import defaultdict

class Solution:
    def same_check(self, hash_map):
        all_same = True
        for word in hash_map:
            if hash_map[word] > 1:
                all_same = False
        return all_same

    def topKFrequent(self, words, k: int):
        
        hash_map = defaultdict(int)
        
        for word in words:
            hash_map[word] += 1
        
        freq_list = []
        
        for word in range(k):
            if self.same_check(hash_map):
                freq_list.append(min(hash_map))
                del hash_map[min(hash_map)]
            else:
                max_val = 0
                most_freq_word = ''
                for i in hash_map.items():
                    if i[1] > max_val:
                        max_val = i[1]
                        most_freq_word = i[0]
                    if i[1] == max_val:
                        if i[0] < most_freq_word:
                            most_freq_word = i[0]

                freq_list.append( most_freq_word)
                del hash_map[most_freq_word]

        return freq_list

if __name__ == "__main__":
    x = Solution()
    print(x.topKFrequent(["i", "love", "leetcode", "i", "love", "coding"], 3))
    print(x.topKFrequent(["a","aa","aaa"], 2))

    print(x.topKFrequent(["plpaboutit","jnoqzdute","sfvkdqf","mjc","nkpllqzjzp","foqqenbey","ssnanizsav","nkpllqzjzp","sfvkdqf","isnjmy","pnqsz","hhqpvvt","fvvdtpnzx","jkqonvenhx","cyxwlef","hhqpvvt","fvvdtpnzx","plpaboutit","sfvkdqf","mjc","fvvdtpnzx","bwumsj","foqqenbey","isnjmy","nkpllqzjzp","hhqpvvt","foqqenbey","fvvdtpnzx","bwumsj","hhqpvvt","fvvdtpnzx","jkqonvenhx","jnoqzdute","foqqenbey","jnoqzdute","foqqenbey","hhqpvvt","ssnanizsav","mjc","foqqenbey","bwumsj","ssnanizsav","fvvdtpnzx","nkpllqzjzp","jkqonvenhx","hhqpvvt","mjc","isnjmy","bwumsj","pnqsz","hhqpvvt","nkpllqzjzp","jnoqzdute","pnqsz","nkpllqzjzp","jnoqzdute","foqqenbey","nkpllqzjzp","hhqpvvt","fvvdtpnzx","plpaboutit","jnoqzdute","sfvkdqf","fvvdtpnzx","jkqonvenhx","jnoqzdute","nkpllqzjzp","jnoqzdute","fvvdtpnzx","jkqonvenhx","hhqpvvt","isnjmy","jkqonvenhx","ssnanizsav","jnoqzdute","jkqonvenhx","fvvdtpnzx","hhqpvvt","bwumsj","nkpllqzjzp","bwumsj","jkqonvenhx","jnoqzdute","pnqsz","foqqenbey","sfvkdqf","sfvkdqf"]
, 1))

    print(x.topKFrequent(["b", "b", "a", "a"], 1))