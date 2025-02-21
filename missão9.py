# Calculando Dobro de um Número 🛠️
# Os alunos precisam de um programa que ajude em cálculos rápidos. 
# Sua tarefa é criar uma função que receba um número e retorne o dobro do seu valor.
# ➡️ Exemplo: dobro(5)
# ➡️ Saída: "O dobro de 5 é 10"

numero = float(input('Insira o número que você deseja saber o dobro: '))

def calculo_rapido():
        print(f'O dobro de {numero} é {numero * 2}.')
calculo_rapido()

deseja_continuar = input('Deseja saber o dobro de outro número? [S/N]: ')

while deseja_continuar == 'S' or deseja_continuar == 's':
    numero = float(input('Insira o número que você deseja saber o dobro: '))
    print(f'O dobro de {numero} é {numero * 2}.')
    deseja_continuar = input('Deseja saber o dobro de outro número? [S/N]: ')

print('Até a próxima!! 💖')