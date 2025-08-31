FROM python:3.9-slim
WORKDIR /app
COPY requirements.txt .
COPY connection.py read.py /app
RUN pip install --no-cache-dir --upgrade pip==21.1 setuptools==78.1.1 \
    && pip install --no-cache-dir -r requirements.txt
EXPOSE 5000
CMD ["python", "read.py"]
