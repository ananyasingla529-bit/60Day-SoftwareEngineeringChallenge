# Day 9 - Prefix Sum Optimization

## What is a Prefix Sum?

A prefix sum array stores the cumulative sum of the elements up to each position.

For example:

Original array:

`[2, 4, 6, 8, 10]`

Prefix sum:

`[2, 6, 12, 20, 30]`

Each value represents the sum of all previous values up to that index.

## Why use Prefix Sums?

If we calculate every range sum using a loop, we may have to repeatedly process the same elements.

With prefix sums, we can answer a range-sum query in constant time.

For a query from index `left` to `right`:

`range_sum = prefix[right] - prefix[left - 1]`

If `left` is 0, the answer is simply `prefix[right]`.

## Time Complexity

### Brute Force

Each query can take O(N) time in the worst case.

For Q queries:

`O(N × Q)`

### Prefix Sum

Building the prefix array takes:

`O(N)`

Each query takes:

`O(1)`

Therefore, for Q queries:

`O(N + Q)`

## Real-World Use

Prefix sums can be useful in analytics systems and dashboards where users repeatedly request totals over different ranges. For example, a dashboard could store daily sales and quickly answer questions such as total sales between two dates without recalculating the entire range each time.
