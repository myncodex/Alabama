#import files
import os
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
import cv2
import glob
import pytesseract
import csv
import pandas as pd
import datetime

#pytesseract funtion to read text from certificates
def ocr_core(img):
    text = pytesseract.image_to_string(img)
    return text

#google authentication
gauth =  GoogleAuth()
drive = GoogleDrive(gauth)

#marks calculator
def calculations():
    e=[]
    z=[]
    names={'jeomol jhon':1,'jose ben':2,'joyal johnson':3,'k.s. gopi krishnan':4,'k s sooraj':5,'karina p joshi':6,'keerthana jayakumar':7,'krishna priya p':8,'malavika m nair':10,'manal zubair':11,'manu mahendran':12,'mareena benny':13,'mirzad m nellickal':14,'muhammed sadhath v h':15,'muskan m a':16,'namitha jason':17,'nanda p':18,'nandana p':18,'navaz p zakkaria':20,'naveena t s':21,'nihal biljith':22,'nikhitha jhonson':23,'nima subair':24,'nimah mehrin':25,'nivedhya gopi':26,'niveditha mathew':27,'noel mathew':28,'p anand':29,'pragathy mohonan':31,'praharsha sooraj':32,'pratyush p t':33,'r aishwarya':34,'rahul ramesh':35,'razal ali k a':36,'riddhi m sarbender':37,'rishi b sanil':38,'riya rose paul':39,'rizwan ahammed rafeeq':40,'ruth elizabeth roshan':42,'saanthanu prasad':43,'sachit sabastian':44,'sanoop m j':45,'sayujya':46,'seetha m n':47,'sidharth v nair':48,'sowmya s':49,'sradha sreekumar':50,'srilekshmi j nair':51,'sudheepth s':52,'swetha kalyani m k':53,'tanisha mariya renjy':54,'theertha r l':55,'thejus joseph':56,'v s muhammed shifas':57,'v shyam krishnan':58,'vandhana p':59,'vishnu subi':60,'vishnu vinod':61,'viswajith vijayakumar':62}
    b={'workshop ':5,'webinar ':5,'intership ':40,'course ':10,'seminar ':5,'lecture ':5,"project":10,'event ':5,'talk':5,'quiz':5,'summit':5}
    nits=['national institute of science and technology','nitk','nitc','nitd']
    iits=['indian institute of science and technology','iitb','iitm','iitk','iitd','iitpkd','iit goa']
    path=glob.glob('C:/Users/User/Desktop/Activitypoints/program/*.jpg')
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
    return e

#reading rfid and verifying


def file_upload(name1):    
    rfid={' 103 204 91 18':'nima subair'," 48 137 53 28":'muskan m a',' 144 185 217 27':'manal zubair'}
    with open('capture.txt', 'r') as f:
        lines = f.read().splitlines()
        last_line = lines[-2]
    for i in rfid.keys():
        if i==last_line:
            name1=rfid[i]
    file_loc={'jeomol jhon':'1SyH9GiOx0JO59gN2sqoSomvqpIYiVZ3s','jose ben':'1xGFPMrL21DdHlmMcfphXZtMqdQ7FyRIe','joyal johnson':'1yyy3Ae0H0tEG8q58Zvf8R8tqEMkiFW5m','k.s. gopi krishnan':'1Oc2hr4RNDJvkVx4tmAEvX4sFKDQlKZQo','k s sooraj':'1jlEGFMKfHgYbNpl1yYy5bsAxIajxYLCY','karina p joshi':'1mRSbRFaSWaBCN-XQdTdt0iH5xHpM7x9W','keerthana jayakumar':'14XbjXnGrS31V8OBdOmgYq2kBn8BZ75Dp','krishna priya p':'1rVYQJ6C6ey_tjtiPTqJItjwarKqHNJrg','malavika m nair':'10fiOExZOciU0hyE3C_kZemTte6yTrq7t','manal zubair':'1dPp7uu3qTV-oOupCpljYV1KsONGIV38T','manu mahendran':'1xU25U14YBORClVVJ3XGPYt957oNUbU1T','mareena benny':'1mGjMQWU9VHHJ2XchcDQrHA7HxyYid7dt','mirzad m nellickal':'15wCTkub1Y_G7jchvrtsYfyr55ZWYfjzH','muhammed sadhath v h':'1ZtbshFrjsC8-iDNgfipT96gp9sIUPh6x','muskan m a':'1D6-n-pG4fJuQL-r15l8XsdCgAM6Huvie','namitha jason':'1tDYjvvnHMSqV6wRKK4H9gcLTIaZS7mMa','nanda p':'1Kwhn8hOOzcdlOxjvVhtPc04ATQrDjnkV','nandana m':'1x7NrUtZpKfYlF8uELKDgWIFgwCDsLd','navaz p zakkaria':'1CFMDBjYlvFuBc4YC7gCcghVPKmcIl6uz','naveena t s':'1SsC-5fhPrmUasdJpnesIEk7aWKTsURrH','nihal biljith':'1I4LOq9FgOwndm3YQpZ95pCdlTUYwPzGE','nikhitha jhonson':'1Mt8MKvZoFfNznTplF8PrQOEPp82pq0wJ','nima subair':'11gu8gTyGPxTgFvv39V2TWUJMdcmwVSWI','nimah mehrin':'1o5UnNbTD8tsqntsy6NgZ49','nivedhya gopi':'1wggBUqERjGfFlZOF0wLlHzHBRhWOmIay','niveditha mathew':'1KfairVwhMxjD-ojDCbz_PW_0T90HfIiX','noel mathew':'17OszFYxIS_w6o0DIaTsdQKciiK1HSpEd','p anand':'1D9jUyvVVTIxCr9uOBsk2E0n1c1XBbBjD','pragathy mohonan':'13Fr2-sx6lIQBmbANMZPgTvwoTwTDEnfU','praharsha sooraj':'1-w-mOJCzSZp3K1cZyEAvFgmgzgVgwcvU','pratyush p t':'1fYRfVn78L8VlwHhvG3SC9lDwaFr_SOyY','r aishwarya':'1dG4gxW0GuqkVdrGf6V7WJKFNjLO6RCna','rahul ramesh':'17USFaAMi2OQAx0a2PUcwTW0qoJr62Dhv','razal ali k a':'11Z_4RJa_MxZ7FPNGGfDqenbLpufL61gU','riddhi m sarbender':'1FwITCRnnznPEwIu3U3PlDB7OAEQrehZO','rishi b sanil':'1FFtm3TXTyuffA40xuK4b6ieJ_wFfwKEB','riya rose paul':'1YhhLxXz3FnNF8TBvxRZgLJ44a9ye0AEC','rizwan ahammed rafeeq':'1NQKma-4ICjmWxlw66IAcQBlA-5si9Ksr','ruth elizabeth roshan':'1KTfyq-fLUHRkjkdYswkYxXjLRm16SaX7','saanthanu prasad':'1bWmQ18yeONMtDZUq6cBXsh1yODrIevyJ','sachit sabastian':'1Z0KjmEm_6_H8Z2Nv2Z28trbifgzhc56j','sanoop m j':'1E9niTjVc-3AXg9YRZmNLGKhLajEzx7bJ','sayujya':'1BS4GlzQIY5y1DcQxLP_uorutLbwmuuqt','seetha m n':'1YjUtySBbrSES5dSeDczZHgftD2RN8Yqj','sidharth v nair':'1SX_9qcnzI8nfy79nJb17rXH3GpX58JMR','sowmya s':'1F3uy6PyVlZpYLptB2FLxdL8vBd6tpAmT','sradha sreekumar':'1Ym0jPNtLQheaQjRshxHUnMDsPIr8ATSI','srilekshmi j nair':'1ilZHVPYZlaEmqdcNZ_kkPTwaL3oCkGgU','sudheepth s':'18rzjysEXtZFL9hCH60cREHUlHmeW8-aM','swetha kalyani m k':'1WrXkJZDxz2XhNSlvWuLetl9yp0dOR_RS','tanisha mariya renjy':'1c5D5gzpFr-mtc6V2GwQBBfIPOoMsgGRM','theertha r l':'18PPQz7wIG9I-vuWhw5nK-01IkpxMpb7d','thejus joseph':'1PKEXIUIWLAWFoGkCKjjvAqOqGaOLZQlN','v s muhammed shifas':'1JaFqwJLTXu_vnxTn1Z4eag2nqYgXROn1','v shyam krishnan':'1Xu2-MmScDiLJRBhYGKV3_x-lpqwZDvfq','vandhana p':'1M6v2GxBBOrju0iO1uUE0cE_A99YNz8T7','vishnu subi':'1SGqklQLvdNQNGhQDlnBWToGpeNu9fe5I','vishnu vinod':'18FRaqukJyudbnqTz7J5xT84jvHozY7se','viswajith vijayakumar':'1mgE7OXdbgYZxK60GFSHBEKCVdCIky4wS'}
    if name1 in file_loc.keys():
        print(name1+' is verified')
        #downloading files in the personal folder
        folder=file_loc[name1]
        print(folder)
        file_list=drive.ListFile({'q':f"'{folder}' in parents and trashed=false"}).GetList()
        for index,file in enumerate(file_list):
            print(index+1,'file downloaded: ',file['title'])
            file.GetContentFile(file['title'])
        a=calculations()
        print(a)
        #deleting files in prog folder

        path=glob.glob('C:/Users/User/Desktop/Activitypoints/program/*.jpg')
        for file in path:
            if os.path.isfile(file):
                os.remove(file)

        #creating txt file to upload output on drive
        activities=[]
        total_points=0
        for i in a :
            activities.append(i[2])
            total_points+=i[3]
        print(a)
        file_list=drive.ListFile({'q':f"'{folder}' in parents and trashed=false"}).GetList()
        for index,file in enumerate(file_list):
            if file['title']=='Activity_points.txt':
                id=file['id']
                file3 = drive.CreateFile({'id':id})
                file3.Delete()
        file1=drive.CreateFile({'parents':[{'id': folder}], 'title':"Activity_points.txt"})
        current_time = datetime.datetime.now()
    
        file1.SetContentString('name of the student: '+name1+'\nRollnumber = '+str(a[0][0])+'\nDate and Time = '+str(current_time)+'\nClass = ECB \nActivities = '+str(activities)+'\nTotal points = '+str(total_points))
        file1.Upload()
        #writing csv file
        
        fin=[name1,a[0][0],activities,total_points]
        return fin
        

#starting point of the prog
final=[]
while True:
    rfid={' 64 96 251 29':'nima subair'," 48 137 53 28":'muskan m a',' 241 23 183 25':'manal zubair'}
    with open('capture.txt', 'r') as f:
        lines = f.read().splitlines()
        last_line = lines[-1]
    for i in rfid.keys():
        if i==last_line:
            name1=rfid[i]
    mc=0
    if last_line not in rfid.keys() and mc==1:
        print("invalid id")
    lin=len(lines)
    
    a=input("Place ur Id card \n Enter \"start\" to calculate Activity points \n else enter \"quit\"  ")
    if a =="start":
        with open('capture.txt', 'r') as f:
            lines1 = f.read().splitlines()
            last_line1 = lines[-1]
        if len(lines)==len(lines1):
            name2=input("Sorry rfid card not detected pls type in your name : ") 
            name1=name2.lower()
            print(a,len(lines))
            mc=1
        lim=file_upload(name1)
        final.append(lim)
    elif a=="quit":
        break
f=open("Totalpoints.csv", 'w')
writer=csv.writer(f)
writer.writerow(['Name','Roll number','Activities','Total points'])# for i in range(0,len(final)):
for i in range(0,len(final)):
    writer.writerow(final[i])    
f.close()
df=pd.read_csv("Totalpoints.csv")
print(df)
df.to_excel("Activity_points.xlsx")
folder2='1ZEBjmCr2RzTs4_fm_O9-GJi2mdxaUAjl'
file_list=drive.ListFile({'q':f"'{folder2}' in parents and trashed=false"}).GetList()
for index,file in enumerate(file_list):
    if file['title']=='Activity_points.xlsx':
        id=file['id']
        file1 = drive.CreateFile({'id':id})
        file1.Delete()
file2=drive.CreateFile({'parents':[{'id': folder2}], 'title':"Activity_points.xlsx"})
file2.SetContentFile('Activity_points.xlsx')
file2.Upload()
    
