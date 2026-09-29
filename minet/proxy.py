import requests


def getproxy():
    list = str('proxy.txt')
    rsp = requests.get('https://api.proxyscrape.com/?request=getproxies&proxytype=http&timeout=10000&country=all&ssl=all&anonymity=all')
    with open(str(list),'wb') as fp:
        fp.write(rsp.content)
    pprr = open(list).readlines()


if __name__ == '__main__':
    getproxy()
print("RESET : PROXYCOMPLETE!!")
