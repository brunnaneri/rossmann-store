import os
import pandas as pd
import pickle
from flask import Flask, request, Response
from rossmann.Rossmann import Rossmann


#loading model
model = pickle.load(open ('home/brunnaneri/repos/ds-em-producao/model/model_rossmann.pkl','rb'))

#inicialize API

app = Flask(__name__)
@app.route('/rossmann/predict',methods=['POST'])

def rossmann_predict():
    test_json = request.get_json()
    if test_json: #there is data
        if isinstance(test_json, dict):
            test_raw = pd.DataFrame(test_json, index=[0])
        
        else:
             test_raw = pd.DataFrame(test_json, columns = test_json[0].keys() )
        
        #Instantiate Rossmann Class
        pipeline = Rossmann()
        
        #Data Cleaning
        df1 = pipeline.data_cleaning(test_raw)
        
        #Feature Engineering
        df2 = pipeline.feature_engineering(df1)
        
        #Data Preparation
        df3 = pipeline.data_preparation(df2)
        
        #Prediction
        df_response = pipeline.get_prediction(model,test_raw,df3)
        
        return df_response
    
    else:
        return Response('{}',status=200, minetype='application/json')

if __name__ == "__main__":
    app.run('0.0.0.0')
