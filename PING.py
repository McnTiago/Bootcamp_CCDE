import os #Importa o modulo ou biblioteca os (integra os programas e recursos do S.O
import time #Importa o modulo ou biblioteca time

with open('hosts') as file: #Condiçao para abertura do arquivo hosts
    dump = file.read() #Cria uma váriável Dump e joga dentro dela o arquivo hosts
    dump = dump.splitlines() #splita as linhas da váriael para que fiquem organizadas
    for ip in dump: #Comando para o que irá fazer para cada IP encontrado em Dump
        print('Verificando IP: ', ip) #Mostra o IP que está sendo verificado
        print('-' * 60) #Imprime - 60 vezes
        os.system('ping -c 2 {}'.format(ip)) #Envia os pacotes de IP 2 vezes para verificar se tem resposta
        print("-" * 60) #Imprime - 60 vezes
        time.sleep(5) #Dá um intervalo de 5 segundos para verificação do próximo IP