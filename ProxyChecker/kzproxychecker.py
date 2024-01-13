from threading import Thread as T;from requests import Session as s;from sys import exit
try:
    l=open(input("Enter proxy list file: ").strip()).read().split("\n");ts=int(input("How .any threads? "));se=input("Show errors? ").lower()=="yes"
except:
    exit("Something went wrong.")
def sir(l,s,se):
    for i in l:
        try:
            s.get("https://api.ipify.org/",proxies={"http":i,"https":i},timeout=5)
        except BaseException as e:
            if se:
                print(type(e).__name__,i)
        else:
            print(i)
a=int(len(l)/ts+1);s=s()
for i in range(0,len(l)+a,a):
    T(target=sir,args=(l[i:i+a],s,se)).start()