import requests
import time
from datetime import datetime

#host = input("Informe o serviço web que deseja monitorar:\n")
#print(f'{site}')
host = "https://evolux.net.br"

print ("Iniciando o monitoramento de " + host + ".\nPara encerrar, pressione crtl + C.\n Monitoramento salvo em ./monitoramento.log")
while True:
    log = open("monitoramento.log", "a")
    try:
        response = requests.get(host)
        response.raise_for_status()
        now = datetime.now()
        log.write (str(now) + " " + host + " " + str(response.status_code) + "\n")
    except requests.exceptions.HTTPError as error:
        now = datetime.now()
        log.write (str(now) + " " + host + " " + str(error) + "\n")
    except requests.ConnectionError as error:
        now = datetime.now()
        log.write (str(now) + " " + host + " Erro de conexao\n")
    except requests.Timeout as error:
        now = datetime.now()
        log.write (str(now) + " " + host + " Request Timeout\n")
    log.close()
    time.sleep(15)

#print (response.status_code)
