a = [15, 1, 53, 26, 43, 31, 47, 39, 8, 5, 12, 25, 1, 93, 30, 60, 83, 58, 64, 3, 23, 16, 97, 33, 77, 11, 28, 90, 59, 95]
def selection_sort(listn):
    for i in range(len(listn)-1):
        p = i
        for j in range(i+1,len(listn)):
            if listn[j] < listn[p]:
                p = j
        if p != i:
            listn[i] , listn[p] = listn[p] , listn[i]
    print(listn)

selection_sort(a)