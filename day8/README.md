# Day 8 - Core Data Structures

## Array Analysis

In this task, I created an array (Python list) containing numbers that simulate user data. I used a loop to check each number and counted how many numbers have an even number of digits.

### How it works

1. A list is created containing numbers.
2. The program goes through each number using a `for` loop.
3. Each number is converted to a string so that its digits can be counted.
4. The program checks whether the number of digits is even.
5. The matching numbers are stored in another list.
6. Finally, the program prints the results and the total count.

### Example

For the data:

`[12, 345, 67, 890, 1234, 56, 789, 1002]`

The numbers with an even number of digits are:

`[12, 67, 1234, 56, 1002]`

Total count: **5**

## How Arrays Are Used in Real Systems

Arrays are used to store and process collections of data efficiently. In real systems, they can represent user activity, website visits, sales records, sensor readings, or application logs. For example, an analytics dashboard can use arrays to store daily user activity and then process the data to calculate statistics and identify patterns.

Arrays are important because programs often need to process many related values together rather than storing every value separately.
