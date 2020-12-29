FROM nginx:1.19.5

MAINTAINER "James Troy"

COPY nginx.conf /etc/nginx/

RUN rm /etc/nginx/conf.d/default.conf
COPY project.conf /etc/nginx/conf.d/
