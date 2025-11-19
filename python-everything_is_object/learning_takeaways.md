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

- a **type** (what it is), shown with `type()`
- a **value** (what it holds)
- an **identity** (its unique memory address), shownwith `id()`

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

Common mutable types: `list`, `dict`, `set`, `bytearray` and user-defined objects.

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

Common immutable types: `int`, `float`, `complex`, `str`, `tuple`, `frozenset`, `bytes`, `bool`.

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
### How Immutable Objects are stored in memory
Python stores the value of immutable objects directly, and creates a new object (means new memory address) whenever the value has changed

_Memory Schema Example 1:_
```
a = 2
b = a
print(f"Before change, a is {a}")
print(f"Before change, b is {b}")

a = a + 3
print(f"After change, a is {a}")
print(f"After change, b is {b}")
```

_Output:_
```
Before change, a is 2
Before change, b is 2
After change, a is 5
After change, b is 2
```

_Memory Schema Example 2:_
```
name = "Da"
alias = name
print(f"Before change, name is {name}")
print(f"Before change, alias is {alias}")

name += "na"
print(f"After change, name is {name}")
print(f"After change, alias is {alias}")
```

_Output:_
```
Before change, name is Da
Before change, alias is Da
After change, name is Dana
After change, alias is Da
```

---
### Assignment vs Referencing
In Python, assignment does not copy the object.  It just creates a new reference to the same object.

_Example:_
```
a = [1, 2, 3]
b = a
```

Both a and b are now referencing to the same list object in memory. If one changes, the other one will also change.

---





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
### Passing Variables to a Function (By Assignment)
Python passes **object references, not the copies** into functions.

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

---
### Integer Pre-Allocation
When CPython starts, it preallocates the integers from -5 to 256.
That means those 262 small integers already exist in memory and they are reused every time we refer to them.

_Example:_
```
a = 250
b = 250
print(a is b) # True
```
Both a and b point to the same preallocated integer object.

**Two internal constants `NSMALLPOSINTS` & `NSMALLNEGINTS`**:
- `NSMALLPOSINTS` => 257 (covers 0 to 256)
- `NSMALLNEGINTS` => 5 (covers -1 to -5)

**Why `NSMALLPOSINTS` & `NSMALLNEGINTS` have those values**
The range covers -5 to 256 because those small integers are used most often in Python

**How `NSMALLPOSINTS` & `NSMALLNEGINTS` are used**:
They are used so that Python doesn't keep recreating integer objects within this range, which saves time and memory 
(to control integer caching in memory)

---
### Mechanism of Aliases
When two variables refer to the same object, they are aliases.

_Example:_
```
a = [1, 2, 3]
b = a
a.append(4)

print(a) 
print(b)  
```

_Output:_
```
[1, 2, 3, 4]
[1, 2, 3, 4]
```
Both a and b are pointing to the same list in memory, changing one affect the other.

---
### Special Case of Tuple and Frozen Set
Tuples and Frozen Sets are immutable but they can hold mutable objects inside them.

_Example:_
```
my_tuple = ([1, 2], 5)
my_tuple[0].append(100)

print(my_tuple)
```

_Output:_
```
([1, 2, 100], 5)
```

Note that the tuple itself is immutable, which means we cannot modify it. However, it contains a list (mutable), which we can modify the list.
