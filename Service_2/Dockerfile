FROM python:3.6.8

RUN apt update
RUN apt install python3 -y
RUN apt install python3-pip -y

WORKDIR /opt/service_2

COPY . ${WORKDIR}

RUN pip3 install -r requirements.txt

EXPOSE 5001

ENTRYPOINT ["/usr/local/bin/python", "app.py"]