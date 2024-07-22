import os
import time
import keyboard

tecla_de_saída = ''

def calcular_valores(num01, num02, operador):
    match operador:
        case '*':
            return num01*num02
        case '/':
            return num01/num02
        case '+':
            return num01+num02
        case '-':
            return num01-num02
        case _:
            return mensagem_erro('Operador inexistente.', 2)

def desenhar_tela_superior(titulo=str,preenchimento=chr):
    titulo_da_tela = f'{preenchimento} {titulo} {preenchimento} '
    preenchimentos = preenchimento * len(titulo_da_tela)

    print(preenchimentos)
    print(titulo_da_tela)
    print(preenchimentos)




def area_de_calculo():
    try:
        num01 = int(input('Digite o Primeiro Número: '))
        num02 = int(input('Digite o Segundo Número: '))
        operador = input('Digite o Operador para Calculo: ')

    except:
        mensagem_erro('Erro ao receber valores. Recomeçando em 3 Segundos....',3)

    os.system('cls')
    print(f'{num01} {operador} {num02} = {calcular_valores(num01,num02,operador)}\n')
    reiniciar_calculadora()

def mensagem_erro(mensagem=str,tempo=int):
        os.system('cls')
        print(f'{mensagem}\n\n')
        time.sleep(tempo)
        os.system('cls')
        main()

def reiniciar_calculadora():
    opcao = input('\nDeseja fazer um novo calculo? (S/N): ')
    match opcao.lower():
        case 's':
            print(opcao)
            calculadora()
        case 'n':
            quit()
        case _:
            mensagem_erro('NaN',1)

def menu_iniciar():
    tentativas = 0

    os.system('cls')
    desenhar_tela_superior('Super Calculadora Quantica', '-')
    print('Selecione uma das Opções Abaixo: \n')

    print('1-Inciar')
    print('2-Sair')
    try:
        opcao = int(input('\n_ '))
    except:
        mensagem_erro('Deu RUIM',1)


        if tentativas > 1:
            print('Calma Caraio. Sem Ansiedade.')

    match opcao:
        case 1:
            calculadora()

        case 2:
            quit()

def calculadora():
    os.system('cls')
    desenhar_tela_superior('Super Calculadora Quantica', '-')
    area_de_calculo()

def main():
        menu_iniciar()



if __name__ == '__main__':
    main()

