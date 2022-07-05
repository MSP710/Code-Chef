# def solution():
#     X,Y,Z = map(int,input().split());
#     if(X%Y == 0):
#         n=X/Y;
#     else:
#         n=int(X/Y)+1;
#     print(n*Z);
    

# t = int(input());
# while(t>0):
#     t = t - 1;
#     solution();


n,atm=map(float,input().split())
n=int(n)
if (n+0.5<=atm and n%5==0):
    print(float(atm-n-0.5))
else:
    print(float(atm))
