# Day 14 - Sprint Review

## Phase

Sprint Review

## Project

Student Performance Analyzer

## Objective

The goal of Day 14 is to combine the concepts learned during the previous days into one small working system.

This project processes a student dataset using arrays/lists, loops, conditions, and hashing.

## Concepts Used

* Lists / Arrays
* Loops
* Conditional statements
* Hashmaps using Python dictionaries
* Data processing
* Basic data analysis

## How It Works

The system stores student names and their marks in a list.

It then:

1. Processes each student's data.
2. Calculates the total and average marks.
3. Finds the student with the highest marks.
4. Finds the student with the lowest marks.
5. Assigns grades based on marks.
6. Uses a dictionary to count the number of students in each grade.
7. Generates simple insights from the dataset.

## Example Dataset

```text
Aman - 85
Riya - 92
Karan - 67
Simran - 74
Rahul - 92
Neha - 56
Arjun - 85
Mehak - 45
```

## Example Insights

The system can identify:

* Total number of students
* Average marks
* Highest scorer
* Lowest scorer
* Grade distribution
* Overall performance

## Hashing Usage

A Python dictionary is used as a hashmap to store the frequency of each grade.

For example:

```text
A → 2
B → 3
C → 2
F → 1
```

This allows the program to quickly look up and update grade counts.

## Complexity

For `N` students:

* **Time Complexity:** `O(N)`
* **Space Complexity:** `O(K)`

Where `K` represents the number of different grades.

## Real-World Impact

Real-world systems often combine multiple data structures and algorithms instead of using only one concept.

Similar approaches can be used in:

* Student management systems
* Sales dashboards
* Customer data analysis
* Employee performance systems
* Data processing applications

## Conclusion

Day 14 was a sprint review of the concepts I learned during the previous days. I combined arrays, loops, conditions, and hashing to build a small data processing system and generate useful insights from the dataset.
