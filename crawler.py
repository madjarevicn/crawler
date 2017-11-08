import re
import requests
from Entities import Employee
from Entities import Company

def crawl_employees():
    #website for employees
    url=  'http://www.greenpeace.org/usa/about/board-members/'
    #getting source code of url
    page = requests.get(url)
    #Ispisujemo u fajl tekst - cisto radi primera ispisa u fajl
    text_file = open("output.txt", "w")
    text_file.write(page.text.encode('utf8'))
    text_file.close()
    #pomocu regularnih izraza uzimamo podatke
    names=re.findall(r'<h3 class="teaser-title title">[\s]*<a href="http://www.greenpeace.org/usa/bios/.*?/">(.*?)</a>[\s]*</h3>',page.text,flags=0)
    position=re.findall(r'<div class="teaser-author smallText">[\s]*(.*?)[\s]*</div>',page.text,flags=0)
    descriptions = re.findall(r'<div class="teaser-summary">[\s]*<p>(.*?)</p>[\s]*</div>',page.text,flags=0)

    emploeyees = []
    #Punimo niz zaposlenima
    for i in range(0,len(names)):
        e = Employee(names[i],position[i],descriptions[i])
        emploeyees.append(e)
    #vracamo ga
    return emploeyees



def crawl_about():
    url = 'http://www.greenpeace.org/usa/about/'
    page = requests.get(url)
    about = re.findall(r'<meta property="og:description"[\s]*content="(.*?)" />',page.text,flags=0)
    return about[0]

def crawl_history():
    url = 'http://www.greenpeace.org/usa/about/'
    page = requests.get(url)
    history = re.findall(r'<h2>Our History</h2>[\s]*<p>(.*?)</p>[\s]*<p>',page.text,flags=0)
    return history[0]


def crawl_camapigns():
    url = 'http://www.greenpeace.org/international/en/campaigns/'
    page = requests.get(url)
    #napravili smo dictionary koji ce cuvati kao key kampanju a kao value ce cuvati link do nje
    dict = {}
    campaigns = re.findall(r'<li>[\s]*<a href="/international/en/campaigns/.*?/" class="drop" .*?>(.*?)</a>',page.text,flags=0)
    links_to_campaigns = re.findall(r' <li>[\s]*<a href="/international/en/campaigns/(.*?)" class="drop" title=".*?">.*?</a>',page.text,flags=0)
    for i in range(0,len(campaigns)):
        links_to_campaigns[i]=url + links_to_campaigns[i]
        dict[campaigns[i]]=links_to_campaigns[i]

    return dict

