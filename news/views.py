from django.shortcuts import render
import requests
from bs4 import BeautifulSoup
from django.http import HttpResponse


toi_r = requests.get("https://timesofindia.indiatimes.com/briefs")
toi_soup = BeautifulSoup(toi_r.content, 'html5lib')

toi_headings = toi_soup.find_all('h2')

toi_headings = toi_headings[3:16]

toi_news = []

for th in toi_headings:
    toi_news.append(th.text)



categ_sp= requests.get("https://timesofindia.indiatimes.com/briefs/sports")
toi_sp = BeautifulSoup(categ_sp.content, 'html5lib')
toi_hgs = toi_sp.findAll('h2')
toi_hgs = toi_hgs[3:16] 
toi_newsp = []

for toi_sp in toi_hgs:
    toi_newsp.append(toi_sp.text)



# categ_spx= requests.get("https://www.outlookindia.com/sports")
# ot_sp = BeautifulSoup(categ_spx.content, 'html5lib')
# ot_hgs = ot_sp.findAll('h4')
# ot_hgs = ot_hgs[3:15]
# ot_newsp = []

# for ot_sp in ot_hgs:
#     ot_newsp.append(ot_sp.text)

categ_spx= requests.get("https://www.indiatoday.in/sports")
it_sp = BeautifulSoup(categ_spx.content, 'html5lib')
it_hgs = it_sp.findAll('h3')
it_hgs = it_hgs[3:15]
it_newsp = []

for it_sp in it_hgs:
    it_newsp.append(it_sp.text)


categ_pox= requests.get("https://www.indiatoday.in/politics")
it_po = BeautifulSoup(categ_pox.content, 'html5lib')
it_hgpo = it_po.findAll('h2')
it_hgpo=it_hgpo[3:18]
it_newspo=[]



for it_po in it_hgpo:
    it_newspo.append(it_po.text)






categ_po= requests.get("https://timesofindia.indiatimes.com/politics/news")
toi_po = BeautifulSoup(categ_po.content, 'html5lib')
toi_hgpo = toi_po.findAll("span", {"class": "w_tle"})
toi_hgpo=toi_hgpo[3:18]
toi_newspo=[]


for toi_po in toi_hgpo:
    toi_newspo.append(toi_po.text)


categ_edu= requests.get("https://indianexpress.com/section/education/")
ixe_edu = BeautifulSoup(categ_edu.content, 'html5lib')
ixe_hgedu = ixe_edu.findAll('h2')
ixe_hgedu=ixe_hgedu[3:18]
ixe_newsedu=[]


for ixe_edu in ixe_hgedu:
    ixe_newsedu.append(ixe_edu.text)

categ_tec= requests.get("https://timesofindia.indiatimes.com/gadgets-news")
toi_tec = BeautifulSoup(categ_tec.content, 'html5lib')
toi_hgtec = toi_tec.findAll("span", {"class": "w_tle"})
toi_hgtec=toi_hgtec[23:37]
toi_newstec=[]


for toi_tec in toi_hgtec:
    toi_newstec.append(toi_tec.text)

# categ_tecx= requests.get("https://www.outlookindia.com/topic/science-technology")
# ot_tec = BeautifulSoup(categ_tecx.content, 'html5lib')
# ot_hgtec = ot_tec.findAll('h4')
# ot_hgtec=ot_hgtec[3:18]
# ot_newstec=[]


# for ot_tec in ot_hgtec:
#     ot_newstec.append(ot_tec.text)

categ_tecx= requests.get("https://www.indiatoday.in/technology")
it_tec = BeautifulSoup(categ_tecx.content, 'html5lib')
it_hgtec = it_tec.findAll("h2")
it_hgtec=it_hgtec[3:18]
it_newstec=[]


for it_tec in it_hgtec:
    it_newstec.append(it_tec.text)


ot_r = requests.get("https://www.outlookindia.com/national")
ot_soup = BeautifulSoup(ot_r.content, 'html5lib')
ot_headings = ot_soup.findAll('p')
ot_headings = ot_headings[3:12]
ot_news = []

for oth in ot_headings:
    ot_news.append(oth.text)

categ_wea= requests.get("https://indianexpress.com/section/weather/")
ixe_wea = BeautifulSoup(categ_wea.content, 'html5lib')
ixe_hgwea = ixe_wea.findAll('h2')
ixe_hgwea=ixe_hgwea[3:18]
ixe_newswea=[]


for ixe_wea in ixe_hgwea:
    ixe_newswea.append(ixe_wea.text)


def home(req):
    return render(req, 'index.html')
def main(req):
    return render(req, 'PblProject.html', {'toi_news':toi_news, 'ot_news': ot_news})

def aboutx(req):
    return render(req, 'about.html')

def categories_sp(req):
    return render(req, 'PblProject_sp.html',{'toi_newsp':toi_newsp ,'it_newsp':it_newsp})

def categories_po(req):
    return render(req, 'PblProject_po.html',{'toi_newspo':toi_newspo ,'it_newspo':it_newspo})

def categories_edu(req):
    return render(req, 'PblProject_edu.html',{'ixe_newsedu':ixe_newsedu})

def categories_tec(req):
    return render(req, 'PblProject_tec.html',{'toi_newstec':toi_newstec ,'it_newstec':it_newstec})

def categories_wea(req):
    return render(req, 'PblProject_wea.html',{'ixe_newswea':ixe_newswea})










