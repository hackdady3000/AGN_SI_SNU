import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

columns = []
data = []
with open('AGNgas_table_all.txt') as f:
    i = 0
    lines = f.readlines()
    for line in lines:
        if i == 0:
            columns = line.split()
            i+=1
            continue
        data.append(dict(zip(columns, line.split())))

### Get necessary data
FE_MG = []
for dat in data:
    FE_MG.append({dat['haloID']: float(dat['iron_gas']), 't': float(dat['z']) })
    #print(FE_MG)

### Create massive of names
str='a'
halo_names=[]
print(data[0]['haloID'])
print(len(data))
for j in range(len(data)):
    if  data[j]['haloID'] not in halo_names:
        halo_names.append(data[j]['haloID']) 
print(halo_names)

### Split data for halos
met =[]
time=[]
for i in range(len(halo_names)):
    eachhm=[]
    eachht=[]
    for j in FE_MG:
        for k in j:
            if k==halo_names[i]:
                eachhm.append(j[halo_names[i]]/1000) 
                eachht.append(j['t']+1) 
    met.append(eachhm)
    time.append(eachht)
#print(met)
print(met[0][0])
print(time[0][0])  

### Creating plot
#print(y_ax.size)
WD = 'D:/SNU2022/Research/AGN_SI_SNU/'
fig, ax = plt.subplots()
ax.set_xlabel('$z+1$')
ax.set_xlim(0,4)
ax.set_ylabel('$MGmass/10^3*Msolar$')
c=[]
halo=[]
for i in range(len(halo_names)):
    color =0+i*10
    c=np.full(len(met[i]),color)
    str=halo_names[i]
    #for j in range(len(time[i])):
        #ax1.plot(j['t'],'b',j[str])
    halo.append(ax.scatter(time[i], met[i], s=6, c=c, vmin=0, vmax=100,label=halo_names[i]))

ax.legend(handles=halo)
#plt.show()
plt.savefig('Mg.png', dpi=300)