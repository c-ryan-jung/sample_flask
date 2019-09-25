FROM ubuntu:latest
FROM golang:latest
MAINTAINER Ryan Jung "cj9de@virginia.edu""
RUN apt-get update -y
RUN apt-get install -y python-pip python-dev build-essential
COPY . /flask_app
WORKDIR /flask_app
RUN pip install -r requirements.txt
ENTRYPOINT ["python"]
EXPOSE 5000
CMD ["server.py"]