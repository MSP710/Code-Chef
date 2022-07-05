# cook your dish here
def solution():
    X,Y = map(int,input().split());
    print(abs(X-Y));

t = int(input());
while(t>0):
    t = t - 1;
    solution();
