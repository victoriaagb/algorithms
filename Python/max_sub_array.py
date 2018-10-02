### (this is Exercise 4.1-2 from INTRO.TO ALGORITHMS by Cormen).

def maximumSubarray(change):
    start = end = 0
    subProfit= change[0]
    
    for i in range(len(change)):
        tempTotal = 0
        for j in range (i, len(change)):
            tempTotal = tempTotal + change[j]
            if (tempTotal > subProfit):
                subProfit = tempTotal
                start = i
                end = j
    print ("Buy Day " + str(start))
    print ("Sell Day " + str(end))
    print ("profit = " + str(subProfit))

### (this is Exercise 4.1-5 from INTRO.TO ALGORITHMS by Cormen).
def maximumSubarrayLinear(change):
    #initialize dates and profit
    start = tempStart = 1
    end = tempEnd = 1
    profit = tempProfit = change[0]

    #iterate through array of numbers
    for i in range(1, len(change)):
        currentProfit = change[i]

        #store and update subarray sum
        tempProfit = currentProfit + tempProfit
        tempEnd = i + 1

        #restart subarray sum
        if (currentProfit >= tempProfit):
            tempProfit = currentProfit
            tempStart = i + 1

        #update maximum subarray
        if (tempProfit >= profit): 
            profit = tempProfit
            end = tempEnd
            start = tempStart
            

    print ("Buy Day " + str(start))
    print ("Sell Day " + str(end))
    print ("profit = " + str(profit))
            
