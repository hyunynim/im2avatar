import ipyvolume as ipv
import h5py
import numpy as np

file_name = '../0.000.h5'
model = h5py.File(file_name, 'r')
data = np.array(model['data'][:])
X = data[:,:,:,0]
#Y = data[:,:,:,1]
#Z = data[:,:,:,2]

fig = ipv.figure()
ipv.volshow(X, controls=False, max_shape=64)
#ipv.volshow(Y, controls=False, max_shape=64)
#ipv.volshow(Z, controls=False, max_shape=64)
ipv.show()