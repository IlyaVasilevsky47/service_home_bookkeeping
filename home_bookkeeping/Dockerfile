FROM python:3.8-slim
WORKDIR /app
COPY . .
COPY requirements.txt .
RUN pip3 install -r requirements.txt --no-cache-dir
COPY static/ ./static/
CMD ["gunicorn", "home_bookkeeping.wsgi:application", "--bind", "0:8000"]