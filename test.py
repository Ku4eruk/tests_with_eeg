from files import *
from pyPTE import PTE
import random

files = file_reader()
file = files[0]
print(files[0])
signals, info = get_datum(file)
ch_names = info['ch_names']
ch_names = [i[4:] for i in ch_names]
print(ch_names)

s = signals[:19]
s1 = []
for i in s:
    #s1.append(i[:1000])
    s1.append([random.random() for i in range(1000)]) #using random signals to make easier tests

y = PTE(s1)
print('len y', len(y))
print('len y1', len(y[0]))
print('len y2', len(y[1]))
print('len y11', len(y[0][0]))
print('len y21', len(y[1][0]))