import numpy as np
import os
from flask import Flask, request, render_template
import pickle

app = Flask(__name__)

model_path = os.path.join(os.getcwd(), 'model', 'model.pkl')

with open(model_path, 'rb') as model_file:
    model = pickle.load(model_file)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/y_predict', methods=['POST'])
def y_predict():
    year = int(request.form['year'])
    month = int(request.form['month'])
    day = int(request.form['day'])
    
    # Predict the price using the model
    prediction = model.predict([[year, month, day]])
    prediction_text = f'     Gas Price is [{prediction[0]:.2f}] Dollars'
    
    return render_template('index.html', prediction_text=prediction_text)

if __name__ == "__main__":
    app.run(debug=True)