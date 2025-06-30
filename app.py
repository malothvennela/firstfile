from flask import Flask, render_template
from sklearn.linear_model import LinearRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.datasets import make_regression, load_iris
import numpy as np

app = Flask(__name__)

# Route for the homepage
@app.route('/')
def index():
    return render_template('index.html')

# Route for running Linear Regression
@app.route('/run_linear_regression')
def run_linear_regression():
    # Generate regression data for Linear Regression
    X, y = make_regression(n_samples=100, n_features=1, noise=0.1)

    # Split into train/test sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Create and train the model
    model = LinearRegression()
    model.fit(X_train, y_train)

    # Calculate the model score (R²)
    score = model.score(X_test, y_test)

    # Return the result to be displayed on the webpage
    return f"Linear Regression Model Score (R²): {score:.2f}"

# Route for running KNN
@app.route('/run_knn')
def run_knn():
    # Load Iris dataset for KNN
    data = load_iris()
    X, y = data.data, data.target

    # Split into train/test sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

    # Create and train the KNN model
    knn = KNeighborsClassifier(n_neighbors=3)
    knn.fit(X_train, y_train)

    # Calculate the accuracy of the model
    accuracy = knn.score(X_test, y_test)

    # Return the result to be displayed on the webpage
    return f"KNN Model Accuracy: {accuracy:.2f}"

if __name__ == "__main__":
    app.run(debug=True)
