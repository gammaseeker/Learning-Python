#!/usr/bin/python3
#password_locker.py - an insecure pw locker program
import sys, pyperclip

PASSWORDS = {'email': 'cat', 'blog': 'dog', 'luggage': '12345'}

if len(sys.argv) < 2: 
    print('Usage: python password_locker.py [account] - copy account password')
    sys.exit()

account = sys.argv[1]  #1st cmd line arg
if account in PASSWORDS: # looks in pw to see if acct exists
    pyperclip.copy(PASSWORDS[account]) # if exists, copy pw to clipboard
    print('Password for ' + account + ' compied to clipboard.')
else:
    print('There is no account named ' + account)
