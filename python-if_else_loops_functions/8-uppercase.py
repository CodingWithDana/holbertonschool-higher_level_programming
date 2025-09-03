#!/usr/bin/python3
def uppercase(str):
    for char in str:
        # check if lowercase 
        if 'a' <= char <= 'z':
            print("{}".format(chr(ord(char) - 32)), end="")
        else:
            print("{}".format(char), end="")
    print()
