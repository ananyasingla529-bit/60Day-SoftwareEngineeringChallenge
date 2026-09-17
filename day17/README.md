# Day 17 - Backtracking & Search

## Phase

Backtracking & Search

## Problem

Given a list of gems, the goal is to generate **all possible combinations (subsets)** that the player can carry.

For example, for:

```text
[Ruby, Sapphire, Emerald]
```

the program should generate every possible combination, including the empty combination.

## What I Learned

* What backtracking means
* How recursion can explore different choices
* How to generate all subsets of a list
* How the `append()` and `pop()` operations are used in backtracking
* How to visualize a recursion/decision tree
* Why the number of combinations grows exponentially

## How Backtracking Works

Backtracking follows a simple process:

```text
Choose → Explore → Undo → Try Again
```

For every gem, the program chooses a gem, recursively explores the remaining gems, and then removes the selected gem before trying another possibility.

The important part of the code is:

```python
path.append(gems[i])
backtrack(i + 1)
path.pop()
```

* `append()` chooses a gem.
* `backtrack()` explores further combinations.
* `pop()` removes the gem so another choice can be tried.

## Example

For:

```text
[Ruby, Sapphire, Emerald]
```

the possible combinations are:

```text
[]
[Ruby]
[Sapphire]
[Emerald]
[Ruby, Sapphire]
[Ruby, Emerald]
[Sapphire, Emerald]
[Ruby, Sapphire, Emerald]
```

There are **8 total combinations**.

## Number of Combinations

Each gem has two choices:

```text
Include the gem
OR
Don't include the gem
```

Therefore, for `N` gems:

```text
Total combinations = 2^N
```

For example:

```text
1 gem  → 2 combinations
2 gems → 4 combinations
3 gems → 8 combinations
4 gems → 16 combinations
```

## Recursion Tree

For three gems, the decision process can be visualized as:

```text
                []
              /    \
          [Ruby]    ...
          /    \
 [Ruby,Sapphire] [Ruby,Emerald]
        |
[Ruby,Sapphire,Emerald]
```

The tree represents the different choices made by the algorithm.

## Complexity

* **Time Complexity:** `O(N × 2^N)`
* **Space Complexity:** `O(N)` for the recursion path, excluding the output.

Since there are `2^N` possible combinations, generating all of them naturally takes exponential time.

## Real-World Applications

Backtracking is commonly used in:

* Scheduling systems
* Recommendation engines
* AI decision trees
* Games and puzzles
* Combination and subset problems
* Pathfinding and search problems

## Conclusion

Day 17 helped me understand how backtracking can be used to explore all possible choices.

The main idea I learned is:

**Choose → Explore → Undo → Try Again**

Backtracking allows the program to reuse the same path while exploring different possibilities, making it a useful technique for search and combination problems.
