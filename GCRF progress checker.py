import requests
from bs4 import BeautifulSoup


url = input("\n Enter your Google Cloud Public Profile URL : ")

quests = ["Google Cloud Essentials","Baseline: Infrastructure","Networking in Google Cloud ","Kubernetes in Google Cloud","Cloud Engineering","DevOps Essentials","Understanding Your Google Cloud Costs","Google Cloud Solutions I: Scaling Your Infrastructure","Cloud Architecture","Google Cloud's Operations Suite","Google Developer Essentials","OK Google: Build Interactive Apps with Google Assistant","Cloud Development","Website on Google Cloud","Baseline: Deploy & Develop","Exploring APIs","IoT in the Google Cloud","Workspace: Add-ons","Build Apps & Websites with Firebase","Google Cloud Run Serverless Workshop","BigQuery Basics for Data Analysts","BigQuery for Machine Learning","BigQuery for Marketing Analysts","NCAA® March Madness®: Bracketology with Google Cloud","Applied Data: Blockchain","Data Engineering","Cloud SQL","BigQuery for Data Warehousing","Scientific Data Processing","Google Cloud Solutions II: Data and Machine Learning","Baseline: Data, ML, AI","Intro to ML: Language Processing","Intro to ML: Image Processing","Machine Learning APIs","Intermediate ML: TensorFlow on Google Cloud","Advanced ML: ML Infrastructure","Cloud Logging","Security & Identity Fundamentals","Security & Identity Fundamentals","Cloud Healthcare API"]

badges = ['Create and Manage Cloud Resources','Perform Foundational Infrastructure Tasks in Google Cloud','Build and Secure Networks in Google Cloud','Deploy to Kubernetes in Google Cloud','Set Up and Configure a Cloud Environment in Google Cloud','Cloud Architecture: Design, Implement, and Manage','Implement DevOps in Google Cloud','Monitor and Log with Google Cloud Operations Suite','Build Interactive Apps with Google Assistant','Build a Website on Google Cloud','Serverless Firebase Development','Serverless Cloud Run Development','Insights from Data with BigQuery','Insights from Data with BigQuery','Insights from Data with BigQuery','Perform Foundational Data, ML, and AI Tasks in Google Cloud','Integrate with Machine Learning APIs','Ensure Access & Identity in Google Cloud','Secure Workloads in Google Kubernetes Engine']

q_completed = []
b_completed = []

r = requests.get(url)
soup = BeautifulSoup(r.content, 'html.parser')
f = soup.find_all(class_='ql-subhead-1 l-mts')
name = soup.select('h1.ql-headline-1')[0].text.strip()
print('\n Profile Name :',name)
list = []
cnt = 0
q_cnt = 0
b_cnt = 0
#Adding all Completed Items into a list 
for line in f:
    txt = line.text.strip('\n')
    list.append(txt)
#print's all completed Badges/Quests
print('\n Total Completed Quests/Badges')
for word in list:
    cnt += 1
    print(cnt,word)
#separating the Quests & Badges From Completed List
for word in list:
    q = word in quests
    if(q==True):
        q_completed.append(word)
    b = word in badges
    if(b==True):
        b_completed.append(word)
#Print's all completed Quests
print('\n Completed Quests')
for word in q_completed:
    q_cnt += 1
    print(q_cnt,word)
#Print's all completed Badges
print('\n Completed Skill Badges')
for word in b_completed:
    b_cnt += 1
    print(b_cnt,word)

def m1():
    if(q_cnt>10 and b_cnt>5) or (q_cnt==10 and b_cnt==5):
        print("\nMilestone #1 Completed(10 Quests & 5 Skill Badges)")
        print("\nPrizes : Shirt, Buttuon Badge, Pen, Stickers")
    else:
        q = 10-q_cnt
        b = 5-b_cnt
        print("\nMilestone #1 NOT-Completed(10 Quests & 5 Skill Badges)")
        print(f'Progress  Quests : {q}/10   Badges : {b}/5')

def m2():
    if(q_cnt>20 and b_cnt>10) or (q_cnt==20 and b_cnt==10):
        print("\nMilestone #2 Completed(20 Quests & 10 Skill Badges)")
        print("\nPrizes : Sipper, Shirt, Buttuon Badge, Pen, Stickers")
    else:
        q = 20-q_cnt
        b = 10-b_cnt
        print("\nMilestone #2 NOT-Completed(20 Quests & 10 Skill Badges)")
        print(f'Progress  Quests : {q} Left   Badges : {b} Left')
def m3():
    if(q_cnt>30 and b_cnt>15) or (q_cnt==30 and b_cnt==15):
        print("\nMilestone #3 Completed(30 Quests & 15 Skill Badges)")
        print("Prizes : Bag, Sipper, Shirt, Buttuon Badge, Pen, Stickers")
    else:
        q = 30-q_cnt
        b = 15-b_cnt
        print("\nMilestone #3 NOT-Completed(30 Quests & 15 Skill Badges)")
        print(f'Progress  Quests : {q} Left   Badges : {b} Left')
def m4():
    if(q_cnt>40 and b_cnt>20) or (q_cnt==40 and b_cnt==20):
        print("\nMilestone #4 Completed(40 Quests & 20 Skill Badges)")
        print("\nPrizes : Voucher, Sipper, Shirt, Buttuon Badge, Pen, Stickers")
    else:
        q = 40-q_cnt
        b = 20-b_cnt
        print("\nMilestone #4 NOT-Completed(40 Quests & 20 Skill Badges)")
        print(f'Progress  Quests : {q} Left   Badges : {b} Left')
def progess():
    q = 40-q_cnt
    b = 20-b_cnt
    per = (cnt/60)*100
    print(f'\nProgress : {cnt}/60 ==> {per}%')
    print(f'Quests : {q_cnt}/40')
    print(f'Badges : {b_cnt}/20')
    print(f'{q} Left To Complete All Quests')
    print(f'{b} Left TO Complete All Skill Badges')
    

print('\nMilestone Progress \n')
m1()
m2()
m3()
m4()
progess()
