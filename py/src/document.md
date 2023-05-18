# Cheat Sheet

## File Operations

### Open File

- `open(filename, mode)`: Opens a file with the specified name and mode.

### Read File

- `read()`: Reads the contents of a file.
- `readline()`: Reads a single line from a file.
- `seek(offset)`: Moves the file pointer to a specified position.
- `tell()`: Returns the current position of the file pointer.

### Write File

- `write(data)`: Writes data to a file.
- `writelines(lines)`: Writes a list of lines to a file.

### Close File

- `close()`: Closes a file.

## Strings

### Functions

- `index(substring)`: Returns the index of the first occurrence of a substring.
- `rindex(substring)`: Returns the index of the last occurrence of a substring.
- `find(substring)`: Returns the index of the first occurrence of a substring.
- `rfind(substring)`: Returns the index of the last occurrence of a substring.
- `replace(old, new)`: Replaces one substring with another.
- `split(delimiter)`: Splits a string into a list of substrings based on a delimiter.
- `splitlines()`: Splits a string into a list of lines.
- `capitalize()`: Capitalizes the first letter of a string.
- `count(substring)`: Returns the number of occurrences of a substring in a string.
- `startswith(substring)`: Checks if a string starts with a specified substring.
- `endswith(substring)`: Checks if a string ends with a specified substring.
- `lower()`: Converts a string to lowercase.
- `upper()`: Converts a string to uppercase.
- `join(iterable)`: Joins the elements of an iterable into a single string.
- `strip()`: Removes leading and trailing whitespace from a string.
- `str(number)`: Converts a number to a string.

## Math

### Functions

- `abs(number)`: Returns the absolute value of a number.
- `ceil(number)`: Rounds a number up to the nearest integer.
- `floor(number)`: Rounds a number down to the nearest integer.
- `max(iterable)`: Returns the largest value in an iterable.
- `min(iterable)`: Returns the smallest value in an iterable.
- `round(number)`: Rounds a number to the nearest integer.
- `sqrt(number)`: Calculates the square root of a number.

## Lists

### Functions

- `append(element)`: Adds an element to the end of a list.
- `count(element)`: Returns the number of occurrences of an element in a list.
- `extend(iterable)`: Extends a list by appending elements from an iterable.
- `index(element)`: Returns the index of the first occurrence of an element in a list.
- `insert(index, element)`: Inserts an element at a specified index in a list.
- `pop(index)`: Removes and returns an element at a specified index in a list.
- `remove(element)`: Removes the first occurrence of an element from a list.
- `reverse()`: Reverses the order of elements in a list.
- `sort()`: Sorts the elements of a list.

## Sets

### Functions

- `add(element)`: Adds an element to a set.
- `clear()`: Removes all elements from a set.
- `copy()`: Returns a shallow copy of a set.
- `difference(set)`: Returns the difference between two sets as a new set.
- `intersection(set)`: Returns the intersection of two sets as a new set.
- `isdisjoint(set)`: Checks if two sets have no common elements

## Escape Sequences

- `\n`: newline
- `\t`: tab
- `\\`: backslash
- `\'`: single quote
- `\"`: double quote
- `\r`: carriage return
- `\b`: backspace
- `\f`: form feed
- `\v`: vertical tab
- `\ooo`: octal value
- `\xhh`: hexadecimal value
