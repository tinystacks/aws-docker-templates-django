FROM public.ecr.aws/bitnami/python:3.6

# Create app directory
WORKDIR /

# Install app dependencies
COPY requirements.txt .

RUN pip install -r requirements.txt

# Bundle app source
COPY . .

# Migrate and run server
EXPOSE 8000

# Run the script
ENTRYPOINT ["sh", "/django.sh"]