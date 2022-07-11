# cook your dish here
def solution():
    X,Y = map(int,input().split());
    X = X*10;
    Y = Y*90;
    print(X+Y);

t = int(input());
while(t>0):
    t = t - 1;
    solution();
