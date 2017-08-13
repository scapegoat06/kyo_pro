#coding:utf-8
N,M = map(int,input().split())
cor_list=[[] for i in range(N)]
a=[]
b=[]
c=[]
for m in range(M):
    ai,bi,ci=map(int,input().split())
    print(ai,bi,ci)
    a.append(ai)
    b.append(bi)
    c.append(ci*-1)
print(a,b,c)

dist=[]
for i in range(N):
    dist.append(1e+09)

dist[0]=0

for loop in range(N-1):
    for i in range(M):
        print(i)
        if dist[a[i]-1]==1e+09:continue
        if dist[b[i]-1]>dist[a[i]-1]+c[i]:
            dist[b[i]-1]=dist[a[i]-1]+c[i]

ans=dist[N-1]

negative=[]
for i in range(N):
    negative.append(False)


for loop in range(N):
    for i in range(M):
        if(dist[a[i]-1]==1e+09):continue
        if(dist[b[i]-1]>dist[a[i]-1]+c[i]):
            dist[b[i]-1]=dist[a[i]-1]+c[i]
            negative[b[i]-1]=True
        if(negative[a[i]-1]==True):
            negative[b[i]-1]=True

if negative[N-1]:
    print("inf")
else:
    print(-ans)
