FROM alpine:3.19.1
ENV MYNAME=''
ENV FAVOURITE_COLOR=''
WORKDIR /app
# Something here breaks on purpose, why?
COPY .env sample.sh /app/
CMD ["/bin/sh", "/app/sample.sh"]
