from datetime import datetime,timedelta
from time import sleep 
from os import system
from colorama import Fore
import platform
banner="""
██████╗  ██████╗ ███╗   ███╗
██╔══██╗██╔═══██╗████╗ ████║
██████╔╝██║   ██║██╔████╔██║
██╔═══╝ ██║   ██║██║╚██╔╝██║
██║     ╚██████╔╝██║ ╚═╝ ██║
╚═╝      ╚═════╝ ╚═╝     ╚═╝"""
alasArriba = """
     ▄   ▄
 ▄█▄ █▀█▀█ ▄█▄
▀▀████▄█▄████▀▀
     ▀█▀█▀
"""
alasHorizontales = """
     ▄   ▄
     █▀█▀█ 
▀▀████▄█▄████▀▀
     ▀█▀█▀
"""
alasAbajo = """
     ▄   ▄
     █▀█▀█ 
▀▀████▄█▄████▀▀
   ▀ ▀█▀█▀ ▀
"""
colaAbajo = """
▄   ▄
█▀█▀█
█▄█▄█
 ███  ▄▄
 ████▐█ █
 ████   █
 ▀▀▀▀▀▀▀
"""
colaMedio = """
▄   ▄
█▀█▀█
█▄█▄█  ▄▄ 
 ███    █
 ████   █
 ████   █
 ▀▀▀▀▀▀▀
"""
colaArriba = """
▄   ▄
█▀█▀█
█▄█▄█   █ 
 ███    █
 ████   █
 ████   █
 ▀▀▀▀▀▀▀
"""
def clear():
    if(str(platform.system())=='Windows'):
        system('cls')
    elif(str(platform.system())=='Linux'):
        system('clear')
def normalizarFormato(numTime):
    if(len(str(numTime))==1):
        return f'0{str(numTime)}'
    else:
        return f'{str(numTime)}'
def sound():
    try:
        system('mpv noti.mp3')
    except:
        pass
def cronometro(_list,minuts,color):
    comienzo = datetime.now()
    while True:
        now = datetime.now()
        diferencia = timedelta(days=comienzo.day,hours=comienzo.hour,minutes=comienzo.minute,seconds=comienzo.second) 
        for e in _list[:-1]:
            clear()
            print(color+e+(now-diferencia).strftime("%M:%S")+Fore.RESET)
            sleep(0.5)
        _list.reverse()
        if(now.strftime("%Y-%m-%d %H:%M:%S")==(comienzo+timedelta(minutes=minuts)).strftime("%Y-%m-%d %H:%M:%S")):
            sound()
            break
def main():
    clear()
    print(banner)
    work = int(input('[+] Ingresar los minutos de trabajo: '))
    chill = int(input('[+] Ingresar el tiempo de descanso: '))
    while True:
        listAlas = list([alasArriba,alasHorizontales,alasAbajo])
        listRest = list([colaAbajo,colaMedio,colaArriba])
        cronometro(listAlas,work,Fore.GREEN)
        cronometro(listRest,chill,Fore.RED)
        clear()
        if(input('Continuar?: ')!=('Y'or'Yes'or'y'or'yes')):
            break
if __name__=='__main__':
    main()