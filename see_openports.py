import os, subprocess

#os.system(r'netsh advfirewall firewall add rule name="Michael666" dir=in action=allow protocol=TCP')
os.system(r"netsh advfirewall firewall show rule name=all > c:\users\micha\OneDrive\desktop\t.txt")
#os.system(r'netsh advfirewall firewall delete rule name="Michael666"')
with open(r"c:\users\micha\OneDrive\desktop\t.txt" , "r") as f:
    a = f.readlines()


command = r"netsh advfirewall firewall show rule name=all"
info = subprocess.run(command, stdout=subprocess.PIPE).stdout.decode('utf-8')
info = info.split("Rule Name:                            ")[1:]


with open(r"c:\users\micha\OneDrive\desktop\t.txt" , "a") as f:
  for i in info:
    lstt = i.split("\n")
    rulename = lstt[0].replace("\r","")
    for j in lstt:
        if "Port:" in j and not "Any" in j:
            f.write(str(rulename + "\n" + str(j)))


