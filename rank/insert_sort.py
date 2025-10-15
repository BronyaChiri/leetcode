a = [15, 1, 53, 26, 43, 31, 47, 39, 8, 5, 12, 25, 1, 93, 30, 60, 83, 58, 64, 3, 23, 16, 97, 33, 77, 11, 28, 90, 59, 95]
def insert_sort(listn):
    for i in range(1,len(listn)):
        tem = listn[i]
        for t in range(i):
            if tem < listn[t]:
                
                break
        else:
             t = i

        for p in range(i-1,t-1,-1):
            listn[p+1] = listn[p]
        listn[t] = tem
    print(listn)
            
insert_sort(a)