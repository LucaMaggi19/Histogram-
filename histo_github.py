import numpy as np
### Upload the input and open the output files ####
his=np.loadtxt("Path_to_Input_file",usecols=range(2))
out1=open("path_to_output_file","w")

### Searching for the maximum and minimum Values in the dataset ####
leng=len(his)
leng=leng-1000
hmax=-1000000
hmin=10000000
sel=1
for t in range(leng):
 if his[t,sel] > hmax:
   hmax=his[t,sel]
 if his[t,sel] < hmin:
   hmin=his[t,sel]

### Binning the space ###
binn=250
h=np.zeros(binn+1)
delt=(hmax-hmin)/float(binn)

### Generating the histogram ####
for i in range(leng):
 db=(his[i,sel]-hmin)/delt
 dbn=int(db)
 h[dbn]=h[dbn]+1.0/float(leng)

#### Writing the histogram on the output file ####
for i in range(binn):
 b=hmin+float(i)*delt
 if b < hmax: 
  out1.write("%s" % b +"\t" "%s\n"  % h[i]   ) 
