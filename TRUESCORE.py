# cook your dish here
def solution():
    A,B = map(int,input().split());
    C,D = map(int,input().split());
    if(A<=C and B<=D):
        print("POSSIBLE");
    else:
        print("IMPOSSIBLE");

t = int(input());
while(t>0):
    t = t - 1;
    solution();