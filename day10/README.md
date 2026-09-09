# Day 10 - Maximum Subarray

## Problem

The goal is to find the contiguous subarray with the largest possible sum.

For example:

`[-2, 1, -3, 4, -1, 2, 1, -5, 4]`

The maximum subarray is:

`[4, -1, 2, 1]`

Its sum is:

`6`

## Approach

I used Kadane's Algorithm.

The algorithm keeps track of two values:

* `current_sum` - the best subarray sum ending at the current position.
* `max_sum` - the largest subarray sum found so far.

For every number, the algorithm decides whether it is better to:

1. Add the number to the existing subarray.
2. Start a new subarray from the current number.

If the existing running sum becomes disadvantageous, we start a new subarray.

## Time Complexity

The array is traversed only once.

Time Complexity: **O(N)**

The main algorithm uses constant extra space: **O(1)**.

## Real-World Usage

Maximum subarray logic can be useful in financial systems and analytics platforms for finding the best continuous period in a sequence of values.

For example, a financial analytics system could use a similar approach to identify a continuous period with the highest overall gain. The same pattern can also be applied to other time-series and activity data.

## Key Learning

The main takeaway from this problem is that we do not always need to check every possible subarray. By keeping track of a running sum and making a decision at each step, we can solve the problem efficiently in O(N) time.
