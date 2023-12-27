FROM python:latest

WORKDIR /home/sann_htet/Desktop/PythonAPIDevelopment

# Install dependencies
COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]