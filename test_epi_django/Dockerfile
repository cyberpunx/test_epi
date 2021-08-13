# INSTALL PYTHON IMAGE
FROM python:3.6
ENV PYTHONUNBUFFERED=1

# INSTALL TOOLS
RUN apt-get update \
    && apt-get -y install unzip \
    && apt-get -y install libaio-dev \
    && mkdir -p /opt/data/api

WORKDIR /opt/data
ADD ./oracle-instantclient/ /opt/data
ADD ./install-instantclient.sh /opt/data
ADD ./requirements.txt /opt/data

ENV ORACLE_HOME=/opt/oracle/instantclient
ENV LD_LIBRARY_PATH=$LD_LIBRARY_PATH:$ORACLE_HOME
ENV OCI_HOME=/opt/oracle/instantclient
ENV OCI_LIB_DIR=/opt/oracle/instantclient
ENV OCI_INCLUDE_DIR=/opt/oracle/instantclient/sdk/include

RUN chmod +x install-instantclient.sh
RUN /bin/sh ./install-instantclient.sh
RUN pip install -r requirements.txt

WORKDIR /code
COPY scripts/start.sh /
COPY . /code/

RUN chmod +x scripts/start.sh

