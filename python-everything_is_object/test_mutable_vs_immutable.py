# # 1. Tests using Immutable objects
# # Test 1.1
# tuple_1 = (1, 2, 3, 4)
# tuple_2 = (1, 2, 3)
# print(id(s1))
# print(id(s2))
# print(s1 == s2)
# print(tuple_1 is tuple_2)

# # Test 1.2
# def increment(n):
#     n += 1
#     print("Inside:", n)

# a = 1
# increment(a)
# print("Outside:", a)

# # 2. Tests using Mutable objects
# # Test 2.1
# a = [1, 2, 3]
# b = a
# a.append(4)
# print(a)
# print(b)          # [1, 2, 3, 4] (b changed too!)
# print(id(a))
# print(id(b))
# print(a == b)
# print(a is b)

# Test 2.2
def append_value(my_list):
    my_list.append(100)
    print("Inside:", my_list)

nums = [1, 2, 3]
append_value(nums)
print("Outside:", nums)