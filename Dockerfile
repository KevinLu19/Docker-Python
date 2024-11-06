FROM python:3.10

COPY . .

# upgrade pip before install
RUN pip install --upgrade pip

RUN pip install requests

# Set PYTHONPATH so python can find "src" directory
ENV PYTHONPATH=/app/src:$PYTHONPATH

CMD ["python", "app.py"]