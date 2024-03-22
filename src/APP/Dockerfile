FROM python:3.12

COPY requirements.txt .

RUN pip install -r requirements.txt

Run mkdir -p app

COPY ./App app

WORKDIR app

EXPOSE 5000

CMD ["python3", "app.py"]
