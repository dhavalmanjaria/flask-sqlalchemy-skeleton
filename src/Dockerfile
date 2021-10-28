FROM python:3.8

COPY . /app

WORKDIR /app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN pip install -r requirements.txt

CMD ["gunicorn", "-c", "gunicorn-config.py", "wsgi:app"]