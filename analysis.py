import math
sizes=[]
with open("ans.txt",'r') as f:
    for line in f.readlines():
        sizes.append((int(line)))

sizes.sort()
w=[0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.75,0.8,0.85,0.9,0.95]
s=len(sizes)
for widthpercent in w:
    width=math.floor(s*widthpercent)
    ans=sizes[-1]-sizes[0]
    ansl=sizes[0]
    ansr=sizes[-1]
    for r in range(width,s):
        l=r-width
        if(sizes[r]-sizes[l]<ans):
            ans=sizes[r]-sizes[l]
            ansl=sizes[l]
            ansr=sizes[r]
    print(widthpercent,': ',ansl,' - ',ansr)




import matplotlib.pyplot as plt
import numpy as np
plt.hist(sizes,bins=1000)
plt.show()

logsizes=[]
for a in sizes:
    logsizes.append(math.log10(a+1))
plt.xticks(np.arange(0,10,0.5),np.arange(0,10,0.5))
plt.hist(logsizes,bins=100)
plt.show()

