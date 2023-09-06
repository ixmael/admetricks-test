FROM node:18-alpine

COPY ./infrastructure/docker/frontend.build.sh /frontend.build.sh
RUN chmod +x /frontend.build.sh && \
    mkdir -p /packages/frontend

WORKDIR /packages/frontend

ENTRYPOINT [ "sh" ]
CMD [ "/frontend.build.sh" ]
