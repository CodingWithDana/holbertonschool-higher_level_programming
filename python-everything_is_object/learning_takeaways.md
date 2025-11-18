## Python: Everything is Object

<img width="1000" height="400" alt="image" src="https://github.com/user-attachments/assets/b072e900-54f7-419b-85b1-63846f3d6165" />

---

### Introduction
When we write code in Python, we often talk about “variables” and “values”; however, under the hood, what we’re really working with are objects in memory. 

Every number, string, list, or even function that we create is an object.

Understanding how Python stores and handles these objects, especially the difference between mutable and immutable types, is essential to writing bug-free code.

---
### id() and type()
How Python sees our object

Every object in Python has:

- a **type** (what it is)
- a **value** (what it holds)
- an **identity** (its unique memory address)

_Example:_
```
a = [1, 2, 3]

print(type(a))   # print type of the object

print(id(a))     # print the memory address of the object
```

_Output:_
```
<class 'list'>

139926795932424
```

If we later reassign **a**:

_Example:_
```
a = [1, 2, 3]

a = a + [4]

print(id(a))
```

_Output:_
```
139762597923567
```
Python created a new list object (so new memory address) when you used **+**. The old one still exists until garbage-collected.

---
### Mutable Objects
Mutable objects are those that can be changed, meaning we can modify their contents without creating a new object.

Common mutable types: `list`, `dict`, `set`, and user-defined objects.

_Example:_
```
my_list = [1, 2, 3]

print(id(my_list))     # 140231472

my_list.append(4)

print(my_list)         # [1, 2, 3, 4]

print(id(my_list))     # 140231472 (same!)
```

The same memory address proves that the list itself was modified and no new list created.

---
### Immutable Objects
Immutable objects cannot change once created.

If we “modify” them, Python silently creates a new object instead.

Common immutable types: `int`, `float`, `str`, `tuple`, `bool`.

_Example:_
```
a = "Best"

print(id(a))        # 4319301456

a += "School"

print(a)            # 'Best School'

print(id(a))        # 4319319728 (different!)
```

Even though we used **+=**, Python created a brand new string and made **a** point to it.

---
### Why It Matters: Python Treats Them Differently
Because Python objects behave differently depending on mutability, understanding this helps avoid subtle bugs.

_Example 1: with **immutable** objects (`str`)_
```
s1 = "Best School"

s2 = "Best School"

print(s1 == s2)  # True  (same value)

print(s1 is s2)  # Might be False (different memory address)
```

_Example 2: with **mutable** objects (`list`)_
```
a = [1, 2, 3]

b = a

a.append(4)

print(a)          # [1, 2, 3, 4]

print(b)          # [1, 2, 3, 4] (b changed too!)

print(a == b)     # True (same value)

print(a is b)     # True (same list object so same memory address)
```

Both **a** and **b** refer to the same list object (so same memory address), so changing one changes both.

This doesn’t happen with immutable types because we can’t modify them in place.

---
### How Arguments Are Passed to Functions
Python passes **object references not the copies** into functions.

That means the behavior depends on whether the object is mutable or immutable.

_Example: with an **immutable** object (`int`)_
```
def increment(n):
    n += 1
    print("Inside:", n)


a = 1
increment(a)
print("Outside:", a)
```

Output:
```
Inside: 2

Outside: 1
```

**a** stays the same, because integers are immutable, so **n += 1** created a new object inside the function.

_Example: with a **mutable** object (`list`)_
```
def append_value(my_list):
    my_list.append(100)
    print(my_list)


nums = [1, 2, 3]
append_value(nums)
print(nums)
```

_Output:_
```
[1, 2, 3, 100]
[1, 2, 3, 100]
```

The function changed the original list because lists are mutable, so both **nums** and **my_list** refer to the same object in memory.
