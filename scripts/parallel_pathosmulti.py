import collections
from pathos.multiprocessing import ProcessingPool as Pool
import pandas as pd
import time

def getAreaSlowTuples(x,verbose=False):
    x = tuple(x)
    if verbose: print(f'processing: {x[0]}')
    time.sleep(.05)
    result = {'ID':x[0],
            'sepArea':x[1] * x[2],
            'petArea':x[3] * x[4]}
    if verbose: print(f'done with: {x[0]}')
    return result

data = pd.read_csv('https://gist.githubusercontent.com/curran/a08a1080b88344b0c8a7/raw/0e7a9b0a5d22642a06d3d5b9bcbad9890c8ee534/iris.csv')
data.reset_index(inplace=True) #Use idx as identifier

## Convert dataset to tuple with names
irises = tuple(data.itertuples(name='Iris', index=False))
tIris = [tuple(_) for _ in irises]

### Multiprocessing implementation
pool4 = Pool(4)
pool8 = Pool(8)
pool16 = Pool(16)

## Map function over
print('4\n')
start = time.time()
resParallel = pool4.map(getAreaSlowTuples, tIris)
end = time.time()
print(f'time: {end-start:.4f}s\n')

## 8
print('8\n')
start = time.time()
resParallel = pool8.map(getAreaSlowTuples, tIris)
end = time.time()
print(f'time: {end-start:.4f}s\n')

## 16
print('16\n')
start = time.time()
resParallel = pool16.map(getAreaSlowTuples, tIris)
end = time.time()
print(f'time: {end-start:.4f}s\n')


#print(resParallel[0:5])