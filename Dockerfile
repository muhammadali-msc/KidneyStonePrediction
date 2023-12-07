FROM python:3.11.0-slim-buster
WORKDIR /app
ADD . /app

RUN apt update -y && apt install awscli -y

RUN pip install -r requirements.txt
CMD ["python3", "app.py"]