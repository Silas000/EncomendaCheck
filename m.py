import requests
import time
import pyautogui
import math
def move_mouse():
    R = 400
    (x,y) = pyautogui.size()
    (X,Y) = pyautogui.position(x/2,y/2)
    STEP = 15
    for angle_deg in range(0, 360, STEP):
        angle_rad = math.radians(angle_deg)
        pyautogui.moveTo(
                X + R * math.cos(angle_rad),
                Y + R * math.sin(angle_rad))
print("Bem vindo ao: ")
print("69 78 67 79 77 69 78 68 65 \n67 72 69 67 75 \n Feito por Silas Rosário")
url_site = 'https://www.linkcorreios.com.br/?id='
cod = input('Insira o codigo de rastreamento dos correios: ')
intervalo = int(input('Digite o tempo de intervalo em min Ex 60: '))
intervalo = (intervalo*60)
url_completo = url_site + cod 
while True:
        r = requests.get(url_completo)
        html = r.text
        if '<li>Status: <b>Objeto saiu para entrega ao destinatário</b></li>' in html:
            print('Objeto saiu para entrega')
            move_mouse()
        elif '- Verifique se o código do objeto está correto;' in html:
            print('Codigo Incorreto')
            exit()
        else:
            print('Objeto ainda não saiu')
        time.sleep(intervalo)

            
