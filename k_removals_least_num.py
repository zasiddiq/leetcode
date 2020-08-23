# https://leetcode.com/problems/least-number-of-unique-integers-after-k-removals/
import heapq

def findLeastNumOfUniqueInts(arr, k: int) -> int:
    hashmap = {}
    for i in range(len(arr)):
        if arr[i] in hashmap:
            hashmap[arr[i]]+=1
        else:
            hashmap[arr[i]]=1
    count_arr = []
    for i in hashmap:
        count_arr.append(hashmap[i])
    heapq.heapify(count_arr)
    while len(count_arr) and k>0:
        popped = heapq.heappop(count_arr)
        if popped<=k:
            k-=popped
        else:
            k=popped-k
            heapq.heappush(count_arr,k)
            break
    return len(count_arr)


if __name__ == '__main__':
    # print(findLeastNumOfUniqueInts([5,5,4], 1))
    # print(findLeastNumOfUniqueInts([1,1], 1))
    print(findLeastNumOfUniqueInts([4,3,1,1,3,3,2], 3))
    # print(findLeastNumOfUniqueInts([2,1,1,3,3,3], 3))
    # print(findLeastNumOfUniqueInts([1,2,2,2,2], 4))