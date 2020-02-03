#! python3
# pw.py - Ein unsicherer Passwortsafe

PASSWORDS = {'email': ' skudfheuhweiufhwiefuhwei',
             'blog': 'fhweuhksdjhfsjdfhskfhewuf',
             'luggage': '12345'}

import sys, pyperclip
if len(sys.argv) < 2:
    print('Usage: python pw.py [account] - copy account password')
    sys.exit()

account = sys.argv[1]   # Das ersre Befehlszeilenargument

if account in PASSWORDS:
    pyperclip.copy(PASSWORDS[account])
    print('Password for ' + account + ' copied to clipboard.')
else:
    print('There is no accout named ' + account)
