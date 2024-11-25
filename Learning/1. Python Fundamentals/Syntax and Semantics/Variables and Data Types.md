## **1. Variables**

### What is a Variable?
A variable is a container for storing data values. Think of it as a labeled box where you can keep your data for later use.

### Key Features of Python Variables:
- **No need to declare the type:** Python is dynamically typed, so you don’t need to specify the type of a variable (e.g., `int`, `float`, etc.). The type is inferred from the value assigned.
- **Case-sensitive:** Variable names are case-sensitive (`age` and `Age` are two different variables).
- **Naming Rules:**
  - Must start with a letter or an underscore (`_`).
  - Cannot start with a number.
  - Can contain letters, numbers, and underscores.
  - Cannot use reserved keywords (like `for`, `if`, `while`, etc.).

### Example:
```python
# Assigning values to variables
name = "Alice"       # A string
age = 25             # An integer
height = 5.6         # A float
is_student = True    # A boolean

print(name, age, height, is_student)
```

---

## **2. Constants**

Unlike variables, **constants** are values that do not change during the program's execution. Python does not have built-in constant support, but by convention:
- Use **uppercase** variable names to indicate constants.

### Example:
```python
PI = 3.14159     # Constant for the value of Pi
GRAVITY = 9.8    # Constant for gravitational force

print("Pi:", PI)
print("Gravity:", GRAVITY)
```

---

## **3. Data Types**

Python has several built-in data types. Let’s explore the most common ones:

### **A. Integers (`int`)**
- Used to store whole numbers.
- No decimal point.
- Can be positive or negative.
  
### Example:
```python
x = 10       # Integer
y = -5       # Negative integer
z = 0        # Zero

print(type(x))   # Output: <class 'int'>
```

---

### **B. Floating-Point Numbers (`float`)**
- Used to store numbers with a decimal point.
- Can also represent scientific notation (e.g., `1.2e3` for 1200).

### Example:
```python
pi = 3.14159    # Float
scientific = 1.2e3  # Scientific notation (1200.0)

print(type(pi))         # Output: <class 'float'>
print(scientific)       # Output: 1200.0
```

---

### **C. Strings (`str`)**
- Used to store text data.
- Enclosed in single (`'`) or double (`"`) quotes.
- Strings are **immutable** (cannot be changed after creation).

### Example:
```python
greeting = "Hello, World!"     # String in double quotes
single_quote = 'Python is fun' # String in single quotes

# String Concatenation
message = greeting + " " + single_quote

print(message)                 # Output: Hello, World! Python is fun
print(type(message))           # Output: <class 'str'>
```

---

### **D. Booleans (`bool`)**
- Represents one of two values: `True` or `False`.
- Often used in conditional statements or logical expressions.

### Example:
```python
is_python_fun = True     # Boolean
is_raining = False       # Boolean

print(is_python_fun)     # Output: True
print(type(is_python_fun))  # Output: <class 'bool'>
```

---

## **4. Checking Data Types**

You can use the `type()` function to check the data type of a variable.

### Example:
```python
x = 42
y = 3.14
z = "Hello"
w = True

print(type(x))  # Output: <class 'int'>
print(type(y))  # Output: <class 'float'>
print(type(z))  # Output: <class 'str'>
print(type(w))  # Output: <class 'bool'>
```

---

## **5. Dynamic Typing in Python**

In Python, you can reassign a variable to a value of a different type. This is because Python is **dynamically typed**.

### Example:
```python
x = 10          # Initially an integer
print(type(x))  # Output: <class 'int'>

x = 3.14        # Reassigned to a float
print(type(x))  # Output: <class 'float'>

x = "Now a string!"  # Reassigned to a string
print(type(x))  # Output: <class 'str'>
```

---

## **6. Input and Type Conversion**

When you take input from the user using `input()`, it is always treated as a string. You may need to convert it to another data type (e.g., `int`, `float`).

### Example:
```python
# Taking input and converting to an integer
age = input("Enter your age: ")
age = int(age)   # Convert to integer
print("Your age is:", age)
print(type(age)) # Output: <class 'int'>
```

### Type Conversion Functions:
- `int()`: Converts to an integer.
- `float()`: Converts to a float.
- `str()`: Converts to a string.
- `bool()`: Converts to a boolean.

---

## **7. Common Operations**

Here are some basic operations you can perform with these data types:

### Arithmetic Operations:
- **Integers and Floats**: Support addition, subtraction, multiplication, division, modulus, etc.
  ```python
  x = 10
  y = 3

  print(x + y)    # Addition: 13
  print(x - y)    # Subtraction: 7
  print(x * y)    # Multiplication: 30
  print(x / y)    # Division: 3.333...
  print(x % y)    # Modulus (remainder): 1
  print(x // y)   # Floor division: 3
  print(x ** y)   # Exponentiation: 1000
  ```

### String Operations:
- Strings allow concatenation and repetition.
  ```python
  name = "Alice"
  greeting = "Hello, " + name  # Concatenation
  repeated = name * 3          # Repetition

  print(greeting)  # Output: Hello, Alice
  print(repeated)  # Output: AliceAliceAlice
  ```

---

## **8. Example Program: Combining Variables and Data Types**

Here’s a simple program that demonstrates variables and data types together:

```python
# User details
name = input("What is your name? ")      # String input
age = int(input("How old are you? "))    # Integer input
height = float(input("What is your height in meters? "))  # Float input
is_student = input("Are you a student? (yes/no): ").lower() == "yes"  # Boolean

# Display the details
print("\nUser Details:")
print(f"Name: {name}")
print(f"Age: {age}")
print(f"Height: {height} meters")
print(f"Student: {is_student}")
```

---

### **Key Takeaways:**
1. Variables are containers for data values and can hold different types of data.
2. Python has basic data types like integers, floats, strings, and booleans.
3. Use `type()` to check the data type of a variable.
4. Python is dynamically typed, so variables can change types during execution.
5. Input data is always a string and must be converted to other types if needed.