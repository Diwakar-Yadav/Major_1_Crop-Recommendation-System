import numpy as np
import pandas as pd
from flask import Flask, request, render_template
import pickle
from sklearn.preprocessing import MinMaxScaler

# Load the model and scaler
model = pickle.load(open('model.pkl', 'rb'))
scaler = pickle.load(open('minmaxscaler.pkl', 'rb'))

# Initialize the Flask app
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    Nitrogen = int(request.form['Nitrogen'])
    Phosphorus = int(request.form['Phosphorus'])
    Potassium = int(request.form['Potassium'])
    Temperature = float(request.form['Temperature'])
    Humidity = float(request.form['Humidity'])
    pH_Value = float(request.form['pH_Value'])
    Rainfall = float(request.form['Rainfall'])
    
    input_data = np.array([[Nitrogen, Phosphorus, Potassium, Temperature, Humidity, pH_Value, Rainfall]])
    
    input_data_scaled = scaler.transform(input_data)
    
    prediction = model.predict(input_data_scaled)
    
    crop_dict = {1: 'Rice', 2: 'Maize', 3: 'Jute', 4: 'Cotton', 5: 'Coconut', 6: 'Papaya', 7: 'Orange', 8: 'Apple', 9: 'Muskmelon', 10: 'Watermelon', 11: 'Grapes', 12: 'Mango', 13: 'Banana', 14: 'Pomegranate', 15: 'Lentil', 16: 'Blackgram', 17: 'MungBean', 18: 'MothBeans', 19: 'PigeonPeas', 20: 'KidneyBeans', 21: 'ChickPea', 22: 'Coffee'}
    
    
    if prediction[0] in crop_dict:
        crop = crop_dict[prediction[0]]
        result = "{} is the best crop to be cultivated right there".format(crop)
    else:
        result = "Sorry, we could not determine the best crop to be cultivated with the provided data."
    return render_template('index.html',result = result)
if __name__ == '__main__':
    app.run(debug=True)