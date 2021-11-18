
from flask import Flask, config,request,jsonify
import pickle
import pandas as pd
import numpy
import os

from adclick import function

app = Flask(__name__)
@app.route('/get_click_prediction', methods=["GET"])
def get_click_prediction():
    try:
        # Getting the paramters from API call
        Time_Spent_value = float(request.args.get('Time_Spent'))
        Avg_Income_value = float(request.args.get('Avg_Income'))
        Internet_Usage_value=float(request.args.get('Internet_Usage'))

        
                
        # Calling the funtion to get click status
        prediction_from_api=function.FunctionClickPrediction(inp_Time_Spent=Time_Spent_value,
                               inp_Avg_Income=Avg_Income_value, 
                               inp_Internet_Usage=Internet_Usage_value,
                               )

        


        return (prediction_from_api)
    
    except Exception as e:
        return('Something is not right!:'+str(e))


if __name__ =="__main__":
    
    # Hosting the API in localhost
    app.run(host='127.0.0.1', port=8080, threaded=True, debug=True, use_reloader=False)

    #app.run(host='0.0.0.0', port=config.PORT_NUMBER,debug=True)
