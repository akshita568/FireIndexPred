import pickle
from flask import Flask, render_template,request, jsonify
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler



application = Flask(__name__)
app=application

# import ridge regressor and standardscaler pickle
ridge_model=pickle.load(open('models/ridge.pkl','rb'))
standard_scaler=pickle.load(open('models/scaler.pkl','rb'))


@app.route("/")
def index():
    return render_template("index.html")

@app.route('/predictdata', methods=['GET','POST'])
def predict_datapoint():
    if request.method == "POST":
        # 1. Extract data from form matching your HTML'name' attributes
        input_data = [
            float(request.form.get('Temperature')),
            float(request.form.get('RH')),
            float(request.form.get('Ws')),
            float(request.form.get('Rain')),
            float(request.form.get('FFMC')),
            float(request.form.get('DMC')),
            float(request.form.get('ISI')),
            float(request.form.get('Classes')),
            float(request.form.get('Region'))
        ]
        
        # 2. Scale the input data using loaded scaler
        new_data_scaled = standard_scaler.transform([input_data])
        
        # 3. Predict using loaded Ridge model
        prediction = ridge_model.predict(new_data_scaled)
        result = round(prediction[0], 2)
        
        # 4. Render the dedicated result.html page with the score
        return render_template('result.html', final_result=result)
    else:
        return render_template('home.html')

if __name__ == "__main__":
    app.run(debug=True)