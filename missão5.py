# Recuperando o Cofre de Segurança 🔒
# O cofre da biblioteca guarda códigos raros de programação, mas o vírus resetou a senha! Agora, apenas quem souber a combinação correta poderá acessá-lo.
# Crie um programa que solicite ao usuário uma senha e verifique se ela está correta. A senha correta é "Python123".
print('SEJA BEM VINDO!')

senha_correta = 'Python123'
senha_usuario = input('Digite a sua senha: ')

while senha_usuario != senha_correta:
    print('❌ Acesso negado. Tente novamente.')
    senha_usuario = input('Digite a sua senha: ')

print('✅ Acesso Liberado!')