FROM tiangolo/uvicorn-gunicorn-fastapi:python3.10

WORKDIR /posts-service

COPY requirements.txt .

RUN pip install --no-cache-dir --upgrade -r requirements.txt

COPY ./service /posts-service/service

CMD ["ls"]

CMD ["uvicorn", "service.main:app", "--host", "0.0.0.0", "--port", "80"]

