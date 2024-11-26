FROM python:3.10

# Set working directory
WORKDIR /app

# Copy requirements and install dependencies
COPY requirements.txt .

# upgrade pip before install
# Combinging all pip command into one RUN command
RUN pip install --upgrade pip && \
    pip install -r requirements.txt

# Copy application code
COPY . .

# Run app.py
CMD ["python", "app.py"]