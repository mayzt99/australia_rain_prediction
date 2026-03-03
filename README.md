# Australia Rain Prediction

A machine learning project that predicts whether it will rain the next day in Australia based on weather observations. The trained model is served as a REST API using Flask and containerized using Docker.

## Project Structure

- `australia-rain-prediction.ipynb`: Jupyter Notebook containing the data exploration, preprocessing, model training, and exporting the model pipeline.
- `rain_model.bin`: The serialized (pickled) model, containing the `DictVectorizer`, `StandardScaler`, and the trained machine learning model.
- `predict_rain.py`: A Flask web service that exposes a `/predict_rain` endpoint to serve predictions using the trained model.
- `predict_rain_test.py`: A test script that sends a sample POST request to the Flask API to verify it's working properly.
- `requirement.txt`: Python package dependencies (`flask`, `scikit-learn`).
- `Dockerfile`: Instructions for containerizing the Flask application using Docker.

## Running the Application Locally

1. **Install dependencies:**
   Make sure you have Python installed. Install the required packages using pip:
   ```bash
   pip install -r requirement.txt
   ```

2. **Run the Flask app:**
   Start the application by running:
   ```bash
   python predict_rain.py
   ```
   The Flask server will start and listen on `http://0.0.0.0:9696`.

3. **Test the prediction endpoint:**
   Open a separate terminal and run the test script:
   ```bash
   python predict_rain_test.py
   ```
   You should receive a JSON response with the rain probability and boolean prediction, for example:
   ```json
   {"rain": true, "rain_probability": 0.58}
   ```

## Running the Application with Docker

1. **Build the Docker image:**
   From the project directory, run:
   ```bash
   docker build -t rain-prediction-app .
   ```

2. **Run the Docker container:**
   Start a container from the built image, mapping port 9696 to your host machine:
   ```bash
   docker run -it -p 9696:9696 rain-prediction-app
   ```

3. **Test the containerized endpoint:**
   Similarly, run the test script in a separate terminal:
   ```bash
   python predict_rain_test.py
   ```
