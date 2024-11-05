FROM python:3.10

ADD app.py .

# upgrade pip before install
RUN pip install --upgrade pip

RUN pip install requests

CMD ["python", ".app.py"]