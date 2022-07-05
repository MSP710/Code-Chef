# cook your dish here
# def solution():
#     X,Y = map(int,input().split());
#     if(X*1.07>=Y):
#         print("YES");
#     else:
#         print("NO");
    
# t = int(input());
# while(t>0):
#     t = t - 1;
#     solution();
t = int(input());
for _ in range(t):
    X,Y = map(int,input().split());
    if(X*1.07>=Y):
        print("YES");
    else:
        print("NO");