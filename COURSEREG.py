# cook your dish here
def solution():
    N,M,K = map(int,input().split());
    if(M-K>=N):
        print("YES");
    else:
        print("NO");
    
t = int(input());
while(t>0):
    t = t - 1;
    solution();