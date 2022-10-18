df = pd.read_csv(r'C:\Users\mains\desktop\Data.csv', low_memory=False)


count = 0

for i,j in enumerate(df["num"]):
    if j != "0":
        last_one = i

for i in range(last_one, len(df)):
    try:
      city = df.loc[i,"addr_city"].lower()
    except:
      continue
    if "orange" == city:
         name = df.loc[i,"full_name"]
         name=name.replace(" ","+")
         url1 = "https://www.google.com/search?q=" +name+"+orange+nj"
         data = '"'+df.loc[i,"full_name"]+ '" '+df.loc[i,"addr_line_1"] +  " " + df.loc[i,"addr_city"] + " " + df.loc[i,"addr_state"] 
         data = data.replace(" ","+")
         url2 = "https://www.google.com/search?q=" +data
         pattern = r"\(\d{3}\) \d{3}-\d{4}"
         textt = requests.get(url2).text 
         if "unusual traffic" in textt:
            print("shit")
            break
         #time.sleep(random.randint(3,7))
         with open(r"C:\Users\mains\Desktop\phonenumbers\searchresults_"+name +".html", "a") as f:
           f.write(textt)
         #textt +=  requests.get(url1).text
         num = re.findall(pattern, textt)
         if len(num)>0:
             df.loc[i,"num"] += str(num)
             count += 1
             print(count, i)
             
        
         

df.to_csv(r'C:\Users\mains\desktop\Data.csv',index=False)