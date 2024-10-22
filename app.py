from flask import Flask, request, jsonify, render_template
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LogisticRegression
import numpy as np
import pickle

app = Flask(__name__)

# Load the Iris dataset
iris = load_iris()
X = iris.data
y = iris.target

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train the KNN classifier
knn_model = KNeighborsClassifier(n_neighbors=3)
knn_model.fit(X_train, y_train)

# Train the Logistic Regression model
log_reg_model = LogisticRegression(max_iter=200)
log_reg_model.fit(X_train, y_train)

# Save the models using pickle (optional if models already saved)
with open('models/knn_model.pkl', 'wb') as f:
    pickle.dump(knn_model, f)

with open('models/log_reg_model.pkl', 'wb') as f:
    pickle.dump(log_reg_model, f)

# Load models from saved pickle files
with open('models/knn_model.pkl', 'rb') as f:
    knn_model = pickle.load(f)

with open('models/log_reg_model.pkl', 'rb') as f:
    log_reg_model = pickle.load(f)

# Route to render the HTML page
@app.route('/')
def index():
    return render_template('index.html')

# API endpoint to classify flower using KNN model
@app.route('/predict_knn', methods=['POST'])
def predict_knn():
    data = request.json
    features = np.array([data['sepal_length'], data['sepal_width'], data['petal_length'], data['petal_width']])
    prediction = knn_model.predict([features])
    return jsonify({'species': iris.target_names[prediction][0]})

# API endpoint to classify flower using Logistic Regression model
@app.route('/predict_logistic', methods=['POST'])
def predict_logistic():
    data = request.json
    features = np.array([data['sepal_length'], data['sepal_width'], data['petal_length'], data['petal_width']])
    prediction = log_reg_model.predict([features])
    return jsonify({'species': iris.target_names[prediction][0]})

if __name__ == '__main__':
    app.run(debug=True)