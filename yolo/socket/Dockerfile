FROM python:3.7-slim
RUN apt update

WORKDIR /socket
ADD ./requirements.txt /socket/requirements.txt
RUN pip install -r /socket/requirements.txt
ADD . /socket/