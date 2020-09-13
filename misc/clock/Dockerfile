FROM ubuntu

RUN apt-get update \
 && apt-get install -y socat python3

WORKDIR /home/pwn
COPY clock.py secret.py ./
COPY sounds ./sounds

RUN adduser --disabled-password pwn \
 && chown -R pwn:pwn /home/pwn \
 && chmod +x ./clock.py

USER pwn

ENTRYPOINT socat TCP-LISTEN:6003,nodelay,reuseaddr,fork EXEC:/home/pwn/clock.py
