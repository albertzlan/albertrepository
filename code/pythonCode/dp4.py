import sys

def dp4(num,cost,cc,dst):
    if num==1:
        return(min(cost[0],cost[1]))
    if num==0:
        return(cost[0])
    if num<0:
        return(0)
    
    print([num,cc[num-1]])
    if cc[num-1]>0:
        print("1>0")
        return cc[num-1]
    if cc[num-2]>0:
        print("2>0")
        return cc[num-2]
    
    print(num)
    t1=0;t2=0
    t1=dp4(num-1,cost,cc,dst)+cost[num-1]
    t2=dp4(num-2,cost,cc,dst)+cost[num-2]
    if (t1)>(t2):
        dst=dp4(num-2,cost,cc,dst)
        cc[num-2]=dst
    else:
        dst=dp4(num-1,cost,cc,dst)+cost[num-1]
        cc[num-1]=dst
    return dst



num=10
cost=list(map(int,"1 100 1 1 1 90 1 1 80 1".split()))
cc=[0 for ii in range(num)]
dst=0
print(dp4(num,cost,cc,dst))
