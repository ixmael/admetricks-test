# Build
FROM node:18-alpine as buildBase

COPY ./packages /packages
WORKDIR /packages/frontend

RUN echo "VITE_REST_API=http://localhost:9000" > .env && \
    yarn install \
    && yarn run build

# Production
FROM nginx:1.25.2-alpine

COPY --from=buildBase /packages/frontend/dist /usr/share/nginx/html
COPY ./infrastructure/docker/frontend.nginx.conf /etc/nginx/conf.d/default.conf

# RUN mkdir /usr/share/nginx/html/dashboard && \
#cp /usr/share/nginx/html/index.html /usr/share/nginx/html/dashboard

WORKDIR /usr/share/nginx/html
