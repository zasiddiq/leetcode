def restoreString(s: str, indices) -> str:   
    shuffle_list = [''] * len(s)
    
    for i, c in zip(indices, s):
        shuffle_list[i] = c
    
    shuffle_string = ''
    for i in shuffle_list:
        shuffle_string += i
    
    return shuffle_string

if __name__ == '__main__':
    print( restoreString('codeleet', [4,5,6,7,0,2,1,3] ) )
