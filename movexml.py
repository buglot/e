import os
import shutil
import sys
argv = sys.argv
folderold = argv[1]
folderNew = argv[2]
c = argv[3]

for x in os.listdir(folderold):
    if x.endswith(".xml"):
        xx=x.split(".xml")[0]
        xx+=".jpg"

        a=os.path.join(folderNew,x)
        b=os.path.join(folderNew,xx)
        try:
            if c=="copy":
                shutil.copy(os.path.join(folderold,x),a)
                shutil.copy(os.path.join(folderold,xx),b)
            elif c=="cut":
                shutil.move(os.path.join(folderold,x),a)
                shutil.move(os.path.join(folderold,xx),b)
        except Exception as e:
                print(e)
                a=input()

    