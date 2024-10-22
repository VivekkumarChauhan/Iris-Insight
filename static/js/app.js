function classifyFlower() {
    const sepalLength = document.getElementById('sepal_length').value;
    const sepalWidth = document.getElementById('sepal_width').value;
    const petalLength = document.getElementById('petal_length').value;
    const petalWidth = document.getElementById('petal_width').value;

    const data = {
        sepal_length: parseFloat(sepalLength),
        sepal_width: parseFloat(sepalWidth),
        petal_length: parseFloat(petalLength),
        petal_width: parseFloat(petalWidth)
    };

    // Call KNN model
    fetch('/predict_knn', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(data)
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('result').innerHTML = `KNN Prediction: ${data.species}`;
    })
    .catch(error => {
        console.error('Error:', error);
        document.getElementById('result').innerHTML = 'Error predicting with KNN.';
    });

    // Call Logistic Regression model
    fetch('/predict_logistic', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(data)
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('result').innerHTML += `<br>Logistic Regression Prediction: ${data.species}`;
    })
    .catch(error => {
        console.error('Error:', error);
        document.getElementById('result').innerHTML += '<br>Error predicting with Logistic Regression.';
    });
}
