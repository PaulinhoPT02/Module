#-------------------------------------------------------------------------------
# Name:        module2
# Purpose:
#
# Author:      aluno
#
# Created:     24/02/2022
# Copyright:   (c) aluno 2022
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    pass

if __name__ == '__main__':
    main()



def menu():
    print("[1] Inseração de valores \n[2] Cálculo idade \n[3] Sair")
    op=str(input("Insira uma opção: "))
    while op not in["1","2","3"]:
        print("Opção incorreta! Insira nova opção.")
        print("[1] Inseração de valores \n[2] Cálculo idade \n[3] Sair")
        op=str(input("Insira uma opção: "))
    return op


