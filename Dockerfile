FROM python:3.8.10

# Exposing port
EXPOSE 8000

# Environment Variables
ENV REDIS_HOST "localhost"
ENV REDIS_PORT 6379
ENV MONGO_HOST "localhost"
ENV MONGO_PORT 27017
ENV MANDRILL_API_KEY "api-key"

# Copying source code
COPY ./requirements.txt /workgenius-challenge/
COPY ./src/ /workgenius-challenge/src

# Installing dependencies
RUN pip install -r /workgenius-challenge/requirements.txt

# Setting working directory
WORKDIR /workgenius-challenge/src

# Running application
CMD ["python", "main.py"]