import marshal,gzip
from base64 import b85encode as b
from _random import Random as s
r=lambda:int(s().random()*255)
def om1(c):
    k=r()
    c=b(bytes([x^k for x in gzip.compress(marshal.dumps(c))]))
    c=f"exec(l(z(bytes([x^{k} for x in d({c})]))))"
    return c
try:
    f=open(fn:=input("Python file to obfuscate: "),"r")
    c,_=f.read(),f.close()
except:
    exit(print("Invalid file.") or 1)
x=input("How Many rounds: ")
try:
    x=int(x)
except:
    exit(print("Not a number."))
for p in range(x):
    print(f"Round {p}/{x}",end='\r')
    c=om1(c)
f=open(fn[:-3]+"_ofs.py","w")
f.write("from base64 import b85decode as d;from gzip import decompress as z;from marshal import loads as l;"+c)
f.close()