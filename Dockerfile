FROM python:3.11-slim

WORKDIR /app

COPY requirement.txt .

RUN pip install -r requirement.txt 

COPY ["predict_rain.py", "predict_rain_test.py", "rain_model.bin", "./"]

CMD ["python", "predict_rain.py"]

EXPOSE 9696