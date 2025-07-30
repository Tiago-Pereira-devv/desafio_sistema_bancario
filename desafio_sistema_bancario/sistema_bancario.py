import textwrap

print("\nSeja Bem-Vindo ao sistema bancário DIO by Tiago-Pereira-devv")

def menu():
    menu = f"""\n
------------SELECIONE UMA OPÇÃO-------------
[1]\tDEPOSITAR
[2]\tSACAR
[3]\tEXTRATO
[4]\tCADASTRAR USUÁRIO
[5]\tLISTAR USUÁRIOS
[0]\tSAIR
-> """
    return int(input(textwrap.dedent(menu)))

def deposito(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        print(f"\n=== Depósito no valor de: R${valor: .2f} efetuado com sucesso! ===")
        extrato += f"|ENTRADA| no valor de: R${valor:>9.2f}\n"
        return saldo, extrato
    
    else:
        print("\n*** FALHA NA OPERAÇÃO. DIGITE UM VALOR VÁLIDO PARA DEPÓSITO! ***")
              
def saque(*, saldo, valor, extrato, limite, numero_saque, LIMITE_SAQUE):
        
        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saque = numero_saque >= LIMITE_SAQUE
        
        if excedeu_saldo:
            print("\n*** FALHA NA OPERAÇÃO. CONTA SEM SALDO, VERIFIQUE O SEU EXTRATO ***")
            
        elif excedeu_limite:
            print(f"\n*** FALHA NA OPERAÇÃO. CONTA NÃO AUTORIZADA PARA SAQUE INDIVIDUAL MAIOR QUE R$:{limite: .2f} ***")
        
        elif excedeu_saque:
            print(f"\n*** FALHA NA OPERAÇÃO. CONTA NÃO AUTORIZADA PARA MAIS DE 3 SAQUES POR DIA ***")
        
        elif valor > 0:
            numero_saque += 1
            extrato += f"|SAÍDA| no valor de: R${valor:>11.2f}\n"  
            saldo -= valor
            print(f"\n=== Saque de R${valor: .2f} feito com sucesso! ===") 
                   
        else:
            print("\n*** FALHA NA OPERAÇÃO. INSIRA UM SALDO VÁLIDO PARA SAQUE ***")
            
        return saldo, extrato, numero_saque 

def exibir_extrato(saldo,/, *, extrato):            
        print("============= EXTRATO =============")
        print("Nenhuma movimentação realizada." if not extrato else extrato)
        print(f"SALDO ATUAL: R${saldo: .2f}")
        print("===================================")

def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None
      
def criar_usuario(usuarios): 
    cpf = int(input("Informe o CPF do novo usuário: "))
    usuario = filtrar_usuario(cpf, usuarios)
    
    if usuario:
        print("===\n Já existe usuário cadastrado com este CPF ===")
        return
    nome = input("Digite seu nome: ")
    data_nascimento = input("Informe sua data de nascimento: ")
    
    usuarios.append({"cpf":cpf, "nome":nome, "data_nascimento":data_nascimento})
    
    print("=== Usuário cadastrado com sucesso ===")

def listar_usuarios(usuarios):
    if not usuarios:
        print("Nenhum usuário cadastrado.")
        return

    print("=" * 30)
    for usuario in usuarios:
        linha = f"""\
CPF:\t\t{usuario['cpf']}
Nome:\t\t{usuario['nome']}
Data Nasc.:\t{usuario['data_nascimento']}
"""
        print(textwrap.dedent(linha))
        print("-" * 30)

              
def main():

    LIMITE_SAQUE = 3  
      
    saldo = 0
    extrato = ""
    limite = 500
    numero_saque = 0
    usuarios = []

    while True: #inicia laço após apresentação do menu
        opcao = menu()
        
        if opcao == 1:
            valor = float(input("Informe o valor para depósito: "))

            saldo, extrato = deposito(saldo, valor, extrato)
        
        elif opcao == 2:
            valor = float(input("Informe o valor que deseja sacar: ")) 
            saldo, extrato, numero_saque = saque(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=limite,
                numero_saque=numero_saque,
                LIMITE_SAQUE = LIMITE_SAQUE                  
            )
        
        elif opcao == 3:
            exibir_extrato(saldo, extrato=extrato)
        
        elif opcao == 4:
            criar_usuario(usuarios)
        
        elif opcao == 5:
           listar_usuarios(usuarios)
            
        elif opcao == 0:
            break
        
        else:
            print("\n*** OPÇÃO INVÁLIDA ***")    
main()