#!/usr/bin/python3
# 1st way: Open the file in the text mode with UTF8 encoding
def read_file(filename=""):
    with open(filename, 'r', encoding='utf-8') as file:
        for line in file:
            print(line, end="")

# # 2nd way: whole file content shown at once
# def read_file(filename=""):
#     with open(filename, "r", encoding="utf-8") as file:
#         contents = file.read()
#     print(contents)
