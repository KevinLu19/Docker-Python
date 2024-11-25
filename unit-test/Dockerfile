FROM python:3.10

# Set working directory for pytest in /dev
WORKDIR /dev

# Copy requirements and install dependencies
COPY requirements.txt .

# upgrade pip before install
# Combinging all pip command into one RUN command
RUN pip install --upgrade pip && \
    pip install -r requirements.txt

CMD ["pytest"]