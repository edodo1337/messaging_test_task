FROM python:3.7
ENV PYTHONUNBUFFERED=1
COPY requirements.txt /code/

WORKDIR /code
COPY requirements.txt /code/
RUN pip3 install -r /code/requirements.txt

WORKDIR /code

COPY backend /code/backend/
COPY conf /code/conf

WORKDIR /code/backend

EXPOSE 8080

CMD python manage.py runserver  