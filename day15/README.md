# Day 15 - Duplicate Detection

## Phase

Algorithmic Thinking

## Problem

A secret agency intercepted a list of agent IDs and needs to check whether any duplicate IDs exist.

The goal of this task is to implement duplicate detection using two different approaches:

1. Brute-force comparison
2. Optimized approach using sets

The two approaches are then compared based on time complexity and execution speed.

## Approach 1 - Brute Force

The brute-force solution compares every ID with every other ID.

If two IDs are equal, a duplicate has been found.

### Complexity

* **Time Complexity:** `O(N²)`
* **Space Complexity:** `O(1)`

This approach is simple but becomes very slow when the dataset becomes large.

## Approach 2 - Using Set

The optimized solution uses a Python set to keep track of IDs that have already been seen.

For every ID:

* If it is already in the set, a duplicate exists.
* Otherwise, it is added to the set.

### Complexity

* **Time Complexity:** `O(N)` average
* **Space Complexity:** `O(N)`

This approach is much more efficient for large datasets.

## Example

**Input:**

```text
101, 205, 309, 412, 518, 620, 735, 842, 950, 101
```

**Output:**

```text
Brute-force result: True
Set result: True
```

The ID `101` appears more than once, so a duplicate exists.

## Execution Speed Comparison

The program uses Python's `time` module to measure how long each approach takes.

For a small dataset, the difference may not be very noticeable.

However, as the number of IDs increases, the brute-force approach becomes significantly slower because its number of comparisons grows quadratically.

## Scaling to 1 Million IDs

For 1 million IDs:

### Brute Force

`O(N²)`

This could require approximately:

```text
500 billion pair comparisons
```

in the worst case, making it impractical for such a large dataset.

### Set

`O(N)` average

The IDs are processed in a single pass, making the set-based solution much more practical for large datasets.

## Comparison

| Approach    | Time         | Space | Scalability |
| ----------- | ------------ | ----- | ----------- |
| Brute Force | O(N²)        | O(1)  | Poor        |
| Set         | O(N) average | O(N)  | Good        |

## Real-World Applications

Duplicate detection is useful in:

* Fraud prevention systems
* Authentication services
* Transaction validation
* Database systems
* User registration systems
* Data cleaning pipelines

For example, a transaction system can use duplicate detection to prevent the same transaction from being processed twice.

## What I Learned

This task helped me understand that choosing the right data structure can make a huge difference in performance.

The brute-force approach is easy to implement, but using a set allows much faster lookups and scales better for large datasets.

## Conclusion

Day 15 helped me understand the importance of algorithmic thinking. I compared a simple `O(N²)` solution with an optimized `O(N)` average solution and learned why efficient data structures become important when working with large datasets.
