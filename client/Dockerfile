FROM node:18.19.1-alpine

# install simple http server for serving static content
RUN npm install -g http-server

RUN mkdir -p /app
WORKDIR /app

# add `/app/node_modules/.bin` to $PATH
ENV PATH /app/node_modules/.bin:$PATH

COPY package.json /app
COPY package-lock.json /app

RUN npm install 
COPY . /app
RUN npm run build 

EXPOSE 8000

