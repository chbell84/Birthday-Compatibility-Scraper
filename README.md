# Birthday-Compatibility-Scraper
## Introduction

This program is the product of bordom and the desire to reflect on old relationships in a manner that justifies my past choices. [Birthday][2] [compatibility][3] [websites][4] are a great place to perform such reflection. This program focuses on the [Cafe Astrology][1] birthday combatilibity tool.

At some point I wondered, if these site are providing numerical scores telling you how compatible you are with people who have a particular birthday, it should be possible to calculate the birthdate of person with whom you are most compatibile... or at least rank your age appropriate options. ...so I wrote this scraper to submit a request (like [this one][5]) testing the compatibliity one birthday against the birthdays within a dating appropriate age range. I've decided to use the formula of Your `age/2+7` to determine the low end and `(Your Age-7)*2` on the high end.

[1]: http://astro.cafeastrology.com/astro.php?page=comp2f   "Cafe Astrology Birthday Compatibilty Tool"
[2]: https://www.biorhythmonline.com/birthday-compatibility/   "Biorhythm Compatibility Calculator"
[3]: https://www.thecalculator.co/love/Birthday-Compatibility-Test-492.html  "The Calculator: Birthday Compatibility Test"
[4]: https://www.biolovematch.com   "BioLoveMatch"
[5]: http://astro.cafeastrology.com/astro.php?page=comp2f&d1day=4&d1month=8&d1year=1964&d2day=17&d2month=1&d2year=1964  "Barak and Michelle Birthday Compatibility"

## Usage

The program prints the scores to standard out as in the below example. You can pipe the results to a csv file and load that file into a spreadsheet app and sort the results. Because [web scraping is frowned upon][No Scrapes], only a few requests are handled at a time so the program takes a while to get through all possible birthdates. The older you are, the more longer it takes.

[No Scrapes]: https://www.cloudflare.com/learning/bots/what-is-data-scraping/ "Cloudflare Scraping Info Sheet"

        % python birthdaycompatibility2.py 1964 8 4              
        08/04/1964 , 06/07/1934 , 951 , -217 , 734
        08/04/1964 , 02/14/1953 , 858 , -826 , 32
        08/04/1964 , 09/29/1978 , 783 , -330 , 453
        08/04/1964 , 09/26/1956 , 477 , -724 , -247
        08/04/1964 , 06/16/1923 , 971 , -665 , 306
        08/04/1964 , 07/29/1974 , 630 , -358 , 272
        08/04/1964 , 09/16/1938 , 896 , -725 , 171
        08/04/1964 , 11/22/1927 , 896 , -918 , -22
        08/04/1964 , 04/08/1965 , 1093 , -188 , 905
        08/04/1964 , 05/21/1925 , 616 , -581 , 35
        08/04/1964 , 10/18/1926 , 644 , -714 , -70
        08/04/1964 , 04/23/1971 , 654 , -647 , 7
        08/04/1964 , 02/18/1969 , 704 , -579 , 125
        08/04/1964 , 02/18/1977 , 1184 , -534 , 650
        08/04/1964 , 05/19/1931 , 631 , -115 , 516
        ...

### Dependencies
BirthdayCompatibility2.py is written in Python 3.5 and uses the following dependancies
*   aiohttp
*   asyncio