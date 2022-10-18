
# activate grand theft auto VR
import os 
import shutil

d = r"C:\Program Files (x86)\Steam\steamapps\common\Grand Theft Auto V"

lst = ["d3d11.dll"]
lst.append("d3dx.ini")
lst.append("dinput8.dll")
lst.append("nvapi64.dll")
lst.append("openvr_api.dll")
lst.append("RealVR.ini")

if not os.path.exists(os.path.join(d, "michaelvr")):
    os.mkdir(os.path.join(d, "michaelvr"))



for i in lst:
    old = str(os.path.join(d,i))
    new = os.path.join(d, "michaelvr",i)
    shutil.move(old, new)



