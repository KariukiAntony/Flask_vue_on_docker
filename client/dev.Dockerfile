FROM node:18.19.1-alpine

RUN mkdir -p /client
WORKDIR /client

# add `/client/node_modules/.bin` to $PATH
ENV PATH /client/node_modules/.bin:$PATH

COPY package.json /client
COPY package-lock.json /client

RUN npm install 
COPY . /client 

EXPOSE 5173

