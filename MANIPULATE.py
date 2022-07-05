# cook your dish here
def solution():
    X,Y = map(int,input().split());
    if(X>=Y):
        print("YES");
    else:
        print("NO");

t = int(input());
while(t>0):
    t = t - 1;
    solution();