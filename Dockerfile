from python:3.8-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt --no-cache-dir
COPY app.py .
EXPOSE 5000
CMD ["python", "app.py"]