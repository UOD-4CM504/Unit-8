# Module Basics

Modules are files that can be imported into your project so you can use pre-built functionality.

Python comes with a number of built-in modules and you can also install python libraries which contain modules that other programmers have installed, but are not part of standard Python.

We will use three modules to demonstrate the basics. ``math``, 
 ``datetime`` and ``random``.

## 1. Importing a Module

You ALWAYS import modules at the top of your python files! 

```python
# import the built-in maths module
import math

print(math.pi)
print(math.sqrt(2.78))
```

If you want to see what is in ``math`` you can type ``help(math)`` into the console or use Google!

```python
import datetime

# Uses the now method in the datetime class (more on this later)
print(datetime.datetime.now())
```

```python
import random

print(random.randint(3, 9)) # rand number between 3 and 9

mylist = ["apple", "banana", "cherry"]
print(random.choice(mylist)) # randomly picks from mylist
```

The main point here is you haven't had to do much to get some serious functionality! 

Generally, unless you feel the need, don't recode something that already exists!

### 1.1 Importing Part of A Module

We could have chosen to just import the ``randint()`` function,

```python
# only import a given function
from random import randint

print(randint(3, 9)) # rand number between 3 and 9
```

or multiple functions.

```python
# only import a given function
from random import randint, choice

print(randint(3, 9)) # rand number between 3 and 9

mylist = ["apple", "banana", "cherry"]
print(choice(mylist)) # randomly picks from mylist
```

I would generally avoid doing this! It is harder to tell when a function has come from an external module. 

### 1.2 Renaming a Module

Sometimes it is useful to give a module an alias (shorten a module name). Again this is something that is done for some modules, if in doubt on how to import a module, just use Google!

```python
# I wouldn't do this!
import datetime as dt

print(dt.datetime.now())
```

Ultimately getting used to using modules takes time and experience, but you can always look up how to do these things.

Normally if I want to do something in Python, I google it and look at some code, there is normally a module either pre-built or as part of an external library that will help.

## 2. Useful Built-in Modules

You can find a complete list of built-in modules via the [Python Docs][1], or a slightly friendlier list of the most common ones via [W3Schools][2].

Again, Google is your friend. If you can use a built-in module instead of a 3rd party one then you should

## 3. Libraries

Libraries in Python are just a collection of related modules. 

The built-in modules are part of the Python standard library.

You can install other libraries and use their modules, we have already seen the use of a 3rd party library (a very common one) called [Matplotlib][3]. And we used the pyplot module.

```python
# import LIBRARY.MODULE as NAME
import matplotlib.pyplot as plt
```
Here we import the pyplot module from the matplotlib library and give it an alias (name).

We also import the [numpy][4] module as ``np``.
```python
import matplotlib.pyplot as plt
import numpy as np

x = np.arange(1,100,0.1)
y = np.sin(x)
plt.plot(x,y)
plt.show()
```

If you run this code in **main.py** it will give you a plot of the sine function.

![Sine function plot](assets/sin_plot.png)

***
# === TASK ===
Import the ``os`` module 

Amend the function ``get_current_working_directory()`` so that it returns the current working directory as a string.

HINT: Search for "current working directory" on the following URL - [Python Docs - os Module](https://docs.python.org/3/library/os.html#module-os)

Implement the functions ``encode_string()`` and ``decode_string()`` using the ``base64`` module so that they encode and decode a string using base64.

You can find out more via the following URLs. You will be required to read at least one of these links to implement the functions.

[Base64 Encoding](https://www.python-engineer.com/posts/base64-module/)

[Encoding and Decoding Base64 Strings in Python - G4G](https://www.geeksforgeeks.org/encoding-and-decoding-base64-strings-in-python/#:~:text=In%20Python%20the%20base64%20module,strings%20isn%27t%20base64%20characters.)

Copy and paste this into **main.py** to get started.

```python
def get_current_working_directory():
  pass

def encode_string(str_to_encode):
  """ Encodes a string using base64"""
  pass

def decode_string(base64_str_to_decode):
  """ Decodes a string encoded in base64"""
  pass
  

if __name__ == "__main__":
  print(get_current_working_directory())
  print(encode_string("Python is a cool programming language!"))
  # should print UHl0aG9uIGlzIGEgY29vbCBwcm9ncmFtbWluZyBsYW5ndWFnZSE=
  str_to_decode = "UHl0aG9uIGlzIGEgY29vbCBwcm9ncmFtbWluZyBsYW5ndWFnZSE="
  print(decode_string(str_to_decode))
  # should print Python is a cool programming language!
```
***

# References 

[1. Python Docs - Built-in Modules][1]

[2. W3schools - Python Built-in Modules][2]

[3. Matplotlib - Plotting Library][3]

[4. Numpy][4]

[1]: <https://docs.python.org/3/py-modindex.html> "Python Docs - Built-in Modules"

[2]: <https://www.w3schools.com/python/python_ref_functions.asp> "W3schools - Python Built-in Modules"

[3]: <https://matplotlib.org/> "Matplotlib - Plotting Library"

[4]: <https://numpy.org/> "Numpy - The fundamental package for scientific computing with Python"