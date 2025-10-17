print("square of the keys in a dictionary")
n=int(input("enter a number:\n"))
d=dict()
for i in range(1,n+1):
    d[i]=i*i
if n<=15:
    print(d)
