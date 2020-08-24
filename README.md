# Ethereum Setting(Python 3.6.8)
> Set the private network with python

In order to simulate Ethereum data transaction, set the private ethereum network with python

## Prerequisite
    * python 3.6
    * go 1.14
    * GETH 1.9

## Installation

OS X & Linux:

```sh
pip install -r requirements.txt
```

## Example
### Docker file build
```sh
docker build . -t mdsung/ubuntu_geth
```

### Docker compose 
You can set the number of node in the docker with modifying docker-compose file
```sh
docker-compose up -d
```

### Send Transaction Example
02_send_transaction.py

### Get Transaction data Example
01_get_input_data.py

## Release History

* 0.0.1
    * Run the Private Network 
* 0.1
   * Run the Private Network on Docker
   * Send Transaction and Get Transaction data 
   
## Meta
MinDong Sung – sungmindong@gmail.com

[https://github.com/mdsung/ethereum_setting
](https://github.com/mdsung/ethereum_setting
)

