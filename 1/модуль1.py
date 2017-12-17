import random
def prosto_hernya(r, s1):
    a = []
    g=[]
    if (r == 1):
        #sumx=int(0)
        #sumy=int(0)
        A = int(input())
        B = int(input())  # в результате работы данная функция
        for i in range(s1):
            g.append(random.randint(A,B))
            for j in range(s1):
                a.append(g)
            g=[]
        for i in a:
             print(' '.join([str(j) for j in i]))
    else:
        for i in range(s1):
            for j in range(s1):
               n = int(input())
               for i in range(n):
                   u = int(input())
                   a.append(u)
        for i in a:
             print(' '.join([str(j) for j in i]))
        return a
l=prosto_hernya(1,2)
print(l)
def adtskoe_veselie(r,sl):
     k=[]
     k=prosto_hernya(r,sl)
     sumx=0
     print(k)
     for i in range(sl):
            for j in range(sl):
                sumx=sumx+k[i][j]
     return 1
m=adtskoe_veselie(1,2)
print(m)