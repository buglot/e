import os
import shutil
import xml.etree.ElementTree as ET
import uuid

folder = input("folder : ")
folder_NewName = "save"
if os.path.exists(folder)!=True:
    print("ไม่เจอ folder รูปที่จะเปลี่ยนชื่อ")
else:
    for file in os.listdir(folder):
        if file.endswith(".xml"):
            name = uuid.uuid1()
            picName = file.split(".xml")[0]+".jpg"
            if os.path.exists(os.path.join(folder,picName))==False:
                print("ไม่เจอรูป",os.path.join(picName))
                continue
            xmlfile = ET.parse(os.path.join(folder,file))
            root = xmlfile.getroot()
            root.find("filename").text = f"{name}.jpg"
            path= os.path.join(folder,folder_NewName)
            if os.path.exists(path)!=True:
                os.makedirs(path)
            shutil.copy(os.path.join(folder,picName),os.path.join(path,f"{name}.jpg"))
            b_xml = ET.tostring(root)
            with open(os.path.join(path,f"{name}.xml"), "wb") as f:
                f.write(b_xml)