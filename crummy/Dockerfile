FROM python:alpine as builder

WORKDIR /build
COPY Pipfile Pipfile.lock ./
RUN pip install pipenv \
 && pipenv lock -r > requirements.txt

FROM python:alpine

WORKDIR /challenge
COPY --from=builder /build/requirements.txt ./
RUN pip install -r requirements.txt \
 && rm -rf /root/.cache

COPY . /challenge

ENTRYPOINT python crummy.py
