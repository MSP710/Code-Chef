# cook your dish here
def solution():
    X,Y,A = map(int,input().split());
    if(X<=A and Y>A):
        print("YES");
    else:
        print("NO");
    
t = int(input());
while(t>0):
    t = t - 1;
    solution();