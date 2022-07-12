# cook your dish here
def solution():
    A,B,C = map(int,input().split());
    print(max(A,B,C));

t = int(input());
while(t>0):
    t = t - 1;
    solution();
