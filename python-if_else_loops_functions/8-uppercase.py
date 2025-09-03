#!/usr/bin/python3
def uppercase(str):
    result = ""
    for char in str:
        # check if lowercase
        if 'a' <= char <= 'z':
            result += chr(ord(char) - 32)
        else:
            result += char
    print("{}".format(result))
