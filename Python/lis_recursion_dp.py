#!/usr/bin/python
import sys

### Efficient algorithm to find the length of a longest increasing subsequence entries.
### Ex. [11, 17, 5, 8, 6, 4, 7, 12, 3] a longest increasing subsequence is 5, 6, 7, 12.
### Dynamic Programming using Memoization.

def longest_increasing_sub(A, pos, lookup):
    item = A[pos]
    lis = [A[pos]] 
    temp = []   
    if pos < len(A)-1:
        for i in range (pos+1, len(A)):
            if lookup[i] == []:
                lookup = longest_increasing_sub(A, i, lookup)
            if item < A[i]:
                temp = [item] + lookup[i]
                lis = temp if len(lis) < len(temp) else lis
    lookup[pos] = lis
    return lookup


def main(argv):
    
    A = argv
    lookup = []
    lis = []
    if len(A) > 0:
        lookup = [[]]* len(A)
        lookup = longest_increasing_sub(A, 0, lookup)
        for i in lookup:
            lis = i if len(lis) < len(i) else lis
    print (lis)

  
            
if __name__ == "__main__":
    main(sys.argv[1:])
