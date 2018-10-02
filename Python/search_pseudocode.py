#Binary search pseudocode algorithm
BSearch(A, k, p, r)

position = -1
if k == A[p]
    return p


else if p < r
    q = lower[(p+r)/2]

    result1 = Search(A, k, p, q)
    resutl2 = Search(A, k, q+1, r)

    if result1 != -1
        position = result1
    else if result2 != -1
        position = result2

return position

#Linear search pseudocode algorithm
Search(A, k, p, r)

position = -1
if p <= r
    for j = p to r
        if A[j] == k
            return j

return position
