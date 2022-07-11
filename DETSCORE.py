# cook your dish here
def solution():
    X,N = map(int,input().split());
    ans = int((X/10)*N);
    print(ans);

t = int(input());
while(t>0):
    t = t - 1;
    solution();