# Day 16 - Recursive Staircase

## Phase

Recursive Thinking

## Problem

A robot is climbing an infinite staircase. It can climb either 1 step or 2 steps at a time.

The goal is to calculate the number of different ways the robot can reach step `N`.

This task focuses on understanding recursion and then optimizing it using memoization.

## What I Learned

* How recursion works
* How a problem can be broken into smaller subproblems
* How a recursion tree is formed
* Why repeated calculations can make recursion slow
* How memoization avoids repeated calculations
* Difference between a basic recursive solution and an optimized solution

## Recursive Approach

To reach step `N`, the robot can come from either:

* Step `N - 1` by taking 1 step
* Step `N - 2` by taking 2 steps

Therefore:

```text
ways(N) = ways(N - 1) + ways(N - 2)
```

The recursive solution keeps breaking the problem into smaller problems until it reaches the base cases.

## Recursion Tree

For example, for `N = 5`:

```text
                    ways(5)
                   /       \
             ways(4)       ways(3)
             /    \         /    \
        ways(3) ways(2) ways(2) ways(1)
          /  \
     ways(2) ways(1)
```

The problem is that values such as `ways(3)` and `ways(2)` are calculated multiple times.

This creates unnecessary work.

## Memoization

Memoization stores the result of a subproblem after calculating it for the first time.

If the same subproblem is needed again, the stored result is used instead of calculating it again.

For example:

```text
ways(3) → calculate once
ways(3) → use stored result
```

This makes the recursive solution much more efficient.

## Complexity Comparison

| Approach        | Time Complexity | Space Complexity |
| --------------- | --------------: | ---------------: |
| Basic Recursion |        `O(2^N)` |                  |
