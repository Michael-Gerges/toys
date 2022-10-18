import upnpy, socket, time, os
os.system("set http_proxy=")
def doit():

    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    s.connect(('10.255.255.255', 1))
    ip = s.getsockname()[0] #print(socket.gethostbyname(socket.gethostname())) #print(socket.gethostbyname("localhost"))
    
    NewExternalPort=22
    NewProtocol='TCP'
    NewInternalPort=22
    NewInternalClient=s.getsockname()[0]
    
    upnp = upnpy.UPnP()
    devices = upnp.discover()
    device = upnp.get_igd()
    service = device['WANIPConn1'] 
    service.AddPortMapping(NewExternalPort=NewExternalPort,NewProtocol=NewProtocol,NewInternalPort=NewInternalPort,NewInternalClient=NewInternalClient, NewRemoteHost="", NewEnabled=1, NewPortMappingDescription="", NewLeaseDuration=0)
    b = service.GetSpecificPortMappingEntry(NewRemoteHost="",NewExternalPort=NewExternalPort,NewProtocol=NewProtocol)["NewInternalClient"]
    assert b == ip
    a = service.GetExternalIPAddress()["NewExternalIPAddress"]
    url = a + ":"+ str(NewExternalPort) 
    url2 = b + ":"+  str(NewInternalPort)
    return (url +" to "+ url2)

    

a = False
while not a:
    a = doit()


print(a)
os.system("pause")