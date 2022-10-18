# netstat -boan >> "C:\Users\micha\OneDrive\Desktop\t.txt"

with open(r"C:\Users\micha\OneDrive\Desktop\t.txt", "r") as f:
    a = f.readlines()

cleaner_a = []
for i in range(len(a)):
    cleaner_a.append(a[i].replace("\n",""))


cleaner_a = cleaner_a[4:]
longs = []

for i in range(len(cleaner_a)):
    if (len(cleaner_a[i]) > 70):
        longs.append(cleaner_a[i])
    else:
        longs[-1] += cleaner_a[i]


goodones = ["any","team", "svchost", "chrome", "sql", "mms", "prime","443", "lsass" , "445", "4 can", "edge", "dash", "spoolsv", "java", "wrapper", "python" , "code"]
del_ones = []

for dell in goodones:
    for i, entry in enumerate(longs):
        if dell  in entry.lower():
            #print(i, entry)
            del_ones.append(entry)


for i in del_ones:
    try:
             longs.remove(i)
    except:
        continue


for i in longs:
    print(i)