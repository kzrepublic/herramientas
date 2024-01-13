from requests import post as p
from requests import delete as rdel
import random, os, time, json
nw=input("Message editor? ").strip().lower() in ("1","yes","y","si","true","yed")
print(end="\x1b[H"+" "*20+"\r")
#Modifiable 
cs={"red":0xDA1012,"green":0x00FE15,"blue":0x1220EA,"black":0x000001,"darkgray":0x2F2F2F,"gray":0x5F5F5F,"lightgray":0x8F8F8F,"white":0xFFFFFE,"pink":0xFFC1E1,"purple":0xC320D1,"yellow":0xF2D80A,"orange":0xFFB420,"cyan":0x12F4C3,"darkpurple":0x800567}
#Modifiable
wcm="""
  ▄█   ▄█▄  ▄███████▄  
  ███ ▄███▀ ██▀     ▄██ 
  ███▐██▀         ▄███▀ 
 ▄█████▀     ▀█▀▄███▀▄▄ 
▀▀█████▄      ▄███▀   ▀ 
  ███▐██▄   ▄███▀       
  ███ ▀███▄ ███▄     ▄█ 
  ███   ▀█▀  ▀████████▀ 
  ▀                   
  Version: 1.1.2
  By CurZitical  """
for qw in range(0,257,2) :
    print(wcm[qw:qw+2],end='',flush=1);time.sleep(0.008)
if nw:
    print("\n\n  Message Editor Mode")
print("\n\n")
if not nw:
    def cw(z):
        if z[0:32]=="https://discord.com/api/webhooks":
            if p(z,json={"content":""}).status_code==400:
                return 1
        return 0
else:
    cw = lambda x:0
def cc(a):
    try:
        c=open(a,"r")
    except:
        return 0
    else:
        u=c.read();c.close()
        return u
if not nw:
    w=cc("./link")
    if not w :
        w=input("Enter the webhook link: ").strip()
    if not cw(w):
        print("Bad link.");exit(0)
else:
    w="Message_Editor_Mode"
eo=0
j=e={}
while 1:
    if not eo :
        u=input("> ").strip().lower()
        if u in ("bomb","send","del","flnk","clnk","chat") and nw:
            print(f"Can use {u} here");continue
        elif u=="quit":
            break
        elif u in ("help","?","ls"):
            print("Options:")
            print("help / ls / ? - This msg")
            print("name - Webhook name")
            print("msg - The message")
            print("embed - Set embed contents")
            print("data - Preview the json data")
            if not nw:
                print("send - Send the message")
                print("bomb - Send the message multiple times")
                print("del - Deletes a webhook")
                print("flnk - Save the current link on ./link")
                print("clnk - Change webhook link")
                print("chat - Send messages like a chat")
            print("cfge - Save the data in a file")
            print("cfgi - Import the data from the saved file")
            print("glnk - Get current webhook link")
            print("avatar / pfp - Picture of the webhook")
            print("quit - Exit")
        elif u=="cfge":
            json.dump(f:=open("./message.txt","w+"))
            print("Saved!")
            f.close()
        elif u=="del":
            if input("Are you sure? ").strip().lower()=="yes":
                rdel(w);os.remove("./link")
            else:
                print("Aborted")
        elif u=="glnk":
            print(w)
        elif u=="flnk":
            lk=open("./link","w");lk.write(w);lk.close();print("Saved!")
        elif u=="clnk":
            v=input("Enter the new webhook link: ").strip()
            if not cw(v):
                print("Invalid webhook.")
            if v==w:
                print("That's the same webhook.")
            w=v;lk=open("./link","w");lk.write(w);lk.close();print("Changed and saved!")
        elif u=="cfgi":
            try:
                j=json.load(f:=open("./message.txt","r"))
            except FileNotFoundError:
                print("File not found")
            except json.JSONDecodeError:
                print("Invalid File contents")
                f.close()
            else:
                if "embeds" in j:
                    e=j["embeds"][0]
                print("Imported!")
                f.close()
        elif u=="data":
            print(j)
        elif u=="chat":
            d={}
            while 1:
                d["content"]=m=input("chat> ").strip()
                if m=="exit":
                    break
                if m=="pfp":
                    d["avatar_url"]=input("Enter the avatar url: ");continue
                if m=="name":
                    d["username"]=input("Enter the username: ");continue
                r=p(w,json=d).status_code
                if r!=204:
                    print("Error: Code: ",r)
                print("Sent!")
        elif u=="send":
            r=p(w,json=j).status_code
            if r == 204:
                print("Sent!");continue
            print("Error, code:",r)
        elif u=="bomb":
            n=t=0;l=int(input("Enter limit: "));rd=input("Randomize name? [y for yes, else no] ").strip()
            while n+t<l:
                if rd in ("Y","y"):
                    j["username"]=''.join(random.choices("0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ@#$&_-()+[]{}<>",k=36))
                s=p(w,json=j).status_code
                if(s==204):
                    n+=1
                if(s==429):
                    t+=1
                print(f"Sent {n}/{l}, {t} rate limits",end='\r',flush=1)
            print("\n")
        elif u=="name":
            j["username"]=input("Enter the webhook name: ")
        elif u=="msg":
            j["content"]=input("Enter the text content: ")
        elif u in ("pfp","avatar"):
            j["avatar_url"]=input("Enter the avatar url: ")
        elif u=="embed":
            eo=1
        else:
            print(f"Invalid option {u}. Use help for options.")
        continue
    u=input("embed> ")
    if u=="help" or u=="?" or u=="ls":
        print("help / ? / ls - This msg")
        print("title - The title")
        print("desc - The description")
        print("color - The color")
        print("author - Author")
        print("footer - Footer")
        print("image / img - Image url")
        print("tbn / thumb - Thumbnail url")
        print("data - Preview the json data")
        print("cfge - Save the data in a file")
        print("cfgi - Import the data from the saved file")
        print("reset - Empty the embed data")
        print("save - Set the embed and exit")
        print("exit - Exit the embed editor without saving")
    elif u=="exit":
        eo=0;continue
    elif u=="reset":
        e={}
    elif u=="cfge":
        json.dump(e,f:=open("./embed.txt","w+"))
        print("Saved!"),f.close()
    elif u=="cfgi":
        try:
            j=json.load(f:=open("./embed.txt","r"))
        except FileNotFoundError:
            print("File not found")
        except json.JSONDecodeError:
            print("Invalid File contents")
            f.close()
        else:
            print("Imported")
            f.close()
    elif u=="title":
        e["title"]=input("Enter the title: ")
    elif u=="desc":
        e["description"]=input("Enter the description: ")
    elif u=="save":
        eo=0;j["embeds"]=[e]
        if e=={}:
            del j["embeds"]
    elif u=="data":
        print(e)
    elif u=="color":
        v=input("Enter a color: ").strip().lower()
        if v=="none":
            e["color"]="1";continue
        if v in cs:
            e["color"]=str(cs[v]);continue
        if v=="random":
            e["color"]=str(random.randint(0,16777216));continue
        if v.isnumeric():
            if int(v)>16777216:
                print("Invalid color");continue
            e["color"]=v;continue
        if v.startswith("0x") and len(v)==8:
            try:
                v=str(int(v[2:],16))
            except:
                print("Invalid color")
            else:
                e["color"]=v;continue
        print("Invalid color")
    elif u=="author":
        t={"name":input("Enter author name: ")};r=input("Enter author url ( - for none ): ")
        if r != "-" :
            t["url"]=r
        r=input("Enter author icon url ( - for none ): ")
        if r != "-" :
            t["icon_url"]=r
        e["author"]=t
    elif u=="footer":
        t={"text":input("Enter footer text: ")};r=input("Enter footer icon url ( - for none ): ")
        if r != "-" :
            t["icon_url"]=r
        e["footer"]=t
    elif u in ("img","image"):
        e["image"]={"url":input("Enter image url: ")}
    elif u in ("tbn","thumb"):
        e["thumbnail"]={"url":input("Enter image url: ")}
    else:
        print(f"Invalid option {u}. Use help for options.")