import numpy as np
import joblib
import pandas as pd
url ='https://sleepster.blob.core.windows.net/newcontainer/Sleepsterdataset.xlsx?sp=r&st=2022-12-20T14:49:25Z&se=2022-12-20T22:49:25Z&spr=https&sv=2021-06-08&sr=b&sig=nZOiY3NqMQq9CoVPoXmoASfxMY5iuNWahD%2FKarVL8jw%3D'
df = pd.read_excel(url)
data['age']=data['age'].apply(np.ceil).astype(int)
data['weight']=data['weight'].apply(np.ceil).astype(int)
x=data.iloc[:,0:5]
y=data.iloc[:,-1]
model=RandomForestClassifier()
model.fit(x,y)
joblib.dump(model, "model.joblib", compress=3)
