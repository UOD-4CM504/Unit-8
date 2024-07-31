# Creating a Module

To create your own module you just need to create a .py file that includes your code. Generally, this will include functions. 

Later we will look at including classes. 

Modules can include both functions and variables.

## 1. Creating a Module

You will see in the file explorer a file called **calculator1.py**

This includes two functions and a variable:

```python
# calculator1.py

# terrible approximation of pi
pi = 3.14

def add(x,y):
  return x + y

def mul(x,y):
  return x * y

```

Please have a look at the file for yourself.

We can now use this file in our **main.py** via an import.

```python
# main.py
import calculator1 as calc

print(calc.add(3,4)) # use the add function from calc
print(calc.mul(3,4)) # use the mul function from calc
print(calc.pi)       # use the pi variable 
```

For now, it's enough that the module is in the same folder as your **main.py**. Later we will discuss ways to organise your project.

# 2. if name == "\_\_main\_\_"

We have used this during this module already, but now it is time to explain why.

You will see two additional files called ``calculator2.py`` and ``calculator3.py``.

They both contain the following code.

```python
# calculator2.py

# ...
# ...

print(f"These are lines printed inside {__name__}")
print("For example we might like to test the add function")
print(add(3, 4))
```

The difference is that ``calculator3.py`` has this code contained within the ``if __name__ == "__main__"`` block. 

```python
# calculator3.py

# ...
# ...

if __name__ == "__main__":
  print(f"These are lines printed inside {__name__}")
  print("For example we might like to test the add function")
  print(add(3, 4))
```

``__name__`` is a special reserved name in Python which 
 is used to keep track of the names of the files that are being run and imported. 

The file that you run, normally **main.py** but it can be any file, takes on the name ``__main__``. 

Try opening the **Shell** and typing ``ls``. This will list the files in the current directory. 

Type ``python main.py`` to run the main file.

Type ``python calculator2.py`` to run the ``calculator2.py`` file.

Type ``python calculator2.py`` to run the ``calculator3.py`` file.

You will not that ``__name__`` for both ``calculator2.py`` and ``calculator3.py`` is ``__main__``. This is because it is the starting (main) file being run by Python.

OK, back to ``if __name__ == "__main__"``.

What this does is tell python only to run that block of code if you are running ``calculator3.py``. 

Why do this?

Well, try importing ``calculator2.py`` and using it.

```python
import calculator2 as calc

print(calc.add(3,4)) # use the add function from calc
print(calc.mul(3,4)) # use the mul function from calc
print(calc.pi)       # use the pi variable 
```

This will print out the following:

```
These are lines printed inside cal2.py
For example, we might like to test the add function
7
7
12
3.14
```
Oh, dear! It printed out the code that is contained at the bottom of the file as well, really we just wanted to use the functions.

Now try it with ``calculator3.py``:

```python
import calculator3 as calc

print(calc.add(3,4)) # use the add function from calc
print(calc.mul(3,4)) # use the mul function from calc
print(calc.pi)       # use the pi variable 
```
This will print out the following:

```
7
12
3.14
```

Much better! Now it just imported the functions for us to use.

You can also run ``calculator3.py`` on its own. Click on the **Shell**.

Type the command ``ls``. This is the list of the contents of the directory. You will see a list of files in the current directory. 

Remember inside this repl it is like a mini-computer with a file directory. 

Now type:

``python calculator3.py``

This will run the file and print out the following.

```
These are lines printed inside __main__
For example, we might like to test the add function
7
```
Notice now that we are running the file itself, so the ``if __name__ == "__main__"`` block runs!

*** 
 # === TASK ===
Create a new file called **hello.py**

Your module should include two functions called ``hello()`` and ``goodbye()`` which take in a name and returns a string.

For example, ``hello()`` should operate as follows.

```python
hello("Joe") # returns "Hello Joe"
print(hello("Joe")) # prints Hello Joe
```
And, ``goodbye()`` should operate as follows.
```python
goodbye("Joe") # returns "Goodbye Joe"
print(goodbye("Joe")) # prints Goodbye Joe
```

I have included this code that you can use in **main.py** to test your module.

```python
# main.py
import hello

def main():
  print(hello.hello("Joe")) # prints Hello Joe
  print(hello.goodbye("Joe")) # prints Goodbye Joe

if __name__ == "__main__":
  main()
```

***