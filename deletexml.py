import os
import sys
for x in os.listdir(sys.argv[1]):
    if x.endswith(".xml"):
        if x.endswith(".xml"):
            a=os.path.join(sys.argv[1],x)
            os.system(f"del \"{a}\"")