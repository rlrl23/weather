FROM python:3.10.12-alpine
WORKDIR /app
COPY ./requirements.txt /code/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY . .
CMD ["fastapi", "run", "main.py"," --proxy-headers", "--port", "80"]
