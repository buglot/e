import os
import shutil
import random
class Name_Path:
    name : str
    folder : str 
    realpath :str
    OSrealpath :str
    fileNonetype : str
    def __init__(self,name,folder,p="") -> None:
        self.name = name
        self.realpath = folder+"\\"+self.name
        self.folder = folder
        self.fileNonetype = os.path.splitext(self.name)[0]
        self.realpathfileNonetype =os.path.splitext(self.realpath)[0]
count =0
pic=[]
for file in os.listdir(folder:=input("Location : ")):
    if file.endswith("jpg"):
        count+=1
        pic.append(Name_Path(file,folder))
while 1:
    try:
        s=int(input("what % :"))
        break
    except:
        print("Enter number %:25 like this")

s=count*(s/100)
new_folder =os.path.join(input("path:"))
t=0
while (t<int(s)):
    move =pic.pop(pic.index(pic[ random.randrange(0, count)]))
    t+=1
    count-=1
    shutil.move(move.realpath,new_folder)
    shutil.move(move.realpathfileNonetype+".xml",new_folder)
    
