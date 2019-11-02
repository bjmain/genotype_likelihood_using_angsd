import pylab as plt
import numpy as np
C = np.genfromtxt("all.cov") # Reads in estimated covariance matrix
#S = np.load("all.inbreed.npy") # Reads results from selection scan
        
eig_vals, eig_vecs = np.linalg.eig(C)
print(sorted(eig_vals))
names = [N.strip().strip("./").split("_")[0] for N in open("bam.filelist")]
counter=-1
coav=0
for sample in eig_vecs:
    pc1=float(sample[0])
    pc2=float(sample[1])
    counter+=1
    name = names[counter]
    if "COAV" in name:
        if not coav:
            plt.text(pc1,pc2,"COAV samples")
        coav+=1
        plt.plot(pc1,pc2,'ro')
        continue
    if name=="f":
        name="KNWR"
    #name = i[0]
    #print name, pc1, pc2
    #print(name,pc1,pc2)
    plt.text(pc1,pc2,name)
    plt.plot(pc1,pc2,'k.')
plt.xlabel("PCA1",fontsize=20)
plt.ylabel("PCA2",fontsize=20)
#print(eig_vecs)
plt.show()
