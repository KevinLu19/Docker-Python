FROM python:3.10

# Set working directory
WORKDIR /app

# Copy requirements and install dependencies
COPY requirements.txt .

# upgrade pip before install
# Combinging all pip command into one RUN command
RUN pip install --upgrade pip && \
    pip install -r requirements.txt && \
    pip install requests

# Set PYTHONPATH so python can find "src" directory
ENV PYTHONPATH=/app/src:$PYTHONPATH

# Copy application code
COPY . .

CMD ["python", "app.py"]