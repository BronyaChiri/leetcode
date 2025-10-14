def bubble_sort(listn):
    length = len(listn)
    for i in range(0,length):
        for j in range(0,length - 1 - i):
            if listn[j] > listn[j+1] :
                listn[j+1] , listn[j] = listn[j] , listn[j+1]
    return listn

a = [4,784,7,7,377,778,3332,787,1,78,8,1,3,4,6,76,889,545]
print(bubble_sort(a))




            