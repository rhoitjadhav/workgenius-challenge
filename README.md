# WorkGenius-Challenge

## Requirements

- Python (3.8+)
- FastAPI
- Redis
- Mongodb

## Running Application

### Setting up Mandrill

1. In order to test the functionality, you will require a Mandrill account with all the setup such as Domain, API KEY,
   etc.
   Otherwise, you can use test mode on Mandrill.
2. After that, you need to add a webhook which will point to the backend application url. For testing purposes I have
   used
   ngrok for pointing the local url to the public domain as suggested in the Mailchimp docs. You could also do the same
   unless you have the public domain.
3. Once mandrill starts to send the events through webhook, the backend application will capture those events into
   database & cache memory and also send those events to the client side (index.html).

### Running Backend App

Before running the application make sure to have redis and mongodb running properly.
Without those services backend app might run into failure.

First, we need to create virtual environment and install dependencies.
After successful installation, we will run the backend application.
Following are the commands which does the same.

```commandline
virtualenv -p python3 venv
source venv/bin/activate
pip install -r requirements.txt
cd src
python main.py
```

Output:

```commandline
INFO:     Started server process [90550]
INFO:     Waiting for application startup.
Connecting to database...
Database connected!
INFO:     Application startup complete.
INFO:     Uvicorn running on http://0.0.0.0:8000 (Press CTRL+C to quit)
```

Test whether the application is started properly or not, just hit the docs API link from below and 
you should see the swagger api response on browser.

http://localhost:8000/docs

## Running Tests

```commandline
cd src
python test.py
```

## Deployment

For deployment, we first need to build docker image. After successfully building image,
we can now simply run the docker image in a container.

Docker build and run commands:

```commandline
docker build -t test/test:latest -f Dockerfile .
docker run -d --name api -p 8000:8000 test/test:latest
```

In k8s folder, there are .yaml files for deploying the application on kubernetes cluster.=