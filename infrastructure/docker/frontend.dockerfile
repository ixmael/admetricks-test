# Builder
FROM node:18-alpine as builderBase

COPY ./packages /packages
WORKDIR /packages/frontend

RUN echo "VITE_REST_API=http://localhost:9000" > .env && \
    yarn install && \
    yarn run build-only

# Production
FROM nginx:1.25.2-alpine

COPY ./infrastructure/docker/frontend.nginx.conf /etc/nginx/conf.d/default.conf
COPY --from=builderBase /packages/frontend/dist /usr/share/nginx/html
COPY --from=builderBase /packages/frontend/dist /usr/share/nginx/html/dashboard

WORKDIR /usr/share/nginx/html