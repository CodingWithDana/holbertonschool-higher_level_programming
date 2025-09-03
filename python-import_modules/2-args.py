#!/usr/bin/python3
import sys

if __name__ == "__main__":
    # excluding the script name
    argv = sys.argv[1:]
    count = len(argv)
    
    if count == 0:
        print("0 arguments.")
    elif count == 1:
        print("1 argument:")
    else:
        print(f"{count} arguments:")
    
    for i in range(len(argv)):
        # i+1 to start counting at 1
        print(i + 1, argv[i])
    