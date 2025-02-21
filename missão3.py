# Recuperando o Sistema de Notas 📊
# As classificações das provas desapareceram! Agora os alunos não sabem se tiraram um não sabem se tiraram um A, B, C, D ou F . Antes que o pânico se espalhe, sua tarefa é criar um programa que peça a nota do aluno e imprima sua classificação conforme a escala:

nota = float(input('Insira sua nota: '))

if nota >= 90 and nota <= 100:
    print('Parabéns, você tirou A!')
elif nota >= 80 and nota <= 89:
    print('Muito bem, você tirou B')
elif nota >= 70 and nota <= 79:
    print('Bom trabalho, você tirou C')
elif nota >= 60 and nota <= 69:
    print('Fique atento, você tirou D')
elif nota < 60:
    print('Estude um pouco mais, você tirou F')
else:
    print('Resposta inválida')