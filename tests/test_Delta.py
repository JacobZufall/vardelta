"""
test_Delta.py
"""

from src.vardelta.Delta import Delta


my_value: Delta = Delta(1)
my_value.change_value(5)
assert my_value.get_change(0) == 4

print(my_value.changes)
print(my_value.values)
