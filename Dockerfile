FROM python:3.9-alpine
# alpine은 파이썬의 minimal한 light 버전이므로 빌드가 더 빠를 수 있다. 

ENV PYTHONUNBUFFERED 1

#OUTPUT을 버퍼하지 않는다
#파이썬을 도커로 실행할 때 추천되는 방식
#이유: 뭔가 복잡해지나봄

COPY ./requirements.txt /requirements.txt

RUN pip install -r /requirements.txt

RUN mkdir /app
WORKDIR /app
COPY ./app /app 
# 복사하려는 디렉토리가 없으면 에러가 난다. 

RUN adduser -D app
# 이 유저는 -D 옵션에 의해 로그인하는 용이 아니라서 홈디렉토리가 없고 오직 프로젝트를 실행하는데만 사용된다.
# 침입자가 루트 계정으로 다 할 수 없게끔 하는 보안 목적
USER app
