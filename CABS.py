# cook your dish here

t = int(input())
for _ in range(t):
    X,Y = map(int,input().split())
    
    if X<Y:
        print("FIRST");
    elif X>Y:
        print("SECOND");
    else:
        print("ANY");