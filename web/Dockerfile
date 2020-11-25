FROM python:3.7-stretch
RUN apt-get update -y
RUN apt-get install -y python-pip python-dev build-essential
COPY . /web/src
WORKDIR /web/src
RUN pip install -r requirements.txt
ENTRYPOINT ["python"]
CMD ["app.py"]
