# Dockerfile
FROM python:3.9-alpine

RUN apk add --no-cache python3 py3-pip

RUN pip3 install flask requests

COPY app.py /app.py

COPY /ssl/fullchain.pem /ssl/fullchain.pem

COPY /ssl/privkey.pem /ssl/privkey.pem

CMD ["python3", "/app.py"]
