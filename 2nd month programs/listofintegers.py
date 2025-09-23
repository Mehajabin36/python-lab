print("lists of integers:")
list1=[1,2,3,4,5]
list2=[3,1,6,7,8,9]
a=len(list1)
print("length of first list is:",a)
b=len(list2)
print("length of second list is:",a)
if(a==b):
     print("length is same")
else:
     print("length is not same")
c=sum(list1)
print("sum=",c)
d=sum(list2)
print("sum=",d)
if(c==d):
     print("sum is equal")
else:
    print("sum is not equal")

for i in list1:
    for j in list2:
        if (i==j):
            print(i)
            
        


    
    
    
