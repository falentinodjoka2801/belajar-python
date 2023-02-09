def online_status(statusesData: dict):
    onlineCount =   0
    
    for _, personOnlineStatus in statusesData.items():
        if personOnlineStatus == 'online':
            onlineCount +=  1
    return onlineCount


onlineStatus    =   {
    'Falentino' :   'online',
    'Andrian'   :   'online',
    'Mega'      :   'online'
}
onlineCount =   online_status(onlineStatus)
print(onlineCount)