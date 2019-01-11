from bank_account import Bank_Account

import sys

host = str(sys.argv[1])
sec = str(sys.argv[2])

ba = Bank_Account(host)
print(sec)
