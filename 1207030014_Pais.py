print('+======== UAS PRAKTIKUM FISIKA KOMPUTASI =======+')
print('+============ FARIS HAIDAR MUBASYIR ============+')

import numpy as np
import csv
import time

from sklearn import svm
import pandas as pd

#Database: Gerbang LOgika AND
#Membaca data dari file
FileDB = 'database_pais.txt'
Database = pd.read_csv(FileDB, sep=",", header=0)

#x = Data, y=Target
X = Database[[u'a', u'b']]
y = Database.Target


clf = svm.SVC()
clf.fit(X.values,y)

print(clf.predict( [[5,2]] ))
print(clf.predict( [[2,5]] ))
print(clf.predict( [[3,6]] ))
print(clf.predict( [[1,2]] ))
print(clf.predict( [[4,4]] ))
print(clf.predict( [[2,9]] ))
print(clf.predict( [[5,10]] ))


