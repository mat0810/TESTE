#teste inicial: media de 3 notas

#Etapa1: Coletar as 3 notas
#Etapa2: Calcular a média
#Etapa3: Exibir a média e a mensagem de acordo com a média

#Etapa1: Coletar as 3 notas:
    ##Exibir a mensagem "Digite a primeira nota: "
    ##Ler e salvar a nota digitada pelo usuário
    ##Exibir a mensagem "Digite a segunda nota: "
    ##Ler e salvar a nota digitada pelo usuário
    ##Exibir a mensagem "Digite a terceira nota: "
    ##Ler e salvar a nota digitada pelo usuário
        ###Cada nota pode ser um número inteiro ou um número decimal entre 0 e 8

#Etapa2: Calcular a média:
    ##Calcular a média das 3 notas: (nota1 + nota2 + nota3) / 3

#Etapa3: Exibir a média:
    ##Exibir a mensagem "A média das notas é: " + média

#Atenção:
    ##A média deve ser exibida com 2 casas decimais, um número inteiro e um número decimal entre 0 e 8
    ##Se houver algum erro, corrija-o sem quebrar o código
    ##Sempre que for ler uma nota, deve-se verificar se o valor digitado é um número válido (inteiro ou decimal) e entre 0 e 8
        ###Se o valor digitado não for um número válido, deve-se exibir a mensagem "Valor inválido. Digite uma nota entre 0 e 8." e solicitar o valor novamente
        ###Se o valor digitado não for um número, deve-se exibir a mensagem "Valor inválido. Digite uma nota entre 0 e 8." e solicitar o valor novamente

    ##Para cada valor de media, deve-se escrever uma mensagem de acordo com a média:
        ###Se >5.6: "Aprovado! Parabéns!"
        ###Se <5.6: "Reprovado. Estude mais!"
        ###Se 5.6: "Aprovado! Mas, foi por pouco, hein..."

#Código:
def ler_nota(mensagem):
    while True:
        valor = input(mensagem)
        try:
            nota = float(valor.replace(',', '.'))
            if 0 <= nota <= 8:
                return nota
            else:
                print("Valor inválido. Digite uma nota entre 0 e 8.")
        except ValueError:
            print("Valor inválido. Digite uma nota entre 0 e 8.")

# Etapa1: Coletar as 3 notas
nota1 = ler_nota("Digite a primeira nota: ")
nota2 = ler_nota("Digite a segunda nota: ")
nota3 = ler_nota("Digite a terceira nota: ")

# Etapa2: Calcular a média
media = (nota1 + nota2 + nota3) / 3

# Etapa3: Exibir a média e a mensagem de acordo com a média
print(f"A média das notas é: {media:.2f}")

if media > 5.6:
    print("Aprovado! Parabéns!")
elif media < 5.6:
    print("Reprovado. Estude mais!")
else:  # media == 5.6
    print("Aprovado! Mas, foi por pouco, hein...")
