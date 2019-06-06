import json


x = {"rxInfo":{"mac":"b827ebfffe99ebfa","timestamp":2581832844,"frequency":868100000,"channel":0,"rfChain":1,"crcStatus":1,"codeRate":"4/5","rssi":-40,"loRaSNR":9,"size":17,"dataRate":{"modulation":"LORA","spreadFactor":12,"bandwidth":125},"board":0,"antenna":0},"phyPayload":"QESufgGAAAABizI7/Kupf6U="}
y =  dict(payload=x["phyPayload"])


print(y)