###########
# BUILDER # 
###########

FROM python:3.8.3-slim-buster AS builder

WORKDIR /app 

# set the environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1  

# install system dependecies.
# RUN apt update && apt install -y --no-install-recommends gcc
RUN apt update && apt install -y --no-install-recommends gcc

# lint
RUN pip install --upgrade pip 
RUN pip install flake8
COPY . /app/
RUN flake8 --ignore=E501,F401 .

# install dependecies
COPY ./requirements.txt /app/
RUN pip install -r requirements.txt
RUN pip wheel --no-cache-dir --no-deps --wheel-dir /app/wheels -r requirements.txt

###########
# FINAL #
###########

FROM python:3.8.10-slim-buster 

RUN mkdir -p /home/app 

# create the app user
RUN addgroup --system app && adduser --system --group app

# create the appropriate directories 
ENV HOME=/home/app
ENV APP_HOME=/home/app/web
RUN mkdir -p ${APP_HOME}
WORKDIR ${APP_HOME}

# install dependecies
RUN apt update && apt install -y --no-install-recommends netcat 
COPY --from=builder /app/wheels /wheels
COPY --from=builder /app/requirements.txt .
RUN pip install --upgrade pip 
RUN pip install --no-cache /wheels/*
RUN pip install psycopg2-binary 

# copy the entrypoint.prod.sh file
COPY ./entrypoint.prod.sh ${APP_HOME}

# copy the entire project
COPY . ${APP_HOME}

# chown all the files to the app user(change ownership)
RUN chown -R app:app ${APP_HOME}

# change to the app user
USER app

# run entrypoint.prod.sh 
ENTRYPOINT [ "./entrypoint.prod.sh" ]