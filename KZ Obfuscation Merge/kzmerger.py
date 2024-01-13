import marshal,gzip
from base64 import b85encode as b
from _random import Random as s
from os import path as p
import sys
r=lambda:int(s().random()*255)
fcd={}
def om1(c):
    k=r()
    c=b(bytes([x^k for x in gzip.compress(marshal.dumps(c))]))
    c=f"exec(l(z(bytes([x^{k} for x in d({c})]))))"
    return c
hn=input("Enter file hub name (Nothing for stdout): ").strip()
if (not (hn=="")) and p.exists(hn):
    sys.exit("File already exists")
f={a for a in input("Files to obfuscate and merge: ").split()}
try:
    assert 0<(st:=int(input("Enter strength [0<x<=10]: ")))<=10
except ValueError:
    sys.exit("Invalid Number.")
except AssertionError:
    sys.exit("Number not in range.")
g=[*f]
for a in g:
    fc=""
    try:
        (compile(fc:=open(a,"r").read(),a,"exec")if p.isfile(a)else (f.remove(a),print(f"{a}/ is a folder!")))if p.exists(a)else (f.remove(a),print(f"File {a} wasn't found!"))
    except SyntaxError:
        print(f"SyntaxError in file {a}."),
        f.remove(a)
    except UnicodeDecodeError:
        print(f"Invalid Contents of file {a}.")
        f.remove(a)
    else:
        if fc!="":
            a=a.removesuffix(".py")
            for i in range(st):
                fc=om1(fc)
            fcd[a]=fc
g=[*f]
fc="fcd="+str(fcd)+";print('Scripts: ',*fcd.keys());az=input('What script do you want to run? ');exec(fcd[az])if az in fcd else exit('Invalid selection.')"
for i in range(st):
    fc=om1(fc)
fc="from base64 import b85decode as d;from gzip import decompress as z;from marshal import loads as l;"+fc
open(hn,"w+").write(fc) if hn else print(fc)