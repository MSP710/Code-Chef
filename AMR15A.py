# cook your dish here
even = 0;
odd = 0;

N = int(input());
A = map(int,input().split());

for i in A:
    if(i%2 == 0):
        even+=1;
    else:
        odd+=1;
print("READY FOR BATTLE" if even > odd else "NOT READY");