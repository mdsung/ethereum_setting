FROM ubuntu:18.04

ENV GOLANG_VERSION 1.14.7
ENV PATH /usr/lib/go-1.14/bin:$PATH

RUN apt-get update \
&& apt-get install -y \
    software-properties-common \
&& add-apt-repository ppa:longsleep/golang-backports\
&& add-apt-repository ppa:deadsnakes/ppa\
&& apt-get install -y \
    apt-utils \
    git \
    golang-1.14-go \
    python3.7\
    python3-pip\
&& rm -rf /var/lib/apt/lists/*

RUN git clone https://github.com/ethereum/go-ethereum \
&& cd go-ethereum \
&& make geth

ENV GOPATH /go
ENV PATH $GOPATH/bin:$PATH
RUN mkdir go \
&& mkdir -p "$GOPATH/src" "$GOPATH/bin" && chmod -R 777 "$GOPATH"

COPY . /network_setting
RUN pip3 install -r /network_setting/requirements.txt

ENTRYPOINT ["cd network_setting/private_network_setting/"]
CMD ["python3", "main.py"]