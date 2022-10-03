"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""

def frequencies(items):
    frequencies = {}
    for x in items:
        if(frequencies[x]):
        
            frequencies[x] = frequencies[x] + 1
        
        else:
            frequencies[x] = 0

    # Your code goes here
    return frequencies

