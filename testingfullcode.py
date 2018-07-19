#READING FROM INPUT FILE
f = open("inputfile.txt", "r") #opens file
N=int(f.readline())
mutationPB=float(f.readline())
maxiter=int(f.readline())
f.close()
import random
#GENOME MATRIX GENERATION FOR 4 QUEENS and 4 BISHOPS
import random
matgenome=[]
for i in range(0,N):
    matgenome.append([])
for i in range(0,N):
    zerocount=0
    onecount=0
    for j in range (0,N):
        a=random.randrange(0, 2, 1)
        if a==0 and zerocount<int(N/2):
            zerocount=zerocount+1
            matgenome[i].append(0)
        elif onecount<N/2:
            matgenome[i].append(1)
            onecount=onecount+1
        elif onecount>zerocount:
            matgenome[i].append(0)
        else:
            matgenome[i].append(1)
#RANDOM N no. POPULATION
mat=[]
ap=[]
def Population():
    matrix=mat
    for i in range(0,N):
        list=random.sample(range(1,N+1),N)
        matrix.append(list)
    return matrix
#PRINTING RANDOM POPULATION
mat=Population()
countmain=0
genome=[1,0,0,1,1,0,1,1]
while countmain<maxiter:
    #AP COUNTING FOR QUEENS & BISHOP
    fitness=[]
    #genome=[1,0,0,1,1,0,1,1] #here 0 denote Queen & 1 denote Bishop
    k=0
    while k<N: 
        ap=0
        for i in range(0,N):
            for j in range(i+1,N):
                if matgenome[k][i]==0:
                    if mat[k][i]==mat[k][j] or abs(mat[k][i]-mat[k][j]) == abs(i-j):
                        ap=ap+1
                elif matgenome[k][i]==1:
                    if abs(mat[k][i]-mat[k][j]) == abs(i-j):
                        ap=ap+1
                    elif mat[k][i]==mat[k][j] and matgenome[k][j]==0:
                        ap=ap+1
        fitness.append(ap)
        k=k+1
    #FITNESS / NONAP CALCULATION
    fitnessPB=[]
    nonAP=[]
    ncr=int((N*(N-1))/2)
    for i in range(0,N):
        nonAP.append(ncr-fitness[i])
    #RANDOM SELECTION FOR K TOURNAMENT
    KTselection=[]
    k=int(len(mat)/2)
    k2=5 #k2 er value
    randomnolist2=[]
    def RandomGeneration():    
        count=0
        flag=[]
        randomnolist=randomnolist2
        selection=KTselection
        while count<k2:
            rnum=random.randrange(0, N, 1)
            randomnolist.append(rnum)    
            selection.append(rnum)
            count=count+1
        return selection,randomnolist
    #K TOURNAMENT SELECTION
    count=0
    selectionResult=[]
    while count<k:
        randomnolist2=[]
        KTselection=[]
        KTselection,randomnolist2=RandomGeneration()
        idxtrack=0
        maximum=nonAP[randomnolist2[0]]
        for i in range(1,k2):
            if maximum<nonAP[randomnolist2[i]]:
                maximum=nonAP[randomnolist2[i]]
                idxtrack=randomnolist2[i]
            elif nonAP[randomnolist2[0]]>=maximum:
                idxtrack=randomnolist2[0]
        selectionResult.append(idxtrack)
        count=count+1
    #DAVIS’S ORDER CROSSOVER (OX1)
    def DavisOrderCrossover(p1,p2,a,b):
        c1=[]
        start=a
        end=b
        for i in range(0,len(p1)):
            if i>=start and i<=end:
                c1.append(p1[i])
            else:
                c1.append('#')
        iteration=len(p1)-(end-start+1)
        count=0
        p2idx=end
        c1idx=end
        while count<iteration:
            flag=0
            p2idx=p2idx+1
            p2idx=p2idx%(len(p2))
            for i in range(start,end+1):
                if p2[p2idx]==c1[i]:
                    flag=1
            if flag==0:
                c1idx=c1idx+1
                c1idx=c1idx%(len(c1))
                c1[c1idx]=p2[p2idx]
                count=count+1
            else:
                continue  
        return c1
    crossoverResult=[]
    cotimes=len(selectionResult)/2
    count=0
    i=0
    while count<cotimes:
        a=random.randrange(0, N, 1)
        b=random.randrange(0, N, 1)
        if a>b:
            start=b
            end=a
        else:
            start=a
            end=b
        p1=mat[selectionResult[i]]
        p2=mat[selectionResult[i+1]]
        c=DavisOrderCrossover(p1,p2,start,end)
        crossoverResult.append(c)
        c=DavisOrderCrossover(p2,p1,start,end)
        crossoverResult.append(c)
        count=count+1
    #SWAP MUTATION
    def swap(p1,x,y):
        p1[x],p1[y]=p1[y],p1[x]
        return p1
    def SwapMutation(p1):
        a=random.randrange(0, N, 1)
        b=random.randrange(0, N, 1)
        
        pp=swap(p1,a,b)
        
        return pp
    mutationResult=[]
    n=N/2
    count=0
    i=0
    while count<n:
        mPB=random.randrange(1, 101, 1)
        
        p=crossoverResult[i]
        if mPB>=1 and mPB<=int(mutationPB*100):
            pp=SwapMutation(p)
            mutationResult.append(pp)
        else:
            mutationResult.append(p)
        i=i+1
        count=count+1

    #APPENDING TO MAT AFTER MUTATION
    n=N/2
    count=0
    i=0
    while count<n:
       mat.append(mutationResult[i])
       i=i+1
       count=count+1
    #GENOME MATRIX GENERATION 2 For Children
    import random
    matgenome2=[]
    for i in range(0,int(N/2)):
        matgenome2.append([])
    for i in range(0,int(N/2)):
        zerocount=0
        onecount=0
        for j in range (0,N):
            a=random.randrange(0, 2, 1)
            if a==0 and zerocount<int(N/2):
                zerocount=zerocount+1
                matgenome2[i].append(0)
            elif onecount<int(N/2):
                matgenome2[i].append(1)
                onecount=onecount+1
            elif onecount>zerocount:
                matgenome2[i].append(0)
            else:
                matgenome2[i].append(1)
    #APPENDING TO MATGENOME AFTER CROSSOVER
    n=N/2
    count=0
    i=0
    while count<n:
       matgenome.append(matgenome2[i])
       #matgenome2.append(matgenome[i+1])
       i=i+1
       count=count+1
    #AP COUNTING FOR QUEENS & BISHOP AFTER MUTATION
    genome=[1,0,0,1,1,0,1,1] #here 0 denote Queen & 1 denote Bishop
    k=0
    n=int(N/2)
    while k<n: 
        ap=0
        flag=0
        for i in range(0,N):
            for j in range(i+1,N):
                if matgenome2[k][i]==0:
                    if mutationResult[k][i]==mutationResult[k][j] or abs(mutationResult[k][i]-mutationResult[k][j]) == abs(i-j):
                        ap=ap+1
                elif matgenome2[k][i]==1:
                    if abs(mutationResult[k][i]-mutationResult[k][j]) == abs(i-j):
                        ap=ap+1
                    elif mutationResult[k][i]==mutationResult[k][j] and matgenome2[k][j]==0:
                        ap=ap+1
        fitness.append(ap)
        k=k+1
    #FITNESS CALCULATION NonAP AFTER MUTATION
    nonAP=[]
    n=int(N+(N/2))
    ncr=int((N*(N-1))/2)
    for i in range(0,n):
        nonAP.append(ncr-fitness[i])
    #SORTING POPULATION ACCORDING TO FITNESS
    n=int(N+(N/2))
    for i in range(0,n):
        for j in range(i+1,n):
            if nonAP[i]<nonAP[j]:
                temp=nonAP[i]
                nonAP[i]=nonAP[j]
                nonAP[j]=temp

                temp2=mat[i]
                mat[i]=mat[j]
                mat[j]=temp2

                temp3=fitness[i]
                fitness[i]=fitness[j]
                fitness[j]=temp3

                temp4=matgenome[i]
                matgenome[i]=matgenome[j]
                matgenome[j]=temp4
    #REMOVING LESSFIT POPULATION
    count=0;
    i=N+int(N/2)
    while count<int(N/2):
        i=i-1
        mat.remove(mat[i])
        nonAP.remove(nonAP[i])
        fitness.remove(fitness[i])
        matgenome.remove(matgenome[i])
        count=count+1
    #FINDING SOLUTION
    array28=[]
    array0=[]
    array0genome=[]
    for i in range(0,N):
        if nonAP[i]==28:
            array28.append(mat[i])
        if fitness[i]==0:
           array0.append(mat[i])
           array0genome.append(matgenome[i])
    countmain=countmain+1
#Printing
#print(array28)
print(array0genome)
print(array0)
