# Contando Letras 🔄
# O sistema precisa contar quantas letras há em um nome.
# ➡️ Crie uma função que receba um nome e diga quantas letras esse nome tem.
# ➡️ Exemplo: contar_letras("Ana")
# ➡️ Saída:" O nome Ana tem 3 letras"

print('Contador de Letras')

nome = input('Insira o nome que você quer saber quantas letras tem: ')

def contador():
    print(f'O nome {nome} tem {len(nome)} letras')

contador()

print('· · ────── ꒰ঌ·✦·໒꒱ ────── · ·') # Divisória

deseja_continuar = input('Deseja saber quantas letras tem outro nome? [S/N]: ')

while deseja_continuar == 'S' or deseja_continuar == 's':
    nome = input('Insira o nome que você quer saber quantas letras tem: ')
    print(f'O nome {nome} tem {len(nome)} letras')
    print('· · ────── ꒰ঌ·✦·໒꒱ ────── · ·') 
    deseja_continuar = input('Deseja saber quantas letras tem outro nome? [S/N]: ')

print('Até a próxima! 💖')