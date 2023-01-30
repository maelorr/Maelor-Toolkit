import time
import os
print("BEM VINDO AO TOOL-KIT BY MAELOR404")
time.sleep(1)
print("Team 404")
print("Acervo mais completo e grátis do Telegram")
print("↓")
print("t.me/acervoteam404")
time.sleep(3)
print("Meu GitHub: https://github.com/maelorr")
time.sleep(2)
os.system("clear")
print("Aqui irei te mostrar ferramentas comuns do hacking e oque elas fazem")
time.sleep(0.8)
print("Tambem irei fazer a instalação da ferramenta")
time.sleep(0.5)
os.system("clear")
print("[1] Ddos")
print("[2] Sqlmap")
print("[3] Ip-Tracer (feito por membro da 404) ")
print("[4] Ngrok")
print("[5] Metasploit")
print("[6] InfSite (feito por membro da 404)")
print("[7] Moon-DoS (feito por lider da 404")
print("[8] PortScan (feito por lider da 404")
print("[9] Meu Github")
print("[10] Acervo Team404")
print("[11] Sair")
time.sleep(1)
opçao = int(input("Escolha uma das opçoes acima"))

if opçao == 1:
 print("DDoS, ou negação de serviço distribuída, é um tipo de ataque cibernético que tenta indisponibilizar um website ou recurso de rede inundando-o com tráfego mal-intencionado e deixando-o incapaz de operar.")
 os.system("git clone https://github.com/palahsu/DDoS-Ripper")
 os.system("python tool-kit.py")
elif opçao == 2:
 print("Sqlmap é uma ferramenta de teste de penetração de código aberto que automatiza o processo de detecção e exploração de falhas de injeção SQL.")
 os.system("git clone https://github.com/sqlmapproject/sqlmap")
 os.system("python tool-kit.py")
elif opçao == 3:
 print("Ip-Tracker ele é uma ferramenta para pegar informações de um endereço IP.")
 os.system("git clone https://github.com/WBs234/WBIP")
 os.system("python tool-kit.py")
elif opçao == 4:
 print("O que é Ngrok? O Ngrok é uma ferramenta CLI (Comand Line Interface) que te permite criar um túnel seguro, atrás de NATs e Firewalls, que expõem serviços locais para a Internet, tudo isso de forma fácil e segura.")
 os.system("git clone https://github.com/PSecurity/ps.ngrok")
 os.system("python tool-kit.py")
elif opçao == 5:
 print("O Projeto Metasploit é um projeto de segurança de computadores que fornece informações sobre vulnerabilidades de segurança e ajuda em testes de penetração e desenvolvimento de assinaturas IDS.")
 os.system("git clone https://github.com/gushmazuko/metasploit_in_termux")
 os.system("python tool-kit.py")
elif opçao == 6:
 print("O InfSite pega as informações de um site para fazer um ataque")
 os.system("git clone https://github.com/WBs234/InfSiteWB")
 os.system("python tool-kit.py")
elif opçao == 7:
 print("Está ferramenta que nem o proprio nome ja diz ira fazer a verificaçao das portas de uma conexao")
 os.system("git clone https://github.com/koppyy/portscanpy")
 os.system("python tool-kit.py")
elif opçao == 8:
 print("O DOS, sigla para Disk Operating System ou sistema operacional em disco[1] é um acrónimo para vários sistemas operativos intimamente relacionados que dominaram o mercado para compatíveis IBM PC entre 1981 e 1995, ou até cerca de 2000 caso sejam incluídas as versões de Microsoft Windows parcialmente baseadas em DOS: Windows 3.11, 95, 98 e Me.")
 os.system("git clone https://github.com/koppyy/Moon-DoS")
 os.system("python tool-kit.py")
elif opçao == 9:
 os.system("termux-open https://github.com/maelorr")
elif opçao == 10:
 os.system("termux-open t.me/acervoteam404")
elif opçao == 11:
 os.system("exit")
else:
 print("Essa nao é uma opção disponivel, reiniciando script")
 os.system("python tool-kit.py")
