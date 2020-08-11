def product_except_self(nums: list) -> list:
    count = 0
    m = list()
    final = list()
    while count != len(nums):
        for i in nums:
            m.append(i)
        del m[count]
        count += 1
        num = 1
        for i in m:
            num *= i
        final.append(num)
        m = list()
    return final

if __name__ == '__main__':
    print( product_except_self([1,2,3,4]) ) # should be [24,12,8,6]