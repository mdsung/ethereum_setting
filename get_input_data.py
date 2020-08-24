from transaction.transaction import Transaction

blockchain_ip = "103.22.220.153"
hexstring = "0x46e899a7c0b31e324bff6b31def97027b431ffbbb294cca975f7c5b2230053ad"

print(Transaction.get_input_data(blockchain_ip, hexstring))
