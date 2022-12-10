FROM python:3.10.2

RUN pip install --upgrade pip
RUN pip install flask
RUN pip install numpy
RUN pip install pandas
RUN pip install selenium, chromedriver-binary==84.0.4147.30
RUN yum -y install java-1.8.0-openjdk
RUN pip install tabula-py
RUN pip install flask_cors

WORKDIR /workdir
EXPOSE 5000


