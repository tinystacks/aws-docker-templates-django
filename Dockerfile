FROM public.ecr.aws/bitnami/python:3.6
COPY --from=public.ecr.aws/m7b0o7h1/secret-env-vars-wrapper:latest-x86 /opt /opt
COPY --from=public.ecr.aws/awsguru/aws-lambda-adapter:0.3.2-x86_64 /lambda-adapter /opt/extensions/lambda-adapter

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
ENTRYPOINT ["/opt/tinystacks-secret-env-vars-wrapper", "sh", "/django.sh"]
