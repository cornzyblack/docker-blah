FROM alpine:3.19.1
ENV MYNAME='Eni'
ENV FAVOURITE_COLOR='Blue'
WORKDIR /app
# Something here breaks on purpose, why?
COPY sample.sh /app/
CMD ["/bin/sh", "/app/sample.sh"]
