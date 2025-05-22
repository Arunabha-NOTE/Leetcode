# 3355. Zero Array Transformation I
* **Will revisit this problem again**

## LeetCode Link
[Zero Array Transformation I](https://leetcode.com/problems/zero-array-transformation-i/description/)

## Problem Description
You are given an integer array nums of length n and a 2D array queries, where queries[i] = [li, ri].

For each queries[i]:

Select a subset of indices within the range [li, ri] in nums.
Decrement the values at the selected indices by 1.
A Zero Array is an array where all elements are equal to 0.

Return true if it is possible to transform nums into a Zero Array after processing all the queries sequentially, otherwise return false.

## Initial Thought Process & Brute Force
Tried to iterate the length of queries and made changes to array as per problem and query one by one. This did not end up working out.

## Optimized Approach
Unable to figure out this one by myself i turn to editorial for help. Turns out i need to learn the concept of prefix sum first. 

### Editorial Solution
We count the maximum number of operations that can be performed at each position using a difference array. Construct the difference array deltaArray with a length of n + 1 (where n is the length of the array nums), which is used to record the increment for each query on the number of operations.

For each query interval [left, right], increment deltaArray[left] by +1, indicating an increase in the operation count starting from left. Decrement deltaArray[right + 1] by -1, indicating that the operation count returns to its original value after right + 1.

Next, perform a prefix sum accumulation on the difference array deltaArray to obtain the total operation count at each position in the array, storing these counts in operationCounts. Traverse the nums array and the operationCounts array, comparing the actual operation counts (operations) at each position to see if they meet the minimum number of operations (target) required for zeroing. If all positions meet operations >= target, return true; otherwise, return false.

### Time Complexity
$O(N + M)$ We need O(m) time to construct the difference array, followed by checking all O(n) positions.

### Space Complexity
$O(N)$ We need O(n) space to store the difference array.

## Code
```python
# Python solution
class Solution:
    def isZeroArray(self, nums: List[int], queries: List[List[int]]) -> bool:
        deltaArray = [0] * (len(nums) + 1)
        for left, right in queries:
            deltaArray[left] += 1
            deltaArray[right + 1] -= 1
        operationCounts = []
        currentOperations = 0
        for delta in deltaArray:
            currentOperations += delta
            operationCounts.append(currentOperations)
        for operations, target in zip(operationCounts, nums):
            if operations < target:
                return False
        return True

