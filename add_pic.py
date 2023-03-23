import albumentations as alb
import os
import xml.etree.ElementTree as ET
import cv2
import math
# albumentations setting https://albumentations.ai/docs/examples/example/
tt = alb.Compose(
                    [   
                        alb.HorizontalFlip(p=0.5), 
                        alb.RandomBrightnessContrast(p=0.3),
                        alb.RandomGamma(p=0.3), 
                        alb.RGBShift(p=0.3), 
                        alb.VerticalFlip(p=0.5),
                        alb.Rotate(border_mode=cv2.BORDER_CONSTANT,limit=180)
                    ], 
                    bbox_params=alb.BboxParams(format='pascal_voc',label_fields=['labels'],min_area=0.7)# https://albumentations.ai/docs/getting_started/bounding_boxes_augmentation/
                )
folder=input("folder : ")
count_pic=0
Error_Count=0
list_Error=[]
count=0
k="="
for x in os.listdir(folder):
        if x.endswith(".jpg"):
            count_pic+=1
b=int(input("pic add?:"))
print(f"Do you want pic from {count_pic} to {count_pic*b}? (y/n)")
if input(": ") =='y':
    print("[Processing]")
    for x in os.listdir(folder):
        bndboxs = []
        label = ""
        
        if x.endswith(".jpg"):
            filepic = os.path.join(folder,x)
            fileXML = os.path.join(folder,x.split(".jpg")[0]+".xml")

            if os.path.exists(filepic) and os.path.exists(fileXML):
                    
                #folder save
                path= os.path.join(folder,"Save")
                if os.path.exists(path)!=True:
                    os.makedirs(path)


                #read xml
                xmlfile = ET.parse(fileXML)
                root = xmlfile.getroot()
                inOject = root.find("object")
                label=inOject.find("name").text
                inBndbox = inOject.find("bndbox")
                xmin = inBndbox.find("xmin").text
                ymin = inBndbox.find("ymin").text
                xmax = inBndbox.find("xmax").text
                ymax = inBndbox.find("ymax").text
                bndboxs.append(int(xmin))
                bndboxs.append(int(ymin))
                bndboxs.append(int(xmax))
                bndboxs.append(int(ymax))

                #read image
                img = cv2.imread(filepic)
                time =1

                #run
                for r in range(b):
                    item=tt(image=img, bboxes=[bndboxs], labels=[label])

                    # new name file
                    filepic_new = x.split(".jpg")[0]+f"_{time}.jpg"
                    filexml_new = x.split(".jpg")[0]+f"_{time}.xml"

                    #change setXML
                    bnd =item["bboxes"][0]
                    inBndbox.find("xmin").text = str(int(round(bnd[0],0)))
                    inBndbox.find("ymin").text = str(int(round(bnd[1],0)))
                    inBndbox.find("xmax").text = str(int(round(bnd[2],0)))
                    inBndbox.find("ymax").text = str(int(round(bnd[3],0)))
                    inOject.find("name").text = item["labels"][0]
                    root.find("filename").text = filepic_new
                    time+=1
                        
                    #save pic and save xml
                    xml_string = ET.tostring(root)
                    with open(os.path.join(path,filexml_new), "wb") as f:
                        f.write(xml_string)
                    cv2.imwrite(os.path.join(path,filepic_new),item["image"])
                    count+=1
                    print(f"{count}/{count_pic*b} [{k*(int(math.ceil(count*100/(count_pic*b))))}] {count*100/(count_pic*b):.4f}%",end="\r")
            else:
                list_Error.append(f"[Error]:{x} [XMLnoFileexists]:{fileXML}")
                Error_Count+=1
                count_pic-=1
                print(f"{count}/{count_pic*b} [{k*(int(math.ceil(count*100/(count_pic*b))))}] {count*100/(count_pic*b):.4f}%",end="\r")
print(f"{count}/{count_pic*b} [{k*(int(math.ceil(count*100/(count_pic*b))))}] {count*100/(count_pic*b):.4f}%")
print("Error count :",Error_Count)
print(*list_Error,sep="\n")