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
    txt = line.text.strip('\n')
    list.append(txt)
for word in list:
    cnt += 1
    print(cnt,word)
per = (cnt/60)*100
print(f'\nProgress : {cnt}/60 ==> {per}%')
if (cnt==15):
    print("\nMilestone #1 Completed(10 Quests & 5 Skill Badges)")
    print("\nPrizes : Shirt, Buttuon Badge, Pen, Stickers")
elif (cnt==30):
    print("\nMilestone #2 Completed(20 Quests & 10 Skill Badges)")
    print("\nPrizes : Sipper, Shirt, Buttuon Badge, Pen, Stickers")
elif (cnt==45):
    print("\nMilestone #3 Completed(30 Quests & 15 Skill Badges)")
    print("\nPrizes : Bag, Sipper, Shirt, Buttuon Badge, Pen, Stickers")
elif (cnt==60):
    print("\nMilestone #4 Completed(40 Quests & 20 Skill Badges)")
    print("\nPrizes : Voucher, Sipper, Shirt, Buttuon Badge, Pen, Stickers")
    print("\nYou are elgible For Voucher ")
elif(cnt>=0 and cnt<=15):
    t = 15-cnt
    print('\ncomplete another ',t,'for reaching Milestone #1')
    print("\nMileStone #1 Prizes : Shirt, Buttuon Badge, Pen, Stickers")
elif(cnt>=15 and cnt<=30):
    print("\nMilestone #1 Completed(10 Quests & 5 Skill Badges")
    t = 30-cnt
    print('\ncomplete another ',t,'for reaching Milestone #2')
    print("\nMileStone #2 Prizes : Sipper, Shirt, Buttuon Badge, Pen, Stickers")
elif(cnt>=30 and cnt<=45):
    print("\nMilestone #1 Completed(10 Quests & 5 Skill Badges")
    print("\nMilestone #2 Completed(20 Quests & 10 Skill Badges")
    t = 45-cnt
    print('\ncomplete another ',t,'for reaching Milestone #3')
    print("\nMileStone #3 Prizes : Bag, Sipper, Shirt, Buttuon Badge, Pen, Stickers")
elif(cnt>=45 and cnt<=60):
    print("\nMilestone #1 Completed(10 Quests & 5 Skill Badges")
    print("\nMilestone #2 Completed(20 Quests & 10 Skill Badges")
    print("\nMilestone #3 Completed(30 Quests & 15 Skill Badges")
    t = 60-cnt
    print('\ncomplete another ',t,'for reaching Milestone #4')
    print("\nMileStone #4 Prizes : Voucher, Sipper, Shirt, Buttuon Badge, Pen, Stickers")
elif(cnt==0):
    print('\nthere is no progress kindly start doing your labs')
else:
    print("\nError occured while executing program")
