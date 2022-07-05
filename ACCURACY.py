# cook your dish here
def solution():
    X = int(input());
    if X % 3:
        print(3- X % 3);
    else:
        print(0);
        
        
t = int(input());
while(t>0):
    t = t - 1;
    solution();
    