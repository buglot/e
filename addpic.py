import albumentations as a
import cv2 
import os
transform = a.Compose([
    a.HorizontalFlip(p=0.5),
    a.RandomBrightnessContrast(p=0.3),
    a.VerticalFlip(p=0.5),
    a.Rotate(border_mode=cv2.BORDER_CONSTANT,crop_border=True)
])
a=input("f:")
b=input("d:")
timeb=input("time:")
count=0
t=len(os.listdir(a))
for filenames in os.listdir(a):
    image  = cv2.imread(filename=os.path.join(a,filenames))
    k=0
    count+=1
    try:
        for x in range(int(timeb)):
            e=transform(image=image)['image']
            cv2.imwrite(os.path.join(b,filenames.split(".jpg")[0]+f"-{k}.jpg"),e)
            k+=1
    except:
        print(f"Error{t}/{count}")
    

    print(f"{t}/{count} {count*100/t:.2f}%")