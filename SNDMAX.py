# cook your dish here
def solution():
    n1,n2,n3 = map(int,input().split());
    ans = sorted([n1,n2,n3]);
    print(ans[1]);

t = int(input());
while(t>0):
    t = t - 1;
    solution();

