a=40 # the time-consuming of 5km without any training
b=36 # the time-consuming of 5km after the month of running training
c=30 # the time-consuming of 5km after a second mouth of running and strength training
d=a-b # the time improvement from running only
e=b-c # the time improvement from running and strength training
if d<e:
    print("running and strength training had a greater improvement")
else:
    print("running only had a greater improvement")

X=True 
Y=False
W=X or Y 
# A=ture B=ture W=False
#A=Ture B=False W=Ture
#A=False B=Ture W=Ture
#A=False B=False W=False
print(W)
