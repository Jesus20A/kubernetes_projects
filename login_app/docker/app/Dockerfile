FROM python:3.10-bookworm

WORKDIR /usr/src/app

COPY ./requirements.txt ./

RUN apt update
RUN apt install -y python3-dev default-libmysqlclient-dev build-essential

RUN pip install -r requirements.txt

COPY ./src/ ./

CMD [ "python3", "app.py"]

EXPOSE 5000
