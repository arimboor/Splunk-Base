import requests 
import sys 
import json

def main():
    if len(sys.argv)>1 and sys.argv[1]=="--execute":
        payload = json.loads(sys.stdin.read())
        #config = payload.get('configuration')
        #result = payload.get('result')
        #file1 = open('/opt/myfile.txt', 'a')
        #file1 = open('myfile.txt','a')
        #file1 = open('/Applications/Splunk/etc/apps/kanbanv1/bin/myfile.txt','a')
        #file1.writelines(payload)
        #file1.close()

        value1 = payload.get('result')
        with open('/Applications/Splunk/etc/apps/kanbanv1/bin/data.json', 'a') as f:
            json.dump(value1, f)
            f.close()

        value2 = payload.get('search_name')
        with open('/Applications/Splunk/etc/apps/kanbanv1/bin/config.json', 'a') as f2:
            json.dump(value2, f2)
            f2.close()

if __name__=="__main__":
    main()
