FROM node:18.19.1-alpine

# install simple http server for serving static content
RUN npm install -g http-server

RUN mkdir -p /client
WORKDIR /client

# add `/client/node_modules/.bin` to $PATH
ENV PATH /client/node_modules/.bin:$PATH

COPY package.json /client
COPY package-lock.json /client

RUN npm install 
COPY . /client
RUN npm run build 

EXPOSE 8000

