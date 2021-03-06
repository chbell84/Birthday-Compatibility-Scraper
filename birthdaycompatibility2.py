#!/usr/bin/python3.5
from html.parser import HTMLParser
import re
import time
import datetime
import random
import sys
from aiohttp import ClientSession
import asyncio
from datetime import timedelta

def print_scores(scores, partner_dates):
    regex = re.compile('<td align=\"right\"> (\d+)</td><td align=\"right\"\>\s(-*\d+)<\/td><td align=\"right\">\s(-*\d+)<\/td><\/tr><\/table>')
    #scores = regex.search(rawhtml)
    mdy_regex = re.compile('(\d\d)\/(\d\d)\/(\d\d\d\d)')
    date_regex = re.compile('<tr><th>(\d\d\/\d\d\/\d\d\d\d)<\/th><th>Aspect<\/th><th>(\d\d\/\d\d\/\d\d\d\d)<\/th>')
    for i in scores:
        score = regex.search(i)
        dates = date_regex.search(i)
        if dates is not None and score is not None:
            found = mdy_regex.search(dates.group(2))
            found_date = datetime.date(int(found.group(3)),int(found.group(1)),int(found.group(2)))
            #print(found)
            partner_dates.remove(found_date)
            print(dates.group(1),',',dates.group(2),',',score.group(1),',',score.group(2),',',score.group(3))

async def fetch(session, url):
    async with session.get(url) as response:
        return await response.text()
async def birthday_compatibility(d1,partner_dates, partner_list):
    birthday_scores = []
    tasks = []
    day = timedelta(days=1)
    async with ClientSession() as session:
        for d2 in partner_list:
            url = ("http://astro.cafeastrology.com/astro.php?page=comp2f&d1day=%s&d1month=%s&d1year=%s&d2day=%s&d2month=%s&d2year=%s" % (d1.day,d1.month,d1.year,d2.day,d2.month,d2.year))
            task = asyncio.ensure_future(fetch(session, url))
            tasks.append(task)
        birthday_scores = await asyncio.gather(*tasks)
    print_scores(birthday_scores, partner_dates)

def main(argv):
    #print("The program is starting\n")
    year = timedelta(days=365)
    day = timedelta(days=1)
    if len(argv)>=4:
        d1 = datetime.date(int(argv[1]),int(argv[2]),int(argv[3]))
        age = datetime.date.today() - d1
        if len(argv)==5:
            youngAge = age - year*float(argv[4])
            oldAge = age + year*float(argv[4])
        else:
            youngAge = age/2 + year*7
            oldAge = (age - year*7)*2
        youngDate = datetime.date.today() - youngAge
    else:
        print("Need birthdate: YYYY MM DD")
        return
    
    #oldDate = datetime.date.today() - oldAge
    timeSpan = oldAge - youngAge
    timeSpan = timeSpan.days
    partner_dates = set()
    for i in range(0,timeSpan):
        partner_dates.add(youngDate-day*i)
    while len(partner_dates)>0:
        partner_list = []
        j = 0
        limit = 15
        for partner in partner_dates:
            partner_list.append(partner)
            j += 1
            if j == limit:
                j=0
                break
        loop = asyncio.get_event_loop()
        future = asyncio.ensure_future(birthday_compatibility(d1,partner_dates, partner_list))
        loop.run_until_complete(future)
        time.sleep(random.randint(1,5))

main(sys.argv)
