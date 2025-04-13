# Sócio do Clube Delta OU ela tiver mais de 60 = 10,00
# Sócio do Clube Delta + Aniversariante daquele dia =  5,00
# Compra > 100,00
socio = 0
maior = 0
aniv = 0

valor = float(input("Digite o valor da compra: "))
if(valor >= 100.00):
    socio = int(input("Digite 1 se você for socio do Clube Delta ou 0 se não: "))
    maior = int(input("Digite 1 se você for 60+ ou 0 se não: "))
    aniv = int(input("Digite 1 se hoje for seu aniversario ou 0 se não "))

if(valor < 100):
    valor = valor
elif ((socio == 1) and (aniv == 1)):
    valor = valor - 15.00
elif ((socio == 1) and (aniv == 0)) or (maior == 1):
   valor = valor - 10.00  
else:
   valor = valor   

print(f"Valor total da compra: R$ {valor}")