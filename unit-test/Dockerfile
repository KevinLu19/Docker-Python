FROM python:3.10

# Set working directory for pytest in /dev
WORKDIR /app

# upgrade pip before install
# and doing a pip install on pytest.
RUN pip install --upgrade pip && \
    pip install -U pytest && \
    pip install requests

COPY . /app/

CMD ["pytest", "unit-test", "-s", "--maxfail=1", "--disable-warnings"]