#!/usr/bin/env python

# ---------------------------
# projects/collatz/Collatz.py
# Copyright (C) 2012
# Glenn P. Downing
# ---------------------------

# ------------
# collatz_read
# ------------

def collatz_read (r, a) :
    """
    reads two ints into a[0] and a[1]
    r is a  reader
    a is an array of int
    return true if that succeeds, false otherwise
    """
    s = r.readline()
    if s == "" :
        return False
    l = s.split()
    a[0] = int(l[0])
    a[1] = int(l[1])
    assert a[0] > 0
    assert a[1] > 0
    return True

# ------------
# collatz_eval
# ------------

def collatz_eval (i, j) :
    """
    i is the beginning of the range, inclusive
    j is the end       of the range, inclusive
    return the max cycle length in the range [i, j]
    """
    assert i > 0
    assert j > 0
    # <your code>

    m = 0
    x = i
    """ 
    cycle through every integer in the range i through j
    do cycle length for each integer in the range
    compare each new cycle length with the current max cycle length, m
    """
    while (x <= j) :
        c = 0
        c = collatz_cycle(x)
        m = collatz_max (c, m)
        x += 1
        
    return m


def collatz_max (c, m):
    """
    c is the most recent cycle length
    m is the current max cycle length
    return the the greater value of the c and m
    """
    if c > m:
        return c
    else :
        return m
    
def collatz_cycle(r) :
    """
    r is the integer for which the cycle length needs to be determined
    c keeps the count for the cycle length
    return c, the cycle length for the integer r
    """
    c = 1
    
    """ 
    do loop while r does not equal 1
    when r equals 1, stop and return c, the cycle length 
    """
    while r != 1:
        
        """ 
        if r is even, divide by 2 
        else multiply r by 3 and add 1
        """
        if (r%2 == 0) :
            r = r/2
            c += 1
        else :
            r = r*3 + 1
            c += 1
    
    return c

# -------------
# collatz_print
# -------------

def collatz_print (w, i, j, v) :
    """
    prints the values of i, j, and v
    w is a writer
    i is the beginning of the range, inclusive
    j is the end       of the range, inclusive
    v is the max cycle length
    """
    w.write(str(i) + " " + str(j) + " " + str(v) + "\n")

# -------------
# collatz_solve
# -------------

def collatz_solve (r, w) :
    """
    read, eval, print loop
    r is a reader
    w is a writer
    """
    a = [0, 0]
    while collatz_read(r, a) :
        v = collatz_eval(a[0], a[1])
        collatz_print(w, a[0], a[1], v)