# pip install pyicloud==0.9.6.1
from pyicloud import PyiCloudService
api = PyiCloudService('put_email_here', 'put_password')
print(dir(api))
print(api.devices)
print(api.iphone.location())#640587
#for c in api.contacts.all():
#    print(c.get('firstName'), c.get('phones'))

#api.iphone.play_sound()
#print(api.files.dir())