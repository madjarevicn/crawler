import re
import requests
import cyrtranslit
import webbrowser
#raf
url_steva = "https://raf.edu.rs/o-nama/nastavnici-i-saradnici/item/5578-milinkovic-a-stevan"
url_svi = "https://raf.edu.rs/o-nama/nastavnici-i-saradnici/"

def crawl_data_about_staff(url_steva):
    page = requests.get(url_steva)
    ime = re.findall(r'<h1 style="text-transform:none">(.*?)</h1>', page.text, flags=0)
    print cyrtranslit.to_latin(ime[0].encode('utf8'),'sr')
    return ime[0]


def crawl_stuff(url_svi):
    page = requests.get(url_svi)
    names = re.findall(r'<h2>[\s]*<a href="/o-nama/nastavnici-i-saradnici/item/.*?">(.*?)</a>',page.text,flags=0)
    links = re.findall(r'<header>[\s]*<h2>[\s]*<a href="/o-nama/nastavnici-i-saradnici/item/(.*?)">',page.text,flags=0)
    i=1
    for name in names:
        print '[',i,']',cyrtranslit.to_cyrillic(name.encode('utf8'),'sr')
        print '[',i,'] - url = ',url_svi.__add__('item/').__add__(links[i-1])
        i=i+1



if __name__ == '__main__':
    print ("[1] Prikaz jednog imena iz cirilice na latinici? ")
    print ("[2] Prikaz imena svih profesora na cirilici? ")

    while(True):
        x = input('>>>')
        if(x==1):
            crawl_data_about_staff(url_steva)
        elif(x==2):
            crawl_stuff(url_svi)

        else:
            raise Exception('Pogresan unos')



