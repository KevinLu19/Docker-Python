FROM python:3.10

# Set working directory for pytest in /dev
WORKDIR /dev

# upgrade pip before install
# and doing a pip install on pytest.
RUN pip install --upgrade pip && \
    pip install -U pytest

COPY . /dev/

CMD ["pytest"]