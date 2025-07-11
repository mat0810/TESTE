#teste inicial: media de 3 notas

#Etapa1: Coletar as 3 notas
#Etapa2: Calcular a média
#Etapa3: Exibir a média

#Etapa1: Coletar as 3 notas:
    ##Exibir a mensagem "Digite a primeira nota: "
    ##Ler e salvar a nota digitada pelo usuário
    ##Exibir a mensagem "Digite a segunda nota: "
    ##Ler e salvar a nota digitada pelo usuário
    ##Exibir a mensagem "Digite a terceira nota: "
    ##Ler e salvar a nota digitada pelo usuário

#Etapa2: Calcular a média:
    ##Calcular a média das 3 notas: (nota1 + nota2 + nota3) / 3

#Etapa3: Exibir a média:
    ##Exibir a mensagem "A média das notas é: " + média

#Atenção:
    ##A média deve ser exibida com 2 casas decimais, um número inteiro e um número decimal entre 0 e 10
    ##Se houver algum erro, corrija-o sem quebrar o código
    ##Sempre que for ler uma nota, deve-se verificar se o valor digitado é um número válido e entre 0 e 10
        ###Se o valor digitado não for um número válido, deve-se exibir a mensagem "Valor inválido. Digite uma nota entre 0 e 10." e solicitar o valor novamente
        ###Se o valor digitado não for um número, deve-se exibir a mensagem "Valor inválido. Digite uma nota entre 0 e 10." e solicitar o valor novamente

    ##Para cada valor de media, deve-se escrever uma mensagem de acordo com a média:
        ###Se >7: "Aprovado! Parabéns!"
        ###Se <7: "Reprovado. Estude mais!"
        ###Se 7: "Aprovado! Mas, foi por pouco, hein..."

def ler_nota(numero):
    while True:
        try:
            valor = input(f"Digite a {numero}ª nota: ")
            nota = float(valor)
            if 0 <= nota <= 10:
                return nota
            else:
                print("Valor inválido. Digite uma nota entre 0 e 10.")
        except ValueError:
            print("Valor inválido. Digite uma nota entre 0 e 10.")

# Etapa 1: Coletar as 3 notas
nota1 = ler_nota(1)
nota2 = ler_nota(2)
nota3 = ler_nota(3)

# Etapa 2: Calcular a média
media = (nota1 + nota2 + nota3) / 3

# Etapa 3: Exibir a média
print(f"A média das notas é: {media:.2f}")

# Mensagem de acordo com a média
if media > 7:
    print("Aprovado! Parabéns!")
elif media < 7:
    print("Reprovado. Estude mais!")
else:  # media == 7
    print("Aprovado! Mas, foi por pouco, hein...")