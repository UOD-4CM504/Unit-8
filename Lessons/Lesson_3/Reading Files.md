# Reading Files

Reading and writing to files allows us to start using persistent storage to remember data for our programs.

In this lesson, we will look at reading from a simple text file (.txt).

## 1. Opening a file

We can open a file using the following.

```python
open(path_to_file, mode)
```

| Mode | Description |
| -- | -- |
|``'r'`` | Open text file for reading text |
|``'w'`` | Open text file for writing text |
|``'a'`` | Open text file for appending text |

e.g.

```python
# open file in write mode
 f = open("example.txt", "r")
```

Here ``f`` is now a file object that represents the file. We can now use this to read the contents of the file, write to the file or append to the contents of the file.

### 1.1 Relative and Absolute Paths

In the above example we are using a relative path and Python will open the file based on what is known as the current working directory. This is normally the directory that the Python file (.py) is run from. 

It can change though. To check you can run the following (try it out).

```python
import os
print(os.getcwd()) # This uses the os module and returns the current working directory.
```

We could have given an absolute path e.g. ``C:\Users\Bob\example.txt`` if we were running our code on a windows machine and we wanted to read the file from a different directory. If you are using an absolute path on windows, because it uses a ``\`` (backslash) in its paths, you should but an ``r`` in front of it. This will tell Python not to treat the ``\`` as an escape character, i.e. treat it as a raw string.

```python
# open file in write mode
 f = open(r"C:\Users\Bob\example.txt", "r")
```
Alternatively you can escape the escape characters.
```python
# open file in write mode
 f = open("C:\\Users\\Bob\\example.txt", "r")
```

## 2. Reading a file

### Reading Methods 

Here are some select methods for reading. 

| Method | Description |
| -- | -- |
| ``read()`` | Returns the file content. |
| ``read(size)`` | Read the specified number of bytes. |
| ``readline()`` | Returns one line from the file. If you call this multiple times it will return the next line and internally keep track of which line is next. |
| ``readlines()`` | Returns a list of the lines in the file. |
| ``close()`` | Closes the file. This is extremely important for freeing up resources. Always close your file.

You can see other file methods via this link - [Python File Methods](https://www.w3schools.com/python/python_ref_file.asp)

### Read the whole contents

We can read the whole contents of the file using the ``read()`` method.

```python
file = open("example.txt", "r")
lines = file.read()
file.close()

print(lines)
```
You will note the ``close()`` method here. This closes the file. You should always close your file when done. Here are some reasons.

- It can mean that you have too many things open, and thus more used space in the RAM, this may slow down your program.

- Changes are not written to the file until it is closed. If you don't explicitly close then you may not see the edits in another part of your program.

- If you have too many files open, you could run into limits which will throw an error.

- You become reliant on the garbage collector - though the file in theory will be automatically closed when it is closed is now not up to you. 




### Using the context manager ``with``
We can make sure the file is closed by using the ``with`` keyword. 

**I would strongly advise this.**
```python
# this loads all of the lines in the file into a list
with open('example.txt', "r") as file:
  # read all the lines and put in a list of containing each line
  lines = file.readlines()

# print the list of lines
print(lines)
```

### Read the file line by line

We can also read the file line by line. The following code reads the whole content of the file and puts each line into a list.

We can then iterate over the list of lines.

```python
# this loads all of the lines in the file into a list
with open('example.txt', "r") as file:
  # read all the lines and put in a list containing each line
  lines = file.readlines()

# for each of the lines in the list
for l in lines:
  # print the line
  print(l)
  # print(l.strip()) # if you want to stop python printing a new line after each line
```

This is fine when we have a small file, but if we have a large volume of data, we may not wish to load the entire file into memory.

### Don't load the whole file into memory

One way to combat this is to read the file line by line and do something with each line. Now we are not loading the whole file into memory, just a line at a time.

```python
# this reads the file line by line, without reading it all into memory at once
with open('example.txt', "r") as file:
  # read the first line as a string
  line = file.readline()
  # while line is not empty
  while line:
    # print line
    print(line)
    # read the next line
    line = file.readline()
```

### FileNotFoundError

Opening files is a potential source of errors in your program. If the file does not exist and your try to read from it, it will throw an error.

```python
# this loads all of the lines in the file into a list
with open('example1.txt', "r") as file:
  # read all the lines and put in a list containing each line
  lines = file.readlines()
```

As ``example1.txt`` does not exist, this will throw a ``FileNotFoundError``.

We can deal with this error by using a ``try..except``

```python
try:
  file = open("example1.txt", "r")
  lines = file.read()
  print(lines)
except FileNotFoundError:
  print("File not found")
finally:
  # we close the file in a finally block, this executes regardless of whether the try succeeds or fails. It will always run.
  file.close()
```

You will notice an extra keyword here, ``finally``. This executes regardless of whether the try succeeds or fails. It will always run and we always want to make sure the file has been closed!

However, if you use the context manager ``with`` then we don't need the ``finally`` because the ``with`` keyword will close the file for us if there is an error while reading.
```python
try:
  with open("example1.txt", "r") as file:
    lines = file.read()
    print(lines)
except FileNotFoundError:
  print("File not found")
```


# === TASK ===

Amend the function ``number_of_lines()`` so that it reads the contents of the file stored at  ``filename`` and counts the number of lines in the file. It should then return this number.

Copy and paste the following into **main.py** to get started.

```python
def number_of_lines(filename):
  """ Write your code here """
  pass

def main():
  print(number_of_lines("example.txt")) # prints 3 as example.txt contains 3 lines
  print(number_of_lines("test.txt"))    # prints 25 as test.txt contains 25 lines

if __name__ == "__main__":
  main()
```

