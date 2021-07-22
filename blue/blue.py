from bluetooth import *
import time
import json

file_path="./data.json"

while 1:
    port=1
    nearby_devices = discover_devices()
    print(nearby_devices)
    now=time.localtime()
    t=str(now.tm_mon)+'/'+str(now.tm_mday)+' '+str(now.tm_hour)+":"+str(now.tm_min)
    #for bdaddr in nearby_devices:
    #print(bdaddr,lookup_name(bdaddr))
    data={"bluetooth":nearby_devices,"time":t,"location":"403"}
    with open(file_path,'w') as outfile:
        json.dump(data,outfile)
    print(data)
