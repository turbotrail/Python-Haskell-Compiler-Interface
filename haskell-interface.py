import os
import subprocess
cmd="ghc f.hs"
cm="f.exe"
cmc="f.txt"
f=open("f.hs","w")
lines = []
while True:
    line = input()
    if line:
        lines.append(line)
    else:
        break
text = '\n'.join(lines)
f.write(text)
f.close()
os.system(cmd)
ret=subprocess.check_output(cm)
c=open("f.txt","w")
print(ret.decode("UTF-8"))
c.write(ret.decode("UTF-8"))
c.close()
os.system(cmc)

