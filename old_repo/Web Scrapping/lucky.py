#! python3
# lucky.py - Opens several Google search results

import requests, sys, webbrowser, bs4

print('Googleing...')
res = requests.get('http://google.com/search?q=' + ' '.join(sys.argv[1:]))
res.raise_for_status()