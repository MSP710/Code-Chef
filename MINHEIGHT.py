# cook your dish here
def solution():
    X,H = map(int,input().split());
    if(X>=H):
        print("YES");
    else:
        print("NO");

t = int(input());
while(t>0):
    t = t - 1;
    solution();