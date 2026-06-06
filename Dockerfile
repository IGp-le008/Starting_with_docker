#Image name
FROM python:3.11

WORKDIR /app

COPY ./app .


#Command
#CMD ["python","-m","http.server","8000"]
