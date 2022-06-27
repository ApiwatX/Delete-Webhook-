import requests
from pystyle import Colorate, Colors, Center
from os import system
from time import sleep

boucle1 = True

header_final = """
─╔╗─────────╔╗────     ───────╔╗─╔╗───────╔╗─
╔╝║╔═╗╔╗─╔═╗║╚╗╔═╗     ╔╦╦╗╔═╗║╚╗║╚╗╔═╗╔═╗║╠╗
║╬║║╩╣║╚╗║╩╣║╔╣║╩╣     ║║║║║╩╣║╬║║║║║╬║║╬║║═╣
╚═╝╚═╝╚═╝╚═╝╚═╝╚═╝     ╚══╝╚═╝╚═╝╚╩╝╚═╝╚═╝╚╩╝

"""

while boucle1:
    system('clear')
    print(Colorate.Diagonal(Colors.purple_to_blue, Center.XCenter(header_final)))
    print(Colorate.Horizontal(Colors.purple_to_blue, "[?] ลิ้งเว็บฮุค↓"))
    webhook_url = input("")
    if webhook_url.startswith("https://discord.com/api/webhooks/"):
        try:
            system('clear')
            requests.delete(webhook_url.rstrip())
            print(Colorate.Diagonal(Colors.purple_to_blue, Center.XCenter(header_final)))
            print(Colorate.Horizontal(Colors.purple_to_blue, "ลบแล้วจ้า"))
            sleep(5)
        except:
            system('clear')
            print(Colorate.Diagonal(Colors.purple_to_blue, Center.XCenter(header_final)))
            print(Colorate.Horizontal(Colors.yellow_to_red, "[!] ผิดพลาด"))
            sleep(2)
    else:
            system('clear')
            print(Colorate.Diagonal(Colors.purple_to_blue, Center.XCenter(header_final)))
            print(Colorate.Horizontal(Colors.yellow_to_red, "[!] ผิดพลาด"))
            sleep(2)