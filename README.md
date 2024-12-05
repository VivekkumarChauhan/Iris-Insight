# Iris Insight

**Iris Insight** is an interactive web application designed to classify iris flower species based on sepal and petal dimensions using machine learning algorithms like K-Nearest Neighbors and Logistic Regression. It provides users with an intuitive interface to input data and receive immediate classification results .

## Project Description

1. **Overview**
   - The project utilizes the famous Iris dataset to classify iris flowers into three species: Setosa, Versicolor, and Virginica.
   - It employs two machine learning models: K-Nearest Neighbors (KNN) and Logistic Regression.
   - Users can input flower measurements, and the application returns the predicted species.

2. **Technology Stack**
   - **Frontend:** HTML, CSS, JavaScript
   - **Backend:** Flask (Python)
   - **Machine Learning:** Scikit-learn
   - **Data Storage:** Pickle (for model persistence)

## Project Structure

   ```bash
  Iris-InSight/
│
├── app.py                                      # Main application file
│
├── models/                                     # Directory for saved machine learning models
│   ├── knn_model.pkl                           # KNN model
│   └── log_reg_model.pkl                       # Logistic Regression model
│
├── static/                                     # Directory for static files
│   ├── css/                                    # CSS styles for the web interface
│   │   └── style.css                           # Main stylesheet
│   │
│   └── js/                                     # JavaScript files
│       └── app.js                              # JavaScript file for API interaction
│
└── templates/                                   # Directory for HTML templates
        └── index.html                              # Main HTML file for the web interface
 ```

## Installation Guide

Follow these steps to set up the project on your local machine:

### Prerequisites

- Python 3.x installed
- Pip (Python package manager)

### Steps

1. **Clone the Repository**
   ```bash
   git clone https://github.com/yourusername/Iris-In-Sight.git
   cd Iris-In-Sight
2. **Create a Virtual Environment**
    ```bash
    python -m venv iris-env
3.**Activate the Virtual Environment**
On Windows:
  ```bash
   iris-env\Scripts\activate
 ```
On macOS/Linux:
  ```bash
    python -m venv iris-env
 ```
4.**Install Required Packages**
```bash
    pip install Flask scikit-learn flask-cors
```
  OR
```bash
  pip install -r requirements.txt
```
5.**Run the Application**
```bash
    python app.py
```
The application will start on http://127.0.0.1:5000/.


6.**Access the Web Interface Open your web browser and navigate to http://127.0.0.1:5000/. You can now input flower measurements and classify them using the KNN or Logistic Regression models.**


## Usage
1.**Enter the sepal length, sepal width, petal length, and petal width in the input fields.**
2.**Click on "Classify" to get the predicted species of the iris flower.**

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE.md) file for details.

## Contributing

We welcome contributions to enhance **SentimentInsight**! If you're interested in contributing, please follow these steps:

1. **Fork the repository**.
2. **Create a new branch**:
   ```bash
   git checkout -b feature-branch
3. **Commit your changes**:
   ```bash
   git commit -m 'Add feature'
   ```
4. **Push to the branch**:
   ```bash
    git push origin feature-branch
   ```
5. **Open a Pull Request**.
