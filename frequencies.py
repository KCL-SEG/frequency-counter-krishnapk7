"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""

def frequencies(items):
    frequencies = {}
    for x in items:
        val = str(x)
        if frequencies.get(val) != None:
            num = frequencies[val]
            frequencies[val] = num + 1
        
        else:
            frequencies[val] = 1

    # Your code goes here
    return frequencies

frequencies((1,2,3,4,5,1))