# Writing to Files

## 1. Writing To Files

We can write to files in two ways. Either by writing a string or by writing a list of lines.

**WARNING - Writing will overwrite the entire contents of the file.**

We can write a string to the contents of a file using the ``write`` method.
```python
# write to the file example.txt
with open("example.txt", "w") as file:
  file.write("Write some content to the file")
```

The contents of the file will now be:

```
Write some content to the file
```
We can also write a list of strings to the file using the ``writelines()`` method.
```python
string_list = ["This is a line", "This is another line"]

# write to the file example.txt
with open("example.txt", "w") as file:
  file.writelines(string_list)
```

The contents of the file will now be:

```
This is the line
This is another line
```

## 2. Appending To Files
Appending will append to the end of the file.

We can append it to a file as follows:

```python
# append some content to the file example.txt
with open("example.txt", "a") as file:
  file.write("\nThis is some extra content to append\n")
```
For example, if the contents of the file are,

```
This is the line
This is another line
```

then after the append, the contents will be:

```
This is the line
This is another line
This is some extra content to append
```
### Be careful


The following code snippet does the following:

1. Writes to the file and prints it out
2. Appends to the file and prints it out
3. Writes to the file and prints it out (this now overwrites the content produced by 1 and 2)

You should try this in **main.py** and make sure you understand what it is doing.


```python
import os

# this is a relative path
filepath = "example.txt"
# if you do not use the r for the absolute path on windows, the \ are interpreted as an escape character.
# filepath = r"C:\Users\Bob\example.txt"

print("The current working directory (the default path for reading/writing/appending) is:\n")
print(os.getcwd())
print()

print("\n-----Writing some content-----\n")
# write to the file example.txt
with open(filepath, "w") as file:
  file.write("Write some content to the file")

# read the contents of example.txt
with open(filepath) as file:
  lines = file.read()

print("-----Reading content after first write-----\n")
print(lines)

print("\n-----Appending some content-----\n")
# append some content to the file example.txt
with open(filepath, "a") as file:
  file.write("\nThis is some extra content to append\n")

# read the contents of example.txt
with open(filepath) as file:
  lines = file.read()

print("\n-----Reading content after append-----\n")
print(lines)

print("\n-----Writing some content-----\n")
# write some content to the file example.txt. 
# This will now overwrite the previous content
with open(filepath, "w") as file:
  file.write("Oh dear we have overwritten all the content in example.txt")

# read the contents of example.txt
with open(filepath) as file:
  lines = file.read()

print("-----Reading content after second write-----")
print(lines)
```

# === TASK ===

Write a function called ``write_nums()`` that outputs the first positive n numbers to a txt file called ``nums.txt``

For example,

```python
write_nums(10)
```
Should output the first 10 numbers to the file ``nums.txt``

```
1
2
3
4
5
6
7
8
9
10
```

```python
def write_nums(n):
  pass

if __name__ == "__main__":
  write_nums(10) 
  # writes out the first 10 positive numbers to nums.txt
```