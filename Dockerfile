FROM python:3.8

WORKDIR /home/sann_htet/Desktop/PythonAPIDevelopment

# Install dependencies
COPY requirements.txt ./
RUN python -m venv venv
RUN . venv/bin/activate && pip install --no-cache-dir -r requirements.txt

COPY . .

# Install uvicorn
RUN . venv/bin/activate && pip install uvicorn

CMD [ "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000" ]
