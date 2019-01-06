#!/usr/bin/python3

filename = "text.txt"

file = open(filename, "r")

# create an empty list
lines = []

for line in file:
    # strip removes the newline
    # append adds to the list
    lines.append(line.strip())

lines.sort()
print(lines)