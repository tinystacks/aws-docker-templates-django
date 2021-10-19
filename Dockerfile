# FROM public.ecr.aws/bitnami/python:3.6

# # Create app directory
# WORKDIR /

# # Bundle app source
# COPY . .

# # Install app dependencies
# RUN pip install -r requirements.txt

# # RUN python manage.py migrate

# # run server
# EXPOSE 80
# CMD python manage.py runserver 0.0.0.0:80

# syntax=docker/dockerfile:1
FROM python:3
ENV PYTHONUNBUFFERED=1
WORKDIR /code
COPY requirements.txt /code/
RUN pip install -r requirements.txt
COPY . /code/
