import requests


url = "https://discord.com/api/v9/users/@me"

user = str(input('username: '))
h = {"Accept":"*/*",
     "Accept-Encoding":"gzip, deflate, br",
     "Accept-Language":"en-US,en;q=0.9,ar;q=0.8",
     "Authorization":"NzM0NTM0OTY0NjYxNDUyOTA3.GdihFh.1S3ziTKqv_ErM62hN5qNucX03BacU8alyNmCJ0",
     "Content-Length":"41",
     "Content-Type":"application/json",
     "Cookie":"__dcfduid=cf576c80336511ed920e3f458d8db9d4; __sdcfduid=cf576c81336511ed920e3f458d8db9d445af67e5e809f3f17ebcad3cf9d3d3295abc987db2fd05b8c5acae99c5a09236; __cfruid=3b373d08ccc8b4b0aee48e4ddb21f74deb121cc3-1686869007; __cf_bm=c_5Oq8QapcwyhufUluMCJs10_xht0MBw5RraB7PWt.g-1686996222-0-Ac1pS6cg19vD7+or0rtLr4QP5ERuQON1yKWxAoBw/gyXqVsc809YpBd5jI03r6WbWQ==",
     "Origin":"https://discord.com",
     "Referer":"https://discord.com/channels/@me",
     "Sec-Ch-Ua":'"Not.A/Brand";v="8", "Chromium";v="114", "Google Chrome";v="114"',
     "Sec-Ch-Ua-Mobile":"?0",
     "Sec-Ch-Ua-Platform":'"Windows"',
     "Sec-Fetch-Dest":"empty",
     "Sec-Fetch-Mode":"cors",
     "Sec-Fetch-Site":"same-origin",
     "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36",
     "X-Debug-Options":"bugReporterEnabled",
     "X-Discord-Locale":"en-US",
     "X-Discord-Timezone":"Asia/Riyadh",
     "X-Super-Properties":"eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiQ2hyb21lIiwiZGV2aWNlIjoiIiwic3lzdGVtX2xvY2FsZSI6ImVuLVVTIiwiYnJvd3Nlcl91c2VyX2FnZW50IjoiTW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzExNC4wLjAuMCBTYWZhcmkvNTM3LjM2IiwiYnJvd3Nlcl92ZXJzaW9uIjoiMTE0LjAuMC4wIiwib3NfdmVyc2lvbiI6IjEwIiwicmVmZXJyZXIiOiIiLCJyZWZlcnJpbmdfZG9tYWluIjoiIiwicmVmZXJyZXJfY3VycmVudCI6IiIsInJlZmVycmluZ19kb21haW5fY3VycmVudCI6IiIsInJlbGVhc2VfY2hhbm5lbCI6InN0YWJsZSIsImNsaWVudF9idWlsZF9udW1iZXIiOjIwNjU3NiwiY2xpZW50X2V2ZW50X3NvdXJjZSI6bnVsbH0="
    }

data = {
    "password": '"Aq12aq12"',
    "username": user
}

r = requests.get(url=url,headers=h , data=data)
