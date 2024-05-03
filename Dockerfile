FROM python:3.10.0-buster

COPY . .

RUN pip install -r requirements.txt

CMD python -m uvicorn main:app --reload --host 0.0.0.0 --port 8085
