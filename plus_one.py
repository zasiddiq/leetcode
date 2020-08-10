# https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/559/

def plus_one(digits):
    plus_one_list = list()
    for count, d in enumerate(digits):
        if d == digits[-1] and d != 9 and count == len(digits)-1:
            plus_one_list.append(d+1)
        elif count == len(digits)-1 and d == 9:
            index = len(digits) - 2
            plus_one_list.append(0)
            while plus_one_list[index] == 9:
                plus_one_list[index] = 0
                index -= 1
            if index == -1:
                plus_one_list.insert(0, 1)
            else:
                plus_one_list[index] += 1
        else:
            plus_one_list.append(d)

    return plus_one_list

if __name__ == '__main__':
    print( plus_one([1,2,3]) ) # should be 124
    print( plus_one([4,3,2,1]) ) # should be 4322
    print( plus_one([9]) ) # should be 10
    print( plus_one([5,2,9]) ) # should be 530
    print( plus_one([5,9,9]) ) # should be 600
    print( plus_one([7,9,9,9]) ) # should be 8000
    print( plus_one([9,9,9,9]) ) # should be 10,000
    print( plus_one([9,9]) ) # should be 100
    print( plus_one([1,0,0,0,0]) ) # should be 10,001