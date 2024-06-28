FROM  python:3.8.3-slim-buster

WORKDIR /server

ENV PYTHONDONTWRITEBYTECODE 1

ENV PYTHONUNBUFFERED 1 
# install system dependecies
RUN apt update && apt install -y netcat

#install dependecies
RUN pip install --no-cache-dir --upgrade pip
COPY ./requirements.txt /server
RUN pip install -r requirements.txt  

# copy the project
COPY ./entrypoint.sh /server

COPY . /server

RUN chmod u+x ./entrypoint.sh

EXPOSE 5000
# run entrypoint.sh
ENTRYPOINT [ "./entrypoint.sh" ]