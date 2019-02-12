FROM ubuntu

RUN apt-get update \
 && apt-get install -y socat

WORKDIR /home/pwn
COPY 0v3rfl0w flag.txt ./

RUN adduser --disabled-password pwn \
 && chown -R pwn:pwn /home/pwn \
 && chmod +x ./0v3rfl0w

USER pwn

ENTRYPOINT socat TCP-LISTEN:6001,reuseaddr,fork EXEC:/home/pwn/0v3rfl0w
