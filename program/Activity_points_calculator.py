import cv2
import glob
import pytesseract
import pandas as pd
def ocr_core(img):
    text = pytesseract.image_to_string(img)
    return text
path=glob.glob('images/*.jpg')
names={'jeomol jhon':1,'jose ben':2,'joyal johnson':3,'k s gopi krishnan':4,'k s sooraj':5,'karina p joshi':6,'keerthana jayakumar':7,'krishna priya p':8,'malavika m nair':10,'manal zubair':11,'manu mahendran':12,'mareena benny':13,'mirzad m nellickal':14,'muhammed sadhath v h':15,'muskan m a':16,'namitha jason':17,'nanda p':18,'nandana p':18,'navaz p zakkaria':20}
b={'workshop ':5,'webinar ':5,'intership ':40,'course ':10,'seminar ':5,'lecture ':5,"project":10,'event ':5,'talk':5}
nits=['national institute of science and technology','nitk','nitc','nitd']
iits=['indian institute of science and technology','iitb','iitm','iitk','iitd','iitpkd','iit goa']
e=[]
z=[]
for file in path:
    img=cv2.imread(file)
    text=ocr_core(img)
    text=text.lower()
    lists=[]
    for i in names.keys():
        if i in text:
            lists.append(names[i])
            lists.append(i)
    for j in b.keys():
        if j in text:
            lists.append(j)
            lists.append(b[j])
            break
    for k in nits:
        if k in text:
            lists[-1]+=5
    for l in iits:
        if l in text:
            if 'nptel' in text:
                lists[-1]=50
            else:
                lists[-1]+=10
    if len(lists)==4:
        e.append(lists)
    else:
        z.append(file[32:])
print(e)
# ab=[]
# ab.extend(e)
# ad=[]
# for i in b.keys():
#     ac=[]
#     ac.append(i)
#     for j in range(0,len(ab)):
#         if i==ab[j][2]:
#             af=[ab[j][0],ab[j][1],ab[j][3],0]
#             ac.append(af)
#     if len(ac)>1:
#         ad.append(ac)
# print(ad)




# for i in range (0,len(e)):
#     for j in range(len(e)-1,i,-1):
#         if ab[i][2]==ab[j][2]:


bc=[]
bc.append(e)


# for i in range(0,len(e)):
#     for j in range(len(e)-1,i,-1):
#         if e[i][0]==e[j][0]:
#             e[i][3]+=e[j][3]
#             e.pop(j)
print(e)
a={}
p=[]
q=[]
s=[]
r=[]
for i in range(0,len(e)):
    p.append(e[i][0])
    q.append(e[i][1])
    s.append(e[i][2])
    r.append(e[i][3])
a['Roll Nmumber']=p
a['Name']=q
a['activity']=s
a['Activity points']=r

print(a)
df=pd.DataFrame(data=a)
print(df)
df.to_excel("Activity_points.xlsx")
print("Rejected certificates are :",z)