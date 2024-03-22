FROM python:3.12

WORKDIR /Users/uxue/Desktop/Proyecto-ML-Obesity-Risk/src/App

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

COPY src/model/* /app/src/model/

EXPOSE 5000

CMD ["python3", "app.py"]






