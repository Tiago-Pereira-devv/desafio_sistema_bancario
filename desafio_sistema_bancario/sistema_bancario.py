import textwrap

print("\nSeja Bem-Vindo ao sistema bancário DIO by Tiago-Pereira-devv")

def menu():
    menu = f"""\n
------------SELECIONE UMA OPÇÃO-------------
[1]\tDEPOSITAR
[2]\tSACAR
[3]\tEXTRATO
[4]\tNOVA CONTA
[5]\tLISTAR CONTAS
[6]\tNOVO USUÁRIO 
[7]\tSAIR
-> """
    return input(textwrap.dedent(menu))

def deposito(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        print(f"\n=== Depósito no valor de: R${valor: .2f} efetuado com sucesso! ===")
        extrato += f"|ENTRADA| no valor de: R${valor:>9.2f}\n"
    else:
        print("\n*** FALHA NA OPERAÇÃO. DIGITE UM VALOR VÁLIDO PARA DEPÓSITO! ***")
        return saldo, extrato
        
def saque(*, saldo, valor, extrato, limite, numero_saque, LIMITE_SAQUE, ):    
        saque = float(input("Informe o valor do Saque:\nR$ "))   
        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saque = numero_saque >= LIMITE_SAQUE
        
        if excedeu_saldo:
            print("\n*** FALHA NA OPERAÇÃO. CONTA SEM SALDO, VERIFIQUE O SEU EXTRATO ***")
            
        elif excedeu_limite:
            print(f"\n*** FALHA NA OPERAÇÃO. CONTA NÃO AUTORIZADA PARA SAQUE INDIVIDUAL MAIOR QUE R$:{limite: .2f} ***")
        
        elif excedeu_saque:
            print(f"\n*** FALHA NA OPERAÇÃO. CONTA NÃO AUTORIZADA PARA MAIS DE 3 SAQUES POR DIA ***")
        
        elif saque > 0:
            numero_saque += 1
            extrato += f"|SAÍDA| no valor de: R${saque:>11.2f}\n"  
            saldo -= saque
            print(f"\n=== Saque de R${saque: .2f} feito com sucesso! ===") 
            
        else:
            print("\n*** FALHA NA OPERAÇÃO. INSIRA UM SALDO VÁLIDO PARA SAQUE ***")
            
            return saldo, extrato

def exibir_extrato(saldo,/, *, extrato):            
        print("============= EXTRATO =============")
        print("Nenhuma movimentação realizada." if not extrato else extrato)
        print(f" SALDO ATUAL: R${saldo: .2f}")
        print("===================================")
    
    #elif opcao == "0": #encerra o programa com quebra do laço
     #   print("...PROGRAMA ENCERRADO PELO USUÁRIO")
      #  break
    
   # else: #retorna erro caso opção do usuário seja diferente de 1,2,3 ou 0.
    #    print(erro_opcao)  
 
 
 
       
def main():
    extrato = ""

saldo = 0

limite = 500

limite_saque = 3

numero_saque = 0

while True: #inicia laço após apresentação do menu
    opcao = int(input(menu))
    
    if opcao == 1:
        valor = input()

main()