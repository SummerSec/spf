import re

import requests
print(
"""
                                                           ,__                     ,__ 
   ____ ,   . , _ , _   , _ , _     ___  .___         __.  /  `        ____ \,___, /  `
  (     |   | |' `|' `. |' `|' `. .'   ` /   \      .'   \ |__        (     |    \ |__ 
  `--.  |   | |   |   | |   |   | |----' |   '      |    | |          `--.  |    | |   
 \___.' `._/| /   '   / /   '   / `.___, /           `._.' |         \___.' |`---' |   
                                                           /                \      /   
                                                           
 blog: https://samny.blog.csdn.net/
 github: https://github.com/SummerSec 
 usage: python3 spf.py 
 
                                                           
""")
burp0_url = "https://www.kitterman.com:443/spf/getspf3.py"
burp0_headers = {"Connection": "close", "Pragma": "no-cache", "Cache-Control": "no-cache",
                 "Upgrade-Insecure-Requests": "1",
                 "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.122 Safari/537.36",
                 "Origin": "https://www.kitterman.com", "Content-Type": "application/x-www-form-urlencoded",
                 "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
                 "Sec-Fetch-Site": "same-origin", "Sec-Fetch-Mode": "navigate", "Sec-Fetch-User": "?1",
                 "Sec-Fetch-Dest": "document", "Referer": "https://www.kitterman.com/spf/validate.html",
                 "Accept-Encoding": "gzip, deflate", "Accept-Language": "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7"}



with open(file="urls.txt", mode="r", encoding="utf-8") as f:
    domains = f.readlines()
    for do in domains:
        domain = do.strip("\n")
        # print(domain.strip("\r\n"))
        burp0_data = {"serial": "fred12", "domain": domain}
        # burp0_data = {"serial": "fred12", "domain": "58.com"}
        print("domain: " + domain + " is nslookuping")
        response = requests.post(burp0_url, headers=burp0_headers, data=burp0_data)
        flag = str(re.search(r"No valid SPF record found.", response.text))
        if flag == "None":
            print("domain: " + domain + " no vuln!")
        else:
            print("domain: " + domain + " have a spf vuln! ")
            with open(file="spfresult.txt",mode="a+",encoding="utf-8") as result:
                result.write(domain)
                result.write("\n")
                result.close()