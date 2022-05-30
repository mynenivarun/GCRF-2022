from itertools import count
import requests
from bs4 import BeautifulSoup

url = input("Enter your Google Cloud Public Profile URL : ")

r = requests.get(url)
soup = BeautifulSoup(r.content, 'html.parser')
f = soup.find_all(class_='ql-subhead-1 l-mts')
list = []
cnt = 0
for line in f:
    cnt += 1
    txt = line.text.strip('\n')
    ap = [cnt,txt]
    list.append(ap)
for word in list:
    print(word)
print('Progress :',cnt,'/60')
if (cnt==15):
    print("Milestone #1 Completed(10 Quests & 5 Skill Badges")
    print("Prizes : Shirt, Buttuon Badge, Pen, Stickers")
elif (cnt==30):
    print("Milestone #2 Completed(20 Quests & 10 Skill Badges")
    print("Prizes : Sipper, Shirt, Buttuon Badge, Pen, Stickers")
elif (cnt==45):
    print("Milestone #3 Completed(30 Quests & 15 Skill Badges")
    print("Prizes : Bag, Sipper, Shirt, Buttuon Badge, Pen, Stickers")
elif (cnt==60):
    print("Milestone #4 Completed(40 Quests & 20 Skill Badges")
    print("Prizes : Voucher, Sipper, Shirt, Buttuon Badge, Pen, Stickers")
    print("You are elgible For Voucher ")
elif(cnt>=0 and cnt<=15):
    t = 15-cnt
    print('complete another ',t,'for reaching Milestone #1')
    print("MileStone #1 Prizes : Shirt, Buttuon Badge, Pen, Stickers")
elif(cnt>=15 and cnt<=30):
    print("Milestone #1 Completed(10 Quests & 5 Skill Badges")
    t = 30-cnt
    print('complete another ',t,'for reaching Milestone #2')
    print("MileStone #2 Prizes : Sipper, Shirt, Buttuon Badge, Pen, Stickers")
elif(cnt>=30 and cnt<=45):
    print("Milestone #1 Completed(10 Quests & 5 Skill Badges")
    print("Milestone #2 Completed(20 Quests & 10 Skill Badges")
    t = 45-cnt
    print('complete another ',t,'for reaching Milestone #3')
    print("MileStone #3 Prizes : Bag, Sipper, Shirt, Buttuon Badge, Pen, Stickers")
elif(cnt>=45 and cnt<=60):
    print("Milestone #1 Completed(10 Quests & 5 Skill Badges")
    print("Milestone #2 Completed(20 Quests & 10 Skill Badges")
    print("Milestone #3 Completed(30 Quests & 15 Skill Badges")
    t = 60-cnt
    print('complete another ',t,'for reaching Milestone #4')
    print("MileStone #4 Prizes : Voucher, Sipper, Shirt, Buttuon Badge, Pen, Stickers")
elif(cnt==0):
    print('there is no progress kindly start doing your labs')
else:
    print("Error occured while executing program")
