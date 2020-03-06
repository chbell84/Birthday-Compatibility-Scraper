#!/usr/bin/python3.x
from html.parser import HTMLParser
import urllib.request
import re
import time
import datetime
import sys
from datetime import timedelta

#http://astro.cafeastrology.com/astro.php?page=comp2f&d1day=25&d1month=8&d1year=1984&d2day=5&d2month=3&d2year=1988

def birthdayCompatibility(d1,d2):
    url = ("http://astro.cafeastrology.com/astro.php?page=comp2f&d1day=%s&d1month=%s&d1year=%s&d2day=%s&d2month=%s&d2year=%s" % (d1.day,d1.month,d1.year,d2.day,d2.month,d2.year))
    req=urllib.request.Request(
                                url,
                                data=None,
                                headers={
                                'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.5 Safari/605.1.15'
                                })
    try:
        page=urllib.request.urlopen(req)
    except urllib.error.HTTPError:
        print("urllib.error.HTTPError on %s-%s-%s" % (d2.month,d2.day,d2.year))
        return
    rawhtml = page.read().decode('utf-8')
    regex = re.compile('<td align=\"right\"> (\d+)</td><td align=\"right\"\>\s(-*\d+)<\/td><td align=\"right\">\s(-*\d+)<\/td><\/tr><\/table>')
    scores = regex.search(rawhtml)
    if scores:
        return [("%s-%s-%s" % (d2.month,d2.day,d2.year)) ,int(scores.group(1)), int(scores.group(2)),int(scores.group(3))]
    else:
        return
def print_scores(scores):
    for i in scores:
        if i is not None:
            print(i[0],',',i[1],',',i[2],',', i[3])

def main(argv):
    #print("The program is starting\n")
    year = timedelta(days=365)
    day = timedelta(days=1)
    print("Argv:",argv)
    if len(argv)==4:
        birthdate = datetime.date(int(argv[1]),int(argv[2]),int(argv[3]))
    else:
        print("Need birthdate: YYYY MM DD")
        return
    age = datetime.date.today() - birthdate
    youngAge = age/2 + year*7
    #youngAge = age - year
    youngDate = datetime.date.today() - youngAge
    #oldAge = age + year
    oldAge = (age - year*7)*2
    #oldDate = datetime.date.today() - oldAge
    timeSpan = oldAge - youngAge
    timeSpan = timeSpan.days
    birthday_scores = []
    for i in range(0,timeSpan):
        birthday_scores.append(birthdayCompatibility(birthdate, youngDate-day*i))
        if i > 1 and i % 10 == 0:
            time.sleep(1)
            print_scores(birthday_scores)
            birthday_scores = []
    print_scores(birthday_scores)
main(sys.argv)
