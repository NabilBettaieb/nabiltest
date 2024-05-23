#!/usr/bin/env python

import sys

# Read input from STDIN
for line in sys.stdin:
    # Split the line into words
    words = line.strip().split()
    for word in words:
        # Emit each word with a count of 1
        print(f"{word}\t1")