# 135. Candy

## LeetCode Link
[135. Candy](https://leetcode.com/problems/candy/description/)

## Problem Description
There are n children standing in a line. Each child is assigned a rating value given in the integer array ratings.

You are giving candies to these children subjected to the following requirements:

Each child must have at least one candy.
Children with a higher rating get more candies than their neighbors.
Return the minimum number of candies you need to have to distribute the candies to the children.

Example 1:

Input: ratings = [1,0,2]  
Output: 5
Explanation: You can allocate to the first, second and third child with 2, 1, 2 candies respectively.

Example 2:

Input: ratings = [1,2,2]
Output: 4
Explanation: You can allocate to the first, second and third child with 1, 2, 1 candies respectively.
The third child gets 1 candy because it satisfies the above two conditions.

## Optimized Approach


### Time Complexity
$O(N)$

### Space Complexity
$O(n)$

## Code
```python
# Python solution
class Solution:
    def candy(self, ratings: List[int]) -> int:
        # Taking length of the the array
        n = len(ratings)
        # Initialize count to 0
        count = 0
        # Create a array candies to count allocation of candies.
        # To satisfy question every child starts with one candy.
        candies = [1] * n
        # Forward pass
        for i in range(1,n):
            # if rating of current child is higher than the previous child
            if ratings[i] > ratings[i - 1]:
                # Edit current childs candy by giving him the amount previous child has + 1
                candies[i] = candies[i-1] + 1
        # Backward Pass
        for i in range(n-1, 0, -1):
            # If rating of previous child is higher than current
            if ratings[i-1] > ratings[i]:
                # Give previous child the max between the candies he currently has
                # or the current child's candies + 1
                candies[i-1] = max(candies[i] + 1, candies[i-1])
            # Add number of candies to count in every pass
            count += candies[i - 1]
        # Return the count + the no of candies in last index of array candies
        return count + candies[n - 1]
