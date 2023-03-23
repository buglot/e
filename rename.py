import os
import uuid
count=0
for x in os.listdir(e:="unhappy"):
    count+=1
    os.rename(os.path.join(e,x),os.path.join(e,f"{e}_{count}_{uuid.uuid1()}.jpg"))