import re
s=input()
if re.findall("^[1-9]\d*[+][1-9]\d*$",s)and len({*s.split("+")})<2:exit(print("CUTE"))
print("No Money")