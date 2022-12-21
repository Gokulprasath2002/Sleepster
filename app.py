from flask import Flask,render_template,url_for,redirect,request
import numpy as np
import pandas as pd
import joblib
app = Flask(__name__)  

model = joblib.load("model.joblib")
@app.route('/')
def home():  
    return render_template("index.html");  
    
@app.route('/checking',methods=['POST'])
def checking():
    
    data=np.array(list(request.form.values()))
    values=model.predict([[data[1],data[2],data[3],data[4],data[5]]])
    if values == 0 :
        result="Don't worry, You don't have Insomnia"
        flag=0
    else:
        result="We are sorry but you have Insomnia"
        flag=1
    if data[7]=='yes'or 'YES' or 'Yes' or '1':
        mp=1
    else:
        mp=0
    return render_template('result.html',result=result,flag=flag,name=data[0],age=data[1],sleep=data[6],mp=mp,daysleep=data[8],drowsy=data[9])
if __name__ =='__main__':  
    app.run(host='0.0.0.0')  
