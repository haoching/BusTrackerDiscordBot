path = 'temp.json'
with open(path, 'w') as f:
    json.dump(GetBusInfo('https://tdx.transportdata.tw/api/basic/v2/Rail/TRA/LiveTrainDelay?$top=30&$format=JSON'), f)
