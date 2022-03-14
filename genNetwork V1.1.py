import ctypes
import string
import os
import time
from pystyle import *
from pystyle import Colorate, Colors, System, Center, Write, Anime #Merci Billy de proposer du bon contenue
LICNECE = """
discord.gg/bap  ||  2022  ||  https://github.com/cxkalebg
"""


USE_WEBHOOK = True

print(LICNECE)

time.sleep(3)
os.system('cls' if os.name == 'nt' else 'clear')


try: 
    from discord_webhook import DiscordWebhook  
except ImportError:  
    
    input(
        f"Le Module discord_webhook n'est pas installer, pour le download, fais simplement '{'py -3' if os.name == 'nt' else 'python3.8'} -m pip install discord_webhook'\nTu peus ignorer si tu veux pas utiliser de webhook\nAppuie sur entrer pour quitter")
    USE_WEBHOOK = False
try:  
    import requests  
except ImportError:  
   
    input(
        f"Le Module requests n'est pas installer, pour le download, fais simplement '{'py -3' if os.name == 'nt' else 'python3.8'} -m pip install requests'\nAppuie sur entrer pour quitter")
    exit()  
try:  
    import numpy  
except ImportError:  
    
    input(
        f"Le Module numpy n'est pas installer, pour le download, fais simplement '{'py -3' if os.name == 'nt' else 'python3.8'} -m pip install numpy'\nAppuie sur entrer pour quitter")
    exit()  


class NitroGen: 
    def __init__(self): 
        self.fileName = "Codes Nitro.txt" 

    def main(self):  
        os.system('cls' if os.name == 'nt' else 'clear')  
        if os.name == "nt":  
            print("")
            ctypes.windll.kernel32.SetConsoleTitleW(
                "Nitro Generator / Checker - Made by cxka'bap#2222")  
        else:  
            print(f'\33]0;Nitro Generator and Checker - Made by cxka\a',
                  end='', flush=True)  

        banner = r"""Bientôt de nouveaux Services de GEN
       ______              _   __     __                      __  
      / ____/__  ____     / | / /__  / /__      ______  _____/ /__
     / / __/ _ \/ __ \   /  |/ / _ \/ __/ | /| / / __ \/ ___/ //_/
    / /_/ /  __/ / / /  / /|  /  __/ /_ | |/ |/ / /_/ / /  / ,<   
    \____/\___/_/ /_/  /_/ |_/\___/\__/ |__/|__/\____/_/  /_/|_|  
                                                        
                              > by Cxka <                   V1.1              """
        
        Anime.Fade(Center.Center(banner), Colors.green_to_cyan, Colorate.Vertical, enter=True)

        time.sleep(2)  

        self.slowType("Made by : cxka'bap#2222", .02)
        time.sleep(1)  
        
        self.slowType(
            "\nCombien de code nitro veux-tu gen ? : ", .02, newLine=False)
        
        try:
            num = int(input(''))  
        except ValueError:
            input("T'as pas écris un nombre la frérot\nAppuie sur entrer pour quitter")
            exit()  

        if USE_WEBHOOK:
            
            self.slowType(
                "Webhook : *** SOON ***", .02, newLine=False)
            url = input('')  
            
            webhook = url if url != "" else None
            
            if webhook is not None:
                DiscordWebhook(  
                        url=url,
                        content=f"```Checker en cours\nLes codes s'enverront ici```"
                    ).execute()

        

        valide = []  
        invalide = 0  
        chars = []
        chars[:0] = string.ascii_letters + string.digits

        
        c = numpy.random.choice(chars, size=[num, 23])
        for s in c:  
            try:
                code = ''.join(x for x in s)
                url = f"https://discord.gift/{code}"  

                result = self.quickChecker(url, webhook)  

                if result:  
                    
                    valide.append(url)
                else:  
                    invalide += 1  
            except KeyboardInterrupt:
                
                print("\nItterompu par Un Utilisateur")
                break  

            except Exception as e:  
                print(f" Erreur | {url} ")  

            if os.name == "nt":  
                ctypes.windll.kernel32.SetConsoleTitleW(
                    f"Nitro Generator / Checker - {len(valide)} Valide | {invalide} Invalide - Made by cxka'bap#2222")  
                print("")
            else:  
                
                print(
                    f'\33]0;Nitro Generator and Checker - {len(valid)} Valid | {invalide} Invalide - Made by Made by cxka\a', end='', flush=True)

        print(f"""
Resultats :
 Valide : {len(valide)}
 Invalide : {invalide}
 Codes Valide : {', '.join(valide)}""")  

        
        input("\nFini !!   appuie sur entrer 5 fois pour fermer la fenêtre, et le programme")
        [input(i) for i in range(4, 0, -1)]  

    
    def slowType(self, text: str, speed: float, newLine=True):
        for i in text:  
            
            print(i, end="", flush=True)
            time.sleep(speed)  
        if newLine:  
            print()  

    def quickChecker(self, nitro:str, notify=None):  
        
        url = f"https://discordapp.com/api/v9/entitlements/gift-codes/{nitro}?with_application=false&with_subscription_plan=true"
        response = requests.get(url)  

        if response.status_code == 200:  
            
            print(f" Valid | {nitro} ", flush=True,
                  end="" if os.name == 'nt' else "\n")
            with open("Codes Nitro.txt", "w") as file:  
                
                file.write(nitro)

            if notify is not None:  
                DiscordWebhook(  
                    url=url,
                    content=f"Un code valide est detecté ! @everyone \n{nitro}"
                ).execute()

            return True  

        
        else:
            
            print(f" Invalide | {nitro} ", flush=True,
                  end="" if os.name == 'nt' else "\n")
            return False  


if __name__ == '__main__':
    Gen = NitroGen()  
    Gen.main() 
    
#cxka
