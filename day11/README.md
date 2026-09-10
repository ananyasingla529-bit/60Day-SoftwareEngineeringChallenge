# Day 11 - Move Zeroes

## Problem

The goal is to move all zeroes in an array to the end while maintaining the original order of all non-zero elements.

Example:

`[0, 1, 0, 3, 12]`

becomes:

`[1, 3, 12, 0, 0]`

## Approach

I used an in-place approach with a `position` variable.

The `position` variable keeps track of where the next non-zero element should be placed.

I scan through the array and whenever I find a non-zero value, I place it at the current `position` and move the position forward.

After all non-zero elements have been placed at the beginning, the remaining positions are filled with zeroes.

## Why This Maintains Order

The array is scanned from left to right, so the non-zero elements are placed in the same order in which they originally appeared.

For example:

`[0, 1, 0, 3, 12]`

The non-zero elements are encountered as:

`1 → 3 → 12`

Therefore, they remain in that order.

## Complexity

**Time Complexity:** O(N)

The array is traversed once.

**Space Complexity:** O(1)

No additional array is created. The original array is modified in place.

## Real-World Usage

In-place operations are useful when working with large amounts of data where creating additional copies of the data would use unnecessary memory.

Similar techniques can be useful in memory-efficient data processing systems, large datasets, and systems where memory usage needs to be controlled.

## Key Learning

The main lesson from this problem is that we can modify an existing data structure efficiently instead of creating a new one. This can reduce memory usage while still maintaining the required order of the data.
