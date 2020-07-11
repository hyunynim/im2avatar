import numpy as np
import h5py
import sys
f = h5py.File('test.h5', 'r')
print(f)
print(list(f.keys()))
dset = f['data']

fp = open("res.txt", "w")
for i in range(0, 3):
    for j in range(0, 64):
        for k in range(0, 64):
            for l in range(0, 64):
                str = "%f " % dset[j][k][l][i]
                fp.write(str)
            fp.write('\n')
fp.close()