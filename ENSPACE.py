# cook your dish here
t = int(input());
for _ in range(t):
    N,X,Y = map(int,input().split());
    if(X*1+Y*2<=N):
        print("YES");
    else:
        print("NO");