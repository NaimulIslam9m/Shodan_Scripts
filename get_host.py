from shodan import Shodan
from subprocess import getoutput
import re

sp = '  '

def printInfo(val, ind = 0) :
    if (len(val) == 0):
        return
    if isinstance(val, dict):
        for x in val.keys():
            print(sp * ind, end = '')
            print(str(x), end = ': ')
            if isinstance(val[x], dict):
                print('{')
                printInfo(val[x], ind + 1)
                print(sp * ind + '}')
            elif isinstance(val[x], list):
                print('[')
                printInfo(val[x], ind + 1)
                print(sp * ind + ']')
            else:
                print(val[x])
    else:
        for x in val:
            print(sp * ind, end = '')
            if isinstance(x, dict):
                print('{')
                printInfo(x, ind + 1)
                print(sp * ind + '}')
            elif isinstance(x, list):
                print('[')
                printInfo(x, ind + 1)
                print(sp * ind + ']')
            else:
                print(x)

api = Shodan('UDaISuWdgnJ9eilZUT6OnHUo2nHWrj0D')

# Lookup an IP
ip = input('enter ip or domain name: ')

for x in ip:
    if x.isalpha():
        ip = getoutput('dig +short ' + ip)
        break

if ip == '':
    print('enter a valid domain name or ip')
else:
    if bool(re.match('^((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$', ip)):
        try:
            printInfo(api.host(ip))
        except:
            print('No information available for that IP.')
    else:
        print(ip)
        print('enter a valid ip')