#!/usr/bin/python
import sys

### Efficient algorithm to find the amount of items in the longest increasing subsequence.
### Ex. [11, 17, 5, 8, 6, 4, 7, 12, 3] the longest increasing subsequence is 5, 6, 7, 12.
### The amount is 4.
### Precursor to finding the actual longest increasing subsequence.

def longest_increasing_sub(seq, pos):
    lis = 1
    if pos < len(seq)-1:
       for i in range(pos+1, len(seq)):
           if seq[pos] < seq[i]:
              lis = max(lis, longest_increasing_sub(seq, i) + 1)
           elif pos == 0:
              lis = max(lis, longest_increasing_sub(seq, i))
    return lis

def main(argv):
    
    seq=argv
    lis = 0
  
    if len(seq):
        lis = longest_increasing_sub(seq, 0)

    print(lis)
  
            
if __name__ == "__main__":
    main(sys.argv[1:])
