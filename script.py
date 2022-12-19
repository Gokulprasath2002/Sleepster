import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import pickle
import bz2
data=pd.read_excel("Sleepsterdataset.xlsx")
data['age']=data['age'].apply(np.ceil).astype(int)
data['weight']=data['weight'].apply(np.ceil).astype(int)
x=data.iloc[:,0:5]
y=data.iloc[:,-1]
model=RandomForestClassifier()
model.fit(x,y)
def compressed_pickle(title, data):

    with bz2.BZ2File(title + '.pbz2', 'w') as f:
        pickle.dump(data, f)
compressed_pickle('filename', model)