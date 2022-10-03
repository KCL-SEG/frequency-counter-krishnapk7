"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""

def frequencies(items):
    frequencies = {}
    for x in items:
        val = str(x)
        if(frequencies.keys().contains(val)):
        
            frequencies[val] = frequencies[val] + 1
        
        else:
            frequencies[val] = 0

    # Your code goes here
    return frequencies

