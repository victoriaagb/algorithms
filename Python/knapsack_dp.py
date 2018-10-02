### Dynamic programming solution to the 0-1 Knapsack problem.
### Runs in O(nW) time, where
### n is the number of items and
### W is the maximum weight of items that can be put into the knapsack
### (this is Exercise 16.2-2 from INTRO.TO ALGORITHMS by Cormen).

def knapsack_dp(W, n, values, weights):
    #create a matrix of size n+1 x W+1 with zeros
    lookup = [0] * (n+1)
    for i in range(n+1):
        lookup[i] = [0] * (W+1)
   
    #iterate through all values
    for i in range(1, n+1):
        weight = weights[i-1]
        value = values[i-1]

    #iterate through all weights 
    for j in range(1, W+1):    
        prevW = lookup[i-1][j]
        if weight <= j:
            tempW = lookup[i-1][j-weight] + value
            lookup[i][j] = max(prevW, tempW)
        else:
            lookup[i][j] = prevW
    return (lookup)

def main():
    #input change to desired values and weights
    values = [100,120,60]
    weights = [2, 3, 1]
    W = 4
    n = len(values)
    lookup = knapsack_dp(W, n, values, weights)
    ksValue = lookup[n][W]
    ksItems = []

    i = n
    j = W
    #find which items are in the knapsack [1st to nth]
    while i > 0:
        if lookup[i][j] != lookup[i-1][j]:
            ksItems = [i] + ksItems
            j -= weights[i-1]
        i-=1      

    print ("Knapsack value: " + str(ksValue))
    print ("Knapsack items: " + str(ksItems))
