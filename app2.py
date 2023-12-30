from flask import Flask, render_template, request, jsonify
import pickle
from model import predict_pipeline

app = Flask(__name__, template_folder='templates')

# Load the trained model
with open('trained_pipeline-0.1.0.pkl', 'rb') as model_file:
    model = pickle.load(model_file)

# Define the home route for rendering the HTML page
@app.route('/')
def home():
    return render_template("index.html")

# Define a new route for handling the prediction
@app.route('/predict', methods=['POST'])
def predict():
    result = None

    # Get JSON data from the request
    json_data = request.get_json()

    # Check if 'text_input' is in the JSON data
    if 'text_input' in json_data:
        text_input = json_data['text_input']
        # Use the trained model for prediction
        prediction = predict_pipeline(text_input)
        result = f'Predicted Language: {prediction}'
    else:
        result = 'Error: Missing "text_input" in JSON data.'

    return jsonify({'result': result})

if __name__ == '__main__':
    app.run(debug=True)
