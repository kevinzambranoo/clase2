import pickle

import numpy as np
from schemas.cultivo_schemas import CultivoData

with open('RFCultivoV01.pkl','rb') as file:
    model = pickle.load(file)

labels = ['rice',
 'maize',
 'chickpea',
 'kidneybeans',
 'pigeonpeas',
 'mothbeans',
 'mungbean',
 'blackgram',
 'lentil',
 'pomegranate',
 'banana',
 'mango',
 'grapes',
 'watermelon',
 'muskmelon',
 'apple',
 'orange',
 'papaya',
 'coconut',
 'cotton',
 'jute',
 'coffee']    

def cultivo_prediction(data: CultivoData):

    xin = np.array([
        data.N,
        data.P,
        data.K,
        data.temperature,
        data.humidity,
        data.ph,
        data.rainfall,
    
    ]).reshape(1,7)

    prediction = model.predict(xin)

    print("prediccion: ", prediction)

    return prediction[0]
