#Base Docker Image
FROM python:3.10

#Working directory
WORKDIR /app

#Copying requirements.txt to the docker's /app
COPY requirements.txt .


#Install requirements
RUN pip install -r requirements.txt
