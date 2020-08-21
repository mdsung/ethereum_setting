import time

from web3 import Web3, HTTPProvider

# import pymysql
# import pandas as pd
# import numpy as np
# import json
# import random 
# import codecs
# import datetime
# import random

numOfNodes = 3
w3_list = []
for i in range(numOfNodes+1):
    print(f"i={i}")
    w3 = Web3(HTTPProvider(f"http://127.0.0.1:{10000+i}"))
    w3_list.append(w3)
    w3.geth.miner.start(1)

while True:
    print([w.eth.getBlock('latest')['number'] for w in w3_list])
    time.sleep(5)


# conn = pymysql.connect(host="103.22.220.149", 
#                        port = 13306, 
#                        user="mindong", 
#                        passwd='yonsei2020!',  
#                        db='mimiciii', 
#                        charset='utf8', 
#                        cursorclass=pymysql.cursors.DictCursor)
# cur = conn.cursor()
# cur.execute("SHOW TABLES;")
# dfTable = pd.DataFrame(cur.fetchall())

# def ReadTable(num):
#     targetTable = dfTable.iloc[num,0]
#     cur.execute("SELECT * FROM " + targetTable + ";")
#     result = cur.fetchall()
#     return pd.DataFrame(result, index = None)

# # read ADMISSION information
# dfAdm = ReadTable(0)

# def dataframeToJsonlist(df):
#     return df.to_json(orient='records', force_ascii=False)[1:-1].replace('},{','},,{').split(',,')

# sampleIndex = np.random.choice(dfAdm["SUBJECT_ID"].unique().size, numOfNodes) ## index단계에서 random sampling 
# sampleSubjectId = list(dfAdm["SUBJECT_ID"][sampleIndex]) ## random sampling index를 통해서 subject id array 추출
# sampleSubjectId

# dfAdmSample = dfAdm[dfAdm["SUBJECT_ID"].isin(sampleSubjectId)]

# w3 = Web3(Web3.HTTPProvider("http://127.0.0.1:10000"))
# hospitalNodeAccount = w3.geth.personal.listAccounts()[0]
# print(hospitalNodeAccount)

# def mining_start(node = numOfNodes+1):
#     ## random으로 정해진 node 수만큼 추출하여 mining할 node를 임의로 정한다. 
#     miningNodeList = random.sample(range(numOfNodes+1), node)
#     ##miningNodeList = [0]
#     for i in miningNodeList:
#         print(i)
#         w3 = Web3(Web3.HTTPProvider("http://127.0.0.1:" + str(10000+i)))
#         w3.geth.miner.start(1)
#     return miningNodeList

# def mining_stop(miningNodList):
#     for i in miningNodeList:
#         w3 = Web3(Web3.HTTPProvider("http://127.0.0.1:" + str(10000+i)))
#         w3.geth.miner.stop()

# miningNodeList = mining_start()
# numOfMiningNodes = len(miningNodeList)

# ## String to Hex / Hex to string
# def stringtoHex(string):
#     return string.encode('utf-8').hex()

# def hextoString(string):
#     return bytes.fromhex(string).decode('utf-8')

# for index, row in dfAdmSample.iterrows():
#     print(index)
#     ## Prepare for the data to send
#     transactionData = row.to_json(orient='columns')
#     ## change the data to the hex code
#     transactionDataHex = stringtoHex(transactionData)
    
#     ## Get the patient node account 
#     node = sampleSubjectId.index(row["SUBJECT_ID"]) + 1
#     w3 = Web3(Web3.HTTPProvider("http://127.0.0.1:" + str(10000 + node)))
#     patientNodeAccount = w3.geth.personal.listAccounts()[0]
#     w3.geth.personal.unlockAccount(patientNodeAccount, 'password')
    
#     ## SendTransaction
#     print(patientNodeAccount, " -> ", hospitalNodeAccount)
#     ### save the start time of the transaction
#     startTime = datetime.datetime.now().timestamp()
#     transactionHash = w3.eth.sendTransaction({'to': hospitalNodeAccount, 'from': patientNodeAccount, 'value': 0, 'data' : transactionDataHex})
#     print(transactionHash)
#     ### save the end time of the transaction
#     endTime = datetime.datetime.now().timestamp()
#     transactionDict = {'from':node, 'to':0, 'startTime': startTime, 'endTime': endTime, 'transactionHash' : transactionHash.hex()}
#     transactionHistory.append(transactionDict)

#     # transactionHistory[0]['transactionHash']
# transactionOutput = pd.DataFrame(transactionHistory)
# print("===============")
# print(transactionOutput)

# mining_stop(miningNodeList)
