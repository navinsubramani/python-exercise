# Write a program that computes the net amount of a bank account based a transaction log from console input. The transaction log format is shown as following:

# D 100
# W 200
# D means deposit while W means withdrawal.
# Suppose the following input is supplied to the program:

# D 300
# D 300
# W 200
# D 100
# Then, the output should be:

# 500

Balance = 0

while True:
    transaction = input("What is the transaction: ")
    if transaction[0:2] == "D ":
        Balance += int(transaction.split("D ")[1])
    elif transaction[0:2] == "W ":
        Balance -= int(transaction.split("W ")[1])
    else:
        break

print(Balance)
