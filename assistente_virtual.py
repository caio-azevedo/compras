import time
import math

Uni = ["", "primeiro", "segundo", "terceiro", "quarto", "quinto", "sexto", "setimo", "oitavo", "nono"];
Dec = ["", "decimo", "vigesimo", "trigesimo", "quadragesimo", "quinquagesimo", "sexagesimo", "septuagesimo", "octagesimo", "nonagesimo"];
Cen = ["", "centesimo", "ducentesimo", "tricentesimo", "quadringentesimo", "quingentesimo", "sexcentesimo", "septingentesimo", "octingentesimo", "nongentesimo"];  

nome=input("Olá, qual é o seu nome?\n")
print("\n")
print(f"{nome}, aqui é o assistente para a elaboração de pregão!")
resposta=input("Podemos começar? Responda Sim ou Não.\n")

if resposta=="Sim":        
    item=int(input("Qual o número do item pesquisado?\n"))
    unidade = item % 10
    dezena = int(math.floor(item/10))% 10
    centena = int(math.floor(item/10))
    if item >= 100:
        i = Cen[centena] + Dec[dezena] + Uni[unidade]
    else:
        if item >= 10:
            i = Dec[dezena] + Uni[unidade]
        else:
            i = Uni[item]
    
    f1=3*(item-1)+1
    f2=f1+1
    f3=f1+2
    nomeitem=(input('Digite o nome do item.\n'))
    cot=int(input("Quantas cotações em sítios eletrônicos você fez para este item?\n"))
    print("\n")
    pp=input("Você realizou a cotação deste item no painel de preço? Responda Sim ou Não.\n")
    print("\n")
    print("Que legal {}! Parabéns, a Universidade Federal da Paraiba agradece!".format(nome))
    print("\n")
    print("Aguarde alguns segundos enquanto vou gerar o arquivo Latex para você!")
    print("\n")
    time.sleep(5)
    with open("Tex/item{}.txt".format(item), "w") as stream:
        if cot==1 and pp=="Sim":
           print('\def \%sitem{%s}\n\includepdf[pages=1,pagecommand=\chapter{\%sitem}, offset=0 -2cm]{Figuras/fig%d}\n\includepdf[pages=1]{Figuras/pp%d}'%(i,nomeitem,i,f1,item),file=stream)
        if cot==2 and pp=="Sim":
           print('\def \%sitem{%s}\n\includepdf[pages=1,pagecommand=\chapter{\%sitem}, offset=0 -2cm]{Figuras/fig%d}\n\includepdf[pages=1]{Figuras/fig%d}\n\includepdf[pages=1]{Figuras/pp%d}'%(i,nomeitem,i,f1,f2,item),file=stream)
        if cot==3 and pp=="Sim":
           print('\def \%sitem{%s}\n\includepdf[pages=1,pagecommand=\chapter{\%sitem}, offset=0 -2cm]{Figuras/fig%d}\n\includepdf[pages=1]{Figuras/fig%d}\n\includepdf[pages=1]{Figuras/fig%d}\n\includepdf[pages=1]{Figuras/pp%d}'%(i,nomeitem,i,f1,f2,f3,item),file=stream)
        if cot==1 and pp=="Não":
           print('\def \%sitem{%s}\n\includepdf[pages=1,pagecommand=\chapter{\%sitem}, offset=0 -2cm]{Figuras/fig%d}'%(i,nomeitem,i,f1),file=stream)
        if cot==2 and pp=="Não":
           print('\def \%sitem{%s}\n\includepdf[pages=1,pagecommand=\chapter{\%sitem}, offset=0 -2cm]{Figuras/fig%d}\n\includepdf[pages=1]{Figuras/fig%d}'%(i,nomeitem,i,f1,f2),file=stream)
        if cot==3 and pp=="Não":
           print('\def \%sitem{%s}\n\includepdf[pages=1,pagecommand=\chapter{\%sitem}, offset=0 -2cm]{Figuras/fig%d}\n\includepdf[pages=1]{Figuras/fig%d}\n\includepdf[pages=1]{Figuras/fig%d}'%(i,nomeitem,i,f1,f2,f3),file=stream)

else:
    print("Ok então, obrigado vamos encerrar o programa, até a próxima!")
    exit()
print("")
resposta2=input("Você pesquisou mais algum item? Responda Sim ou Não.\n")
if resposta2=="Não":
    print("Ok então, obrigado vamos encerrar o programa, até a próxima!")
    exit()
if resposta2=="Sim":        
    exec(open("Auxiliar/auxiliar.py",encoding='utf8').read())

