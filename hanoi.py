def move(a,b):
    t = a.pop()
    b.append(t)
    print(f'{t} moved from {a} to {b}')
    
def hanoi(n,src,temp,target):
    if n==1:
        move(src,target)
        return
    else:
        hanoi(n-1,src,target,temp)
        move(src,target)
        hanoi(n-1,temp,src,target)

a = [i for i in range(1,7)]
b = []
c = []
hanoi(6,a,b,c)
print(a,c)