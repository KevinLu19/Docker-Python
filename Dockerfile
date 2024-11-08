FROM python:3.10

# Set working directory
WORKDIR /app

# Copy requirements and install dependencies
COPY requirements.txt .

# upgrade pip before install
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
RUN pip install requests

# Set PYTHONPATH so python can find "src" directory
ENV PYTHONPATH=/app/src:$PYTHONPATH

# Copy application code
COPY . .

CMD ["python", "app.py"]