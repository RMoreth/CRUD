"""Crie um CRUD utilizando os conceitos de lista, tupla e dicionário. O usuário pode cadastrar quantas pessoas quiser. Os dados a serem cadastrados são:
- Nome
- CPF
- Telefone
- E-mail
- Profissão
- Empresa"""
import os
lista_perfis = []
dados = ('Nome', 'Cpf', "Telefone", "E-mail", "Profissão", "Empresa")
while True:
    print("<" * 10, "CRUD PERFIL", ">" * 10)
    print("ESCOLHA A OPERAÇÃO QUE DESEJA REALIZAR")
    print("1 - Adicionar novo perfil")
    print("2 - Mostrar todos os perfis")
    print("3 - Alterar dados do perfil")
    print("4 - Excluir Perfil")
    print("5 - SAIR DO PROGRAMA")
    r = int(input("Digite a opção desejada\n"))

    match r:
        case 1:
            while True:
                os.system("cls")
                perfil = {}
                print("<<<<<Cadastrando novo Perfil>>>>")
                for dado in dados:
                    perfil[dado] = str(input(F"Informe o valor de {dado}: "))

                lista_perfis.append(perfil)
                cont = str(
                    input("Deseja adicionar outro? [s/n]")).strip().lower()[0]
                if cont == "n":
                    os.system("cls")
                    break
                else:
                    continue
        case 2:
            os.system("cls")
            c = 0
            for perfil in lista_perfis:
                c += 1
                print("")
                print(f"Indice Perfil: {c}\n")
                for atributo in perfil:
                    print(f"{atributo}: {perfil.get(atributo)}")
                print("")

        case 3:
            os.system("cls")
            print("<<<<<Alterando Cadastro>>>>>")
            indice = int(input("Indice do perfil: "))
            if indice == 0:
                indice = 0
            else:
                indice -= 1
            os.system("cls")
            campo = input("informe o campo a ser alterado: ").capitalize()
            if campo not in dados or indice > len(lista_perfis):
                print("Campo inválido")
            else:
                try:
                    os.system("cls")
                    lista_perfis[indice][campo] = input(
                        f"Digite o novo valor para {campo}: ")
                    print(f"Perfil {indice + 1} alterado")
                except:
                    print("Não foi possível alterar")
                finally:
                    for atributo in lista_perfis[indice]:
                        print(f"{atributo}: {
                            lista_perfis[indice].get(atributo)}")
        case 4:
            os.system("cls")
            print("<<<<<EXCLUINDO Cadastro>>>>>")
            indice = int(input("Indice do perfil: "))
            if indice == 0:
                indice = 0
            else:
                indice -= 1
            print(f"EXCUINDO perfil {indice + 1}")
            for atributo in lista_perfis[indice]:
                print(f"{atributo}: {lista_perfis[indice].get(atributo)}")
            confirm = str(
                input("TEM CERTEZA QUE DESEJA EXCLUIR?[S/N]")).lower().strip()[0]
            if confirm == "s":
                del lista_perfis[indice]
                print(F"Perfil {indice}, deletado com sucesso!")
            else:
                print("Operação cancelada")

        case 5:
            break

        case _:
            print("Opção inválida")
