import os
import xml.etree.ElementTree as ET
labels ={} # ตัวอย่าง labels = {1:"face"} 1คือไอดี
accuracy = 0
data={}
pre_ture={}
worng={}
per=0.8 
for file in os.listdir(folder:="\\"):
    if file.endswith(".xml"):
        xmlfile = ET.parse(os.path.join(folder,file))
        root = xmlfile.getroot()
        file_pic= root.find("filename").text
        for x in root.findall("object"):
           label= x.find("name").text
           if label not in data.keys():
               data.update({label:0})
               worng.update({label:0})
               pre_ture.update({label:0})
           else:
               data[label]+=1
