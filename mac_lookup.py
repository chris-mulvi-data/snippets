import requests
import json
import re
import sys

if sys.platform == "linux":
	import readline


def mac_lookup(mac):
	
	mac = re.sub('[^a-zA-Z0-9]', '', mac)
	url = f"https://api.maclookup.app/v2/macs/{mac.upper()}"

	response = requests.get(url)

	data = response.text
	info = json.loads(data)
	company = info.get('company')
	prefix = info.get('macPrefix')
	start = info.get('blockStart')
	end = info.get('blockEnd')
	print(f"\nSearched MAC: {mac}")
	print(f"\n{company} {prefix}\n"
		+ f"Block Start: {start}\nBlock End: {end}")

	


if __name__ == "__main__":
	mac = ""
	try:
		mac = sys.argv[1] # index 0 is the script so the args start at index 1
	except:
		mac = input('mac address: ').strip()
	mac_lookup(mac)
