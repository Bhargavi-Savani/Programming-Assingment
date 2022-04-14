def areaMax(A, Len) :
    Area = 0
    for i in range(Len) : 
        for j in range(i + 1, Len) : 
            Area = max(Area, min(A[j], A[i]) * (j - i)) 
    return Area
a = [1, 8, 6, 2, 5, 4, 8, 3, 7] 
b = [1, 1] 
l1 = len(a) 
print(areaMax(a, l1))
l2 = len(b) 
print(areaMax(b, l2))