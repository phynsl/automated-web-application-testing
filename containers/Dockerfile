FROM python:3.10-slim

RUN apt-get update && apt-get install -y curl unzip

WORKDIR /app
COPY . .

RUN pip install -r requirements.txt

CMD ["pytest"]
