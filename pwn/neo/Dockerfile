FROM ubuntu

RUN apt-get update \
 && apt-get install -y socat

WORKDIR /home/pwn
COPY neo flag.txt ./

RUN adduser --disabled-password pwn \
 && chown -R pwn:pwn /home/pwn \
 && chmod +x ./neo

USER pwn

ENTRYPOINT socat TCP-LISTEN:6003,reuseaddr,fork EXEC:/home/pwn/0v3rfl0w
