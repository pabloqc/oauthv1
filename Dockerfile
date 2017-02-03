FROM python:3.6.0-slim

RUN mkdir -p /app
WORKDIR /app

COPY requirements.txt /app
RUN pip install --no-cache-dir -r requirements.txt

COPY . /app

CMD [ "python", "./oauthv1.py" ]
