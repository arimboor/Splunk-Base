import requests 
import sys 
import json

def main():
    #pass
    
    #if len(sys.argv)>1 and sys.argv[1]=="--execute":
    payload = json.loads(sys.stdin.read())
        #config = paylod.get('configuration')
    #file1 = open('/opt/myfile.txt', 'a')
    #file1.write(payload)
    #file1.close()
    value1 = payload.get('result')
    with open('/opt/data.json', 'a') as f:
        json.dump(value1, f)
        f.close()
if __name__=="__main__":
    main()
