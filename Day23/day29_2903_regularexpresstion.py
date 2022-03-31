import re

txt = "Anjali anjali Anjali anjali Anjali anjali Anjali anjali"
x = re.search("^The.*spain$", txt)
print(x.group(0))
