FROM python:3.11-slim-buster

COPY main.py /main.py

CMD ["python", "main.py"]