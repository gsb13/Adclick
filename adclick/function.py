from flask import Flask,request,jsonify
import pickle
import pandas as pd
import numpy


def PredictClickStatus(InputData):
    import pandas as pd
    Num_Inputs=InputData.shape[0]
    
    # Making sure the input data has same columns as it was used for training the model
    # Also, if standardization/normalization was done, then same must be done for new input
    
    # Appending the new data with the Training data
    DataForML=pd.read_pickle('DataForML.pkl')
    InputData=InputData.append(DataForML)
    
    # Treating the binary nominal variables first
    # Every column which was converted to numeric has to be converted here as well
    InputData['Male'].replace({'Yes':1, 'No':0}, inplace=True)
    
    # Generating dummy variables for rest of the nominal variables
    InputData=pd.get_dummies(InputData)
            
    # Maintaining the same order of columns as it was during the model training
    Predictors=["Time_Spent", "Avg_Income", "Internet_Usage"]
    
    # Generating the input values to the model
    X=InputData[Predictors].values[0:Num_Inputs]    
    
    # Loading the Function from pickle file
    import pickle
    with open('FinalAdaboostModel.pkl', 'rb') as fileReadStream:
        AdaBoost_model=pickle.load(fileReadStream)
        # Don't forget to close the filestream!
        fileReadStream.close()
            
    # Genrating Predictions
    Prediction=AdaBoost_model.predict(X)
    PredictedStatus=pd.DataFrame(Prediction, columns=['ClickPrediction'])
    return(PredictedStatus)


# Creating the function which can take Ad inputs and perform prediction
#"Time_Spent", "Avg_Income", "Internet_Usage"
def FunctionClickPrediction(inp_Time_Spent, inp_Avg_Income, inp_Internet_Usage):
    SampleInputData=pd.DataFrame(
     data=[[inp_Time_Spent, inp_Avg_Income, inp_Internet_Usage]],
     columns=["Time_Spent", "Avg_Income", "Internet_Usage"])

    # Calling the function defined above using the input parameters
    Predictions=PredictClickStatus(InputData= SampleInputData)
    print(Predictions)

    # Returning the predicted Clicked status
    return(Predictions.to_json())

# Function call
FunctionClickPrediction(inp_Time_Spent=40.97, 
                       inp_Avg_Income=55901.12,
                       inp_Internet_Usage=195.46
                       )
