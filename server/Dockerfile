FROM python:3.8

# 2
RUN pip install -r requirements.txt

# 3
COPY . /app
WORKDIR /app

# 4
ENV PORT 8080

# 5
CMD exec gunicorn --bind :$PORT --workers 1 --threads 8 app:app