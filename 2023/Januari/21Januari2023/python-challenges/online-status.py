def onlineCount(onlineStatusMap: dict):
    online  =   0

    # items: list   =   onlineStatusMap.items()

    # for _, value in items:
    #     if value == 'offline':
    #         online += 1
    
    for value in onlineStatusMap.values():
        if value == 'online':
            online += 1

    return online
        

mapData     =   {
    'Alice' : 'online',
    'Bob' : 'offline',
    'Eve' : 'online'
}
online  =   onlineCount(mapData)
print(online)