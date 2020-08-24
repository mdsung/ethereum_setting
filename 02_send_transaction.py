from transaction.transaction import Transaction

def main():
    blockchain_ip = "103.22.220.153"
    from_node = 1
    to_node = 0
    value = 0
    data = "TEXT"

    t1 = Transaction(blockchain_ip, from_node, to_node)
    t1.transact(value, data)

    print(t1.transaction_history)

if __name__=="__main__":
    main()