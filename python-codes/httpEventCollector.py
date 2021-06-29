import requests

SPLUNK_URL="https://IPADDRSSS:8088/services/collector/event?token=d6c80a41-dfef-4ea0-ad23-b32ba37f271c"
chrome_data = "This is my test 3"
header_data ='{"sourcetype": "json", "event":"' + chrome_data + '", "host":"10.10.22.100"}'
print(header_data)
resp = requests.post(SPLUNK_URL, data=header_data, verify=False)
print(resp)
print(resp.status_code)
