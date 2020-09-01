from collections import defaultdict

def top_k(elem, k):
    arr = [ [] for i in range(len(elem)+1) ]
    freq_dict = defaultdict(int)
    for i in elem:
        freq_dict[i] += 1
    for index,val in freq_dict.items():
        # arr[index].append(val)
        arr[val].append(index)
    output_arr = []
    arr.reverse()
    for k_value, i in enumerate(arr):
        if len(output_arr) == k:
            return output_arr
        if len(i) != 0:
            output_arr.append(i[0])

if __name__ == '__main__':
    print( top_k([1,2], 2 ) ) 
    # print( top_k([1,1,1,2,2,3], 2 ) )
    # print( top_k([-1,-1], 1 ) ) 