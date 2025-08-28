# create a flask app for salary prediction
# import necessary libraries
import numpy as np
from flask import Flask, request, render_template, jsonify
import pickle

# create a flask app
app = Flask(__name__)

# load the model
pipeline = pickle.load(open('salary_model.pkl', 'rb'))

# create a route for the home page
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()

    # Check required fields
    required_fields = ['age', 'education', 'experience']
    for field in required_fields:
        if field not in data:
            return jsonify({'error': f'Missing field: {field}'}), 400

    try:
        # Extract and convert input data
        age = float(data['age'])
        education = float(data['education'])
        experience = float(data['experience'])
    except ValueError:
        return jsonify({'error': 'Invalid input types. Use numbers only.'}), 400

    # Preprocess input
    input_data = np.array([[age, education, experience]])

    # Make prediction
    prediction = pipeline.predict(input_data)

    return jsonify({'predicted_salary': float(prediction[0])})
# run the app
if __name__ == '__main__':
    app.run(debug=False)




