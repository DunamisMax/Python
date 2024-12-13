# Cheat Sheet

## 1. Core Principles & Best Practices

**Python Philosophy (import this):**

- Beautiful is better than ugly.
- Explicit is better than implicit.
- Simple is better than complex.
- Readability counts.

**PEP 8 Conventions:**

- Indent with 4 spaces.
- Limit lines to 79 characters.
- Use `snake_case` for functions and variables, `PascalCase` for classes, and `ALL_CAPS` for constants.
- Import modules at the top of the file, grouped by standard library, third-party, then local modules.
- Write docstrings using triple quotes (`""" """`).

---

## 2. Running Python & Virtual Environments

**Running a Python script:**

```bash
python3 script.py
```

**REPL (Interactive Shell):**

```bash
python3
```

**Virtual Environments:**

```bash
python3 -m venv venv       # Create a virtual environment
source venv/bin/activate   # Activate on Unix/macOS
venv\Scripts\activate      # Activate on Windows
pip install package_name    # Install packages isolated
deactivate                 # Exit virtual environment
```

---

## 3. Basic Syntax & Data Types

**Variables & Assignment:**

```python
x = 10
name = "Alice"
is_active = True
```

**Common Data Types:**

- **Numeric:** `int`, `float`, `complex`
- **Boolean:** `True`, `False`
- **String:** `str` (immutable text)
- **Sequences:** `list`, `tuple`, `range`
- **Sets:** `set`, `frozenset`
- **Mappings:** `dict`

**Type Conversion:**

```python
int("42")       # 42
float("3.14")   # 3.14
str(100)        # "100"
list("abc")     # ["a", "b", "c"]
```

---

## 4. Strings

**String Literals:**

- Single quotes, double quotes, or triple quotes for multi-line strings.

```python
s = 'Hello'
multiline = """This is
a multiline
string."""
```

**Common String Methods:**

```python
s.lower(), s.upper(), s.strip(), s.replace("old","new"), s.split(","), s.join(list_of_strings)
```

**f-Strings (Python 3.6+):**

```python
name = "Alice"
age = 30
f"Name: {name}, Age: {age}, Next Year: {age+1}"
```

**String Formatting Alternatives:**

- `str.format()`: `"{} {}".format(var1, var2)`
- Old style `%` formatting: `"%s %d" % (str_var, int_var)`

---

## 5. Lists, Tuples & Sets

**Lists:** Ordered, mutable.

```python
lst = [1, 2, 3]
lst.append(4)
lst[0] = 10      # Mutation
sub = lst[1:3]   # Slicing
```

**Tuples:** Ordered, immutable.

```python
t = (1, 2, 3)
a, b, c = t      # Unpacking
```

**Sets:** Unordered, unique elements.

```python
s = {1, 2, 3}
s.add(4)
s.remove(2)
```

**Useful List/Set Operations:**

```python
len(lst), sum(lst), min(lst), max(lst)
list(set(lst))  # Convert set to list
```

---

## 6. Dictionaries

**Creation & Basic Operations:**

```python
d = {"key": "value", "count": 10}
d["new_key"] = "new_value"
val = d.get("missing_key", default_value)
```

**Dictionary Methods:**

```python
d.keys(), d.values(), d.items()
d.pop("key"), d.update({"another_key": 42})
```

**Dictionary Comprehension:**

```python
{x: x**2 for x in range(5)}  # {0:0, 1:1, 2:4, 3:9, 4:16}
```

---

## 7. Control Flow

**If/Elif/Else:**

```python
if x > 0:
    print("Positive")
elif x == 0:
    print("Zero")
else:
    print("Negative")
```

**For Loops:**

```python
for i in range(5):
    print(i)
for item in iterable:
    print(item)
```

**While Loops:**

```python
while condition:
    # loop body
```

**Loop Control:**

- `break`: exit loop
- `continue`: skip current iteration
- `else`: block executes if loop not terminated by `break`.

```python
for i in range(5):
    if i == 3:
        break
else:
    print("No break encountered")
```

---

## 8. Functions & Lambda Expressions

**Defining Functions:**

```python
def greet(name: str) -> str:
    """Return a greeting message."""
    return f"Hello, {name}!"
```

**Default Parameters:**

```python
def add(x, y=10):
    return x + y
```

**Keyword Arguments:**

```python
def func(a, b, c):
    pass

func(c=3, a=1, b=2)
```

**Variable-length Arguments:**

```python
def func(*args, **kwargs):
    print(args)
    print(kwargs)
```

**Lambda Functions:**

```python
double = lambda x: x * 2
nums = [1, 2, 3]
doubled = list(map(lambda n: n*2, nums))
```

---

## 9. Comprehensions

**List Comprehension:**

```python
[x*2 for x in range(5)]   # [0, 2, 4, 6, 8]
[x for x in range(10) if x%2==0]
```

**Set & Dict Comprehensions:**

```python
{x**2 for x in range(5)}
{k: v*2 for k,v in {"a":1,"b":2}.items()}
```

---

## 10. Modules & Packages

**Imports:**

```python
import math
from math import sqrt
import os.path as p
```

**Creating a Module:**

- Save Python file (`mymodule.py`).
- Import it: `import mymodule`.

**Package Structure (example):**

```bash
myproject/
    mypackage/
        __init__.py
        module1.py
        module2.py
    main.py
```

**Reloading Modules (for debugging):**

```python
import importlib
importlib.reload(mymodule)
```

---

## 11. Object-Oriented Programming (OOP)

**Classes & Instances:**

```python
class Person:
    species = "Homo sapiens"   # Class attribute

    def __init__(self, name, age):
        self.name = name       # Instance attribute
        self.age = age

    def greet(self):
        return f"Hello, I'm {self.name}"

p = Person("Alice", 30)
print(p.greet())
```

**Inheritance:**

```python
class Employee(Person):
    def __init__(self, name, age, employee_id):
        super().__init__(name, age)
        self.employee_id = employee_id
```

**Class & Static Methods:**

```python
class MyClass:
    @classmethod
    def from_string(cls, s):
        # ...

    @staticmethod
    def helper_method(x):
        # ...
```

**Property Decorator:**

```python
class Square:
    def __init__(self, side):
        self._side = side

    @property
    def area(self):
        return self._side ** 2
```

---

## 12. Exceptions & Error Handling

**Try/Except/Finally:**

```python
try:
    result = 10 / 0
except ZeroDivisionError as e:
    print("Division by zero!")
finally:
    print("Cleanup actions")
```

**Raise Exceptions:**

```python
if condition_not_met:
    raise ValueError("Invalid value")
```

**Custom Exceptions:**

```python
class CustomError(Exception):
    pass
```

---

## 13. File I/O

**Reading & Writing Text Files:**

```python
with open("data.txt", "r") as f:
    content = f.read()

with open("output.txt", "w") as f:
    f.write("Hello, world!")
```

**Reading by Lines:**

```python
with open("data.txt") as f:
    for line in f:
        print(line.strip())
```

---

## 14. Useful Built-in Functions

**Common Built-ins:**

- `len(), max(), min(), sum(), sorted(), reversed()`
- `enumerate(iterable)`, `zip(*iterables)`, `map(func, iterable)`, `filter(func, iterable)`

**Any/All:**

```python
nums = [1, 2, 3]
all(n > 0 for n in nums)  # True
any(n < 0 for n in nums)  # False
```

---

## 15. Iterators & Generators

**Iterators:**

- Objects that implement `__iter__()` and `__next__()`.

**Generators:**

```python
def countdown(n):
    while n > 0:
        yield n
        n -= 1

for val in countdown(3): # 3,2,1
    print(val)
```

**Generator Expressions:**

```python
gen = (x*2 for x in range(5))
```

---

## 16. Functional Programming Tools

**`map`, `filter`, `reduce`:**

```python
from functools import reduce
nums = [1, 2, 3, 4]
mapped = map(lambda x: x*2, nums)
filtered = filter(lambda x: x%2==0, nums)
reduced = reduce(lambda a,b: a+b, nums, 0)  # sum of nums
```

---

## 17. Standard Library Highlights

**`math` & `cmath`:** Mathematical functions, constants.
**`random`:** `random.random()`, `random.choice()`, `random.shuffle()`.
**`datetime`:** Date and time manipulation.
**`os` & `pathlib`:** File system operations, path handling.
**`sys`:** System-specific parameters and functions.
**`subprocess`:** Run external commands.
**`argparse`:** Command-line argument parsing.
**`logging`:** Flexible logging system.
**`json`, `csv`: Data serialization and parsing.
**`re`:** Regular expressions.

---

## 18. Testing & Quality Assurance

**`unittest`:** Built-in unit testing framework.

```python
import unittest

class TestExample(unittest.TestCase):
    def test_addition(self):
        self.assertEqual(1+1, 2)

if __name__ == "__main__":
    unittest.main()
```

**`pytest`:** Third-party testing framework with simpler syntax.
**Linting & Formatting:** `flake8`, `black`, `pylint`, `mypy` for type checking.
**Coverage:** `coverage` package for test coverage reports.

---

## 19. Concurrency & Parallelism

**Threading:** For I/O-bound tasks.

```python
import threading

def worker():
    pass

t = threading.Thread(target=worker)
t.start()
t.join()
```

**Multiprocessing:** For CPU-bound tasks.

```python
from multiprocessing import Pool

def square(x):
    return x**2

with Pool(4) as p:
    results = p.map(square, range(10))
```

**asyncio (Async I/O):**

```python
import asyncio

async def fetch_data():
    # async operations
    return data

async def main():
    result = await fetch_data()
    print(result)

asyncio.run(main())
```

---

## 20. Packaging & Distribution

**`setup.py` or `pyproject.toml`:** For building & distributing packages.
**Wheel & sdist:**

```bash
python3 -m build
python3 -m pip install . # install your local package
```

**Uploading to PyPI:**

```bash
python3 -m twine upload dist/*
```

---

## 21. Debugging & Profiling

**Debugging:**

- Use `print()` for quick checks.
- Use `pdb` or `breakpoint()` (Python 3.7+) for interactive debugging sessions.

```python
import pdb
pdb.set_trace()
```

**Profiling:**

```bash
python3 -m cProfile script.py
```

- Use `timeit` for micro-benchmarks:

```python
import timeit
timeit.timeit("sum(range(1000))", number=10000)
```

---

## 22. Type Hints & Static Analysis

**Type Hints:**

```python
def add(x: int, y: int) -> int:
    return x + y
```

**Tools:**

- `mypy` for type checking.
- `pylint` or `flake8` for linting.

---

## 23. Tips & Tricks

- Use `with` statement (context managers) to ensure resources are freed (files, locks).
- Take advantage of `enumerate()` and `zip()` for cleaner loops.
- Prefer `pathlib` over `os.path` for readability and cross-platform code.
- Keep functions small and focused.
- Write docstrings for public modules, classes, methods, and functions.
- Handle exceptions gracefully and log errors to aid troubleshooting.
- Utilize `namedtuple` or `dataclasses` (Python 3.7+) for cleaner data structures.

**Dataclasses:**

```python
from dataclasses import dataclass

@dataclass
class Point:
    x: int
    y: int
```

---

## 24. Further Resources

- **Official Docs:** [https://docs.python.org/3/](https://docs.python.org/3/)
- **PEP 8 Style Guide:** [https://peps.python.org/pep-0008/](https://peps.python.org/pep-0008/)
- **Real Python Tutorials:** [https://realpython.com/](https://realpython.com/)
- **Read the Source Code:** `import this` and exploring `help()` in the REPL.

---
