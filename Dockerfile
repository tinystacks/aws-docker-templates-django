FROM python:3.6

# Create app directory
WORKDIR /

# Bundle app source
COPY . .

# Install app dependencies
RUN pip3.7 install -r requirements.txt
RUN python3 -m venv venv

RUN python manage.py migrate

# run server
EXPOSE 80
CMD python manage.py runserver 0.0.0.0:80