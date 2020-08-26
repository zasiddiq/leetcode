# https://leetcode.com/problems/container-with-most-water/solution/
# Two Pointer Approach
# Time Complexity: O(n) - single pass
# Space Complexity: O(1) - only used left and right pointers, no extra data structures

def maxArea(height):
    left = 0
    right = len(height) - 1
    max_area = 0

    while left < right:
        max_area = max(max_area, min(height[left], height[right]) * (right - left))
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1
    return max_area

if __name__ == "__main__":

    print(maxArea([1,8,6,2,5,4,8,3,7])) # should be 49

    print(maxArea([1,2,1])) # should be 2

    print(maxArea([2,3,10,5,7,8,9]) ) # should be 36, got 14