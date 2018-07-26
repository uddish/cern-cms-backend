FROM cern/cc7-base

# Install required packages
RUN yum -y install \
        bzip2 \
        gcc \
        gcc-c++ \
        git \
        kernel-devel \
        libcurl-openssl-devel \
        libffi-devel \
        ncurses-devel \
        nano \
        nodejs \
        npm \
        pandoc \
        patch \
        sqlite-devel \
        tar \
        make \
        openssl-devel \
        unzip \
        wget \
        which \
        zeromq3-devel \
        zlib-devel && \
    yum clean all && \
    rm -rf /var/cache/yum

# Install Python 3
RUN mkdir /tmp/pytmp && \
    cd /tmp/pytmp && \
    wget https://www.python.org/ftp/python/3.6.1/Python-3.6.1.tgz && \
    tar xzvf Python-3.6.1.tgz && \
    cd /tmp/pytmp/Python-3.6.1 && \
    ./configure --enable-shared && \
    make install && \
    rm -rf /tmp/pytmp

# Install Oracle Instant client - https://github.com/oracle/docker-images/tree/master/OracleInstantClient

ADD oracle-instantclient12.2-basic-12.2.0.1.0-1.x86_64.rpm /tmp
RUN  yum -y install /tmp/oracle-instantclient*.rpm && \
     rm -rf /var/cache/yum && \
     rm -f /tmp/oracle-instantclient*.rpm && \
     echo /usr/lib/oracle/12.2/client64/lib > /etc/ld.so.conf.d/oracle-instantclient12.2.conf && \
     ldconfig

ENV PATH=$PATH:/usr/lib/oracle/12.2/client64/bin
ENV PYTHONUNBUFFERED 1

ENV LD_LIBRARY_PATH /usr/local/lib/
RUN echo "LD_LIBRARY_PATH=$LD_LIBRARY_PATH" >> /etc/environment

# Application packages
RUN mkdir /code
WORKDIR /code
ADD . /code/
RUN pip3 install -r requirements.txt

EXPOSE 8000
CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]