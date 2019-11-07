
### Estimate genotype likelihoods from BAM files
##### command:
./angsd -sites HC_RGupdate_norepMask_bwa4.SNPs -GL 2 -out genolike -nThreads 20 -doGlf 2 -doMajorMinor 1 -SNP_pval 1e-6 -doMaf 1  -bam bam.filelist

##### -sites = I gave it a list of SNP positions that I specifically wanted to assess. This is not typical.
##### GL = 2 --> GATK model (1=samtools)
##### doGLF = 2 --> beagle log like output
##### doMajorMinor 1 --> infer minor allele

### 


### Estimate covariance matrix and inbreeding coefficients
python pcangsd.py -beagle genolike2.beagle.gz -inbreed 1 -o all -threads 20
### 

### Plot PCA in python with pylab
See python script pca_plotter.py
