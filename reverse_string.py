# https://leetcode.com/explore/interview/card/top-interview-questions-easy/127/strings/879/

def reverseString(s):
        """
        Do not return anything, modify s in-place instead.
        """
        left, right = 0, len(s) - 1
        while left < right:
            s[left], s[right] = s[right], s[left]
            left, right = left + 1, right - 1
        print("Outcome: ", s)

if __name__ == '__main__':
    reverseString(["h","e","l","l","o"]) # should be olleh