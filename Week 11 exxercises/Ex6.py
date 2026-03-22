def perform_atomic_transfer(accounts, sender, receiver, amount):
    # The Data: accounts is a dictionary: {"UserA": 100.0, "UserB": 50.0}.
    if sender not in accounts:
        raise KeyError("Sender not found")
    if accounts[sender] < amount:
         raise ValueError ("Insufficient funds")
    accounts[sender] -= amount
    try:
        accounts[receiver] += amount
    except KeyError:
        accounts[receiver] += amount
        print(f"Reciever not found. Refunding {sender} ...")
        raise
    return True

bank_db = {"Alice": 100.0, "Bob": 50.0}