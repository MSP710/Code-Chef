# cook your dish here
def solution():
    X,Y,Z = map(int,input().split());
    if(X%Y == 0):
        n=int(X/Y);
    else:
        n=int(X/Y)+1;
    print(n*Z);
    

t = int(input());
while(t>0):
    t = t - 1;
    solution();