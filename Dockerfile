FROM python:3.10

# Set working directory
WORKDIR /app

# Copy requirements and install dependencies
COPY requirements.txt .

# upgrade pip before install
# Combinging all pip command into one RUN command
RUN pip install --upgrade pip && \
    pip install -r requirements.txt

# Set PYTHONPATH so python can find "src" directory
ENV PYTHONPATH=/app/src:$PYTHONPATH

# Copy application code
COPY . .

# Run test with pytest first, then start application if test passes
CMD ["pytest", "--maxfail=1", "--disable-warnings", "-v"] && python app.py