#!/usr/bin/python3

filename = "test.txt"
search_string = "schwifty"

file = open(filename, "r")

for line in file:
    s = line

    if search_string in s:
        print(s)


