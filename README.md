# VarDelta
VarDelta is a library that allows you to easily track and access the history of a variable.

## Purpose
The purpose of VarDelta is to make arrays more user-friendly to those using Python as a tool rather than a programming
language. VarDelta was built to be used in PyActy, which is a library designed for accountants. By using VarDelta, it
makes it easier for an accountant to understand what the code is doing.

### Example
Without VarDelta, you could just as easily give a variable a history like so:
```python
# Create a variable with an initial value of 10.
x: list[int] = [10]
# Change the value of the variable to 5.
x.append(5)
# Access the current value of the variable.
print(x[-1])
# Access the previous value of the variable.
print(x[-2])
```
While this works perfectly fine, it may not be as easily understood by people with no prior familiarity with a
programming language. We can use VarDelta to do the exact same thing.
```python
from vardelta import Delta

# Create a variable with an initial value of 10.
x: Delta = Delta(10)
# Change the value of the variable to 5.
x.change_value(5)
# Access the current value of the variable.
print(x.get_value())
# Access the previous value of the variable.
print(x.get_value(1))
# You could also do:
print(x.value)
```
The two code snippets above do the exact same thing. The logic behind the `get_value()` function is that it retrieves
the value of the variable `n` amount of changes ago. By default, it'll get the value of the variable 0 changes ago, or
the current value. If we pass 1 in as an argument, we get the variable as it were 1 change ago.

Similar to an array, negative numbers retrieve from the opposite end of the array that positive numbers do, except the
opposite end is the beginning, and not the end of the array.
```python
# Retrieves the first value that the variable ever was.
print(x.get_value(-1))
```
This still sort of makes sense, as -1 retrieves the first value the variable was, -2 retrieves the second value the
variable was, and so on.

*Remember, it's not intended to make sense from a programmer's perspective.*