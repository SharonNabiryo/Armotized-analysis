#SHARON N NABIRYO

from random import randrange

def test(initialSize, probRemove):
    accCheap, accCosty = 0, 0
    s = initialSize
    m = 2*s
    for i in range(100000):
        if (randrange(100) < probRemove): # cheap
            if (s > 0):
                s -= 1
                accCheap += 1
        else:                             # costly
            if (s == m):
                m = m*2
                s += 1
                accCosty += 1
            else:                         # cheap
                s += 1
                accCheap += 1
                
    print("Initial size:", initialSize, "Prob Remove:", probRemove, "out of 100")
    print("Costy: {:7} ({:3.1}%)".format(accCosty,100*accCosty/(accCosty+accCheap)))
    print("Cheap: {:7} ({:3.1}%)".format(accCheap,100*accCheap/(accCosty+accCheap)))

def main(): # testcases
    test(10, 1)
    test(10, 5)
    test(20, 1)
    test(20, 5)
    test(50, 1)
    test(50, 5)
    test(100, 1)
    test(100, 5)
    test(1, 1)

   

    
main()


# Signifance

"""
It's hard to get at least 1% costly operations because dynamic arrays are designed to be very efficient.

Costly operations (when the array doubles its size) only happen occasionally, and most operations (appending or removing elements) are cheap.

If the initial size is too big, the array has lots of space at the start, so it takes longer to fill up and trigger a costly resize.
If the removal probability is too high, the array keeps shrinking, so it rarely reaches its capacity to need resizing.

This shows that dynamic arrays are great at keeping costly operations rare.

"""
