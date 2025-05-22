# 3362. Zero Array Transformation III
* **Will revisit this problem again**

## LeetCode Link
[3362. Zero Array Transformation III](https://leetcode.com/problems/zero-array-transformation-iii/description/)

## Problem Description
You are given an integer array nums of length n and a 2D array queries where queries[i] = [li, ri].

Each queries[i] represents the following action on nums:

Decrement the value at each index in the range [li, ri] in nums by at most 1.
The amount by which the value is decremented can be chosen independently for each index.
A Zero Array is an array with all its elements equal to 0.

Return the maximum number of elements that can be removed from queries, such that nums can still be converted to a zero array using the remaining queries. If it is not possible to convert nums to a zero array, return -1.

## Initial Thought Process & Brute Force
Was going in the wrong direction only managed to clear a few test cases. 

## Optimized Approach
Turns out i needed to use the concept of difference array.

### Editorial Solution
First, we consider the element at index 0 in nums. If nums[0]>0, we must find at least nums[0] elements in queries with left endpoints of 0 to retain so that nums[0] can be reduced to 0. Now, which elements of nums[0] should we choose? Greedily, we should select those with the largest right endpoints. After this selection, we move on to nums[1]. The elements selected in the previous step may not include index 1, and we need to remove them. This can be accomplished using the difference array deltaArray.

At this point, the cumulative number of operations may not be enough to reduce nums[1] to 0, and we need to select elements from queries, similar to the previous step. We can select the elements with the largest right endpoints from the portion of unselected elements whose left endpoints are ≤1 until the number of operations satisfies the condition to reduce nums[1] to 0. This calculation can be efficiently handled using a priority queue (or heap).

As we traverse nums, we continuously insert the right endpoints of the queries corresponding to the left endpoints into the heap. When the number of operations is insufficient, we keep extracting the largest right endpoint from the heap until the required number of operations is met. After completing the traversal, the size of the heap represents the number of queries that can be deleted.

### Time Complexity
$O(n + m * Logm)$

### Space Complexity
$O(n + m)$

## Code
```python
# Python solution
class Solution:
    def maxRemoval(self, nums: List[int], queries: List[List[int]]) -> int:
        queries.sort(key=lambda x: x[0])
        heap = []
        deltaArray = [0] * (len(nums) + 1)
        operations = 0
        j = 0
        for i, num in enumerate(nums):
            operations += deltaArray[i]
            while j < len(queries) and queries[j][0] == i:
                heappush(heap, -queries[j][1])
                j += 1
            while operations < num and heap and -heap[0] >= i:
                operations += 1
                deltaArray[-heappop(heap) + 1] -= 1
            if operations < num:
                return -1
        return len(heap)

