import csv
import matplotlib.pyplot as plt
import numpy as np

trans = []
with open ('test_dataset/transactions.csv') as f:
    r = csv.reader(f)
    next(r)
    sortedlist = sorted(r, key=lambda row: int(row[6]), reverse=True)
    
    for i in sortedlist:
        trans.append(i[6])
    print(trans)

def count_elements(seq):
    hist = {}
    for i in seq:
        hist[i] = hist.get(i, 0) + 1
    return hist

trans_freq = count_elements(trans)
print(trans_freq)

int_keys = []

for i in trans_freq.keys():
    int_keys.append(int(i))

plt.bar(int_keys, trans_freq.values(), 0.75, color='g')
plt.grid(axis='y')
plt.xlabel('Transaction Count')
plt.ylabel('Frequency')


plt.show()