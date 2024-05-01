# build environment
FROM node:18.19.1-alpine as build

RUN mkdir /app

WORKDIR /app

ENV PATH /app/node_modules/.bin:$PATH

COPY package.json /app

COPY package-lock.json /app

RUN npm install --silent

COPY . /app

RUN npm run build

# production environment
FROM nginx:1.26.0-alpine as production

COPY --from=build /app/dist /usr/share/nginx/html

# RUN rm /etc/nginx/conf.d/default.conf

EXPOSE 80 

CMD ["nginx", "-g", "daemon off;"]