# DSA in Python

This repository contains a few beginner-friendly Python programs for common number-based DSA practice problems.

## Files

- `COUNT_DIGITS.py` - counts the digits in a number using loops and a math-based approach.
- `PALINDROME.py` - reverses a number and checks whether it is a palindrome.
- `ARMSTRONG.py` - checks whether a number is an Armstrong number.
- `FACTORS.py` - prints the factors of a number using brute force, better, and optimal methods.
- `FREQUENCY_MAP.py` - builds a frequency map of numbers using two simple methods.
- `ELEMENT_FREQUENCY_COUNT.py` - counts how often target elements appear in a list using brute force, optimal, and dictionary-based methods.
- `CHARACTER_FREQUENCY_COUNT.py` - counts character occurrences in a string using a dictionary.
 - `RECURSION.py` - small recursion examples: factorial, fibonacci, sum of list, reverse string.

## How to run

Run any script directly with Python:

```bash
python COUNT_DIGITS.py
python PALINDROME.py
python ARMSTRONG.py
python FACTORS.py
python FREQUENCY_MAP.py
python ELEMENT_FREQUENCY_COUNT.py
python CHARACTER_FREQUENCY_COUNT.py
python RECURSION.py
```

## Examples

Character frequency example:

Run:

```bash
python CHARACTER_FREQUENCY_COUNT.py
```

Sample output:

```
Occurence of d is 0
occurence of a is 5
occurence of y is 2
occurence of x is 1
{'a': 5, 'z': 3, 'y': 2, 'x': 1}
```

Other examples:

Count digits:

```bash
python COUNT_DIGITS.py
```

Sample output:

```
4
4
```

Check palindrome:

```bash
python PALINDROME.py
```

Sample output:

```
Not a Palindrome
```

Armstrong check:

```bash
python ARMSTRONG.py
```

Sample output:

```
Is a Armstrong.
```

Factors (n = 36):

```bash
python FACTORS.py
```

Sample output:

```
[1, 2, 3, 4, 6, 9, 12, 18, 36]
[1, 2, 3, 4, 6, 9, 12, 18, 36]
[1, 36, 2, 18, 3, 12, 4, 9, 6]
```

Frequency map:

```bash
python FREQUENCY_MAP.py
```

Sample output (order may vary):

```
{5: 2, 6: 1, 7: 2, 1: 5, 9: 1, 111: 1}
{5: 2, 6: 1, 7: 2, 1: 5, 9: 1, 111: 1}
```

Element frequency count:

```bash
python ELEMENT_FREQUENCY_COUNT.py
```

Sample output:

```
10 occurs 1
111 occurs 0
1 occurs 1
9 occurs 0
5 occurs 4
67 occurs 0
2 occurs 2
```

Recursion examples:

```bash
python RECURSION.py
```

Sample output:

```
factorial_recursive(5) 120
fibonacci_recursive(6) 8
fibonacci_memo(30) 832040
sum_list_recursive([1,2,3,4]) 10
reverse_string_recursive('hello') olleh
```

## Notes

- These scripts are written as simple practice examples.
- You can edit the input values inside each file to test different numbers.
