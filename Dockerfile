FROM golang:1.13

WORKDIR ./devx-bingo
ADD . /devx-bingo

RUN make

ENTRYPOINT server

EXPOSE 8080


