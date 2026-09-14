# Day 13 - Valid Anagram

## Phase

Hashing & Lookup

## Problem

The goal of Day 13 is to solve the **Valid Anagram** problem using a hashmap and understand why hashing can make lookups more efficient.

Two strings are anagrams if they contain the same characters with the same frequency.

## What I Learned

* What hashing means
* How Python dictionaries work like hashmaps
* How to store character frequencies
* How hashing can make lookups faster
* Difference between brute force and optimized approaches

## Approach

### Hashmap Approach

1. First, check if both strings have the same length.
2. Create an empty dictionary to store character frequencies.
3. Go through the first string and count each character.
4. Go through the second string and decrease the corresponding frequency.
5. If a character is missing or its frequency becomes negative, return `False`.
6. If all characters match, return `True`.

## Example

**Input:**

```text
s = "anagram"
t = "nagaram"
```

**Output:**

```text
True
```

Both strings contain the same characters with the same frequencies.

## Brute Force vs Hashmap

### Brute Force

The earlier approach used `count()` for every character.

* **Time Complexity:** `O(N²)`
* Easy to understand but slower for large strings.

### Hashmap

The optimized approach stores character frequencies in a dictionary.

* **Time Complexity:** `O(N)`
* **Space Complexity:** `O(K)`

Where `N` is the length of the string and `K` is the number of distinct characters.

## Real-World Applications

Hashing and fast lookups are commonly used in:

* Databases
* Caching systems
* Authentication systems
* Frequency counting
* Search and lookup systems

## Conclusion

Day 13 helped me understand how a hashmap can improve the efficiency of a solution. I also compared my earlier brute-force approach with the optimized hashmap approach and understood why storing information for quick lookup is useful.
