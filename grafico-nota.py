#importando biblioteca
import matplotlib.pyplot as plt

#lista com o nome de 10 alunos.
nomes_alunos = [
    "Alice", "Bob", "Carlos", "Diana", "Eduardo",
    "Fernanda", "Gabriel", "Helena", "Igor", "Juliana"
]

#um dicionário chamado notas_materias,
# Cada índice nas listas corresponde ao mesmo aluno da lista nomes_alunos.
notas_materias = {
    "matemática": [8.5, 7.0, 9.2, 6.8, 5.4, 7.6, 8.3, 9.1, 6.5, 7.9],
    "português": [7.2, 6.5, 8.0, 5.9, 6.8, 7.7, 8.1, 6.4, 7.3, 6.9],
    "história": [6.8, 7.4, 5.6, 8.2, 7.9, 6.3, 8.5, 7.1, 6.7, 5.8],
    "geografia": [8.3, 7.8, 6.5, 8.9, 7.4, 8.0, 7.2, 6.9, 8.1, 7.6],
    "ciências": [5.9, 6.8, 7.3, 6.1, 7.0, 5.6, 6.9, 7.4, 6.2, 5.8]
}

#média de cada matéria.
#definindo a função chamada calculador_media que recebe uma lista de notas como entrada.
def calculador_media(notas):
    return sum(notas) / len(notas)

#definindo função para imprimir gráfico das notas de uma matéria específica.
def imprimir_grafico_notas_materia(materia):
    if materia in notas_materias:
        notas = notas_materias[materia]
        plt.bar(nomes_alunos, notas, color='green')
        plt.title(f"Notas dos alunos em {materia}")
        plt.xlabel("Alunos")
        plt.ylabel("Notas")
        plt.xticks(rotation=45)  #rotaciona os nomes para facilitar a leitura
        plt.show()
    else:
        print("Matéria não encontrada.")

#definindo função para imprimir os nomes dos alunos.
def imprimir_nomes_alunos():
    print("Lista de alunos:")
    for nome in nomes_alunos:
        print(nome)

#função para calcular e exibir a média de todas as matérias.
def imprimir_media_materias():
    medias = {} #dicionário para armazenar a média de cada matéria.
   
   #calcula a média de cada matéria e armazena no dicionário 'medias'.
    for materia, notas in notas_materias.items():
        medias[materia] = calculador_media(notas)

   #ordena as matérias pela média, do maior para o menor.
    medias_ordenadas = dict(sorted(medias.items(), key=lambda item: item[1], reverse=True))

    #cria e exibe um gráfico de barras com as médias das matérias.
    plt.bar(medias_ordenadas.keys(), medias_ordenadas.values(), color='blue') #color: define  cor do gráfico.
    #key: obtém as chaves do dicionário. values: obtém os valores do dicionário.
    plt.title("Média das Matérias")
    plt.xlabel("Matéria") #rótulo do eixo X.
    plt.ylabel("Média")  #rótulo do eixo Y.
    plt.show() #exibe o gráfico.

#função que exibe o menu e permite ao usuário escolher uma opção.
def menu():
    while True:
        print("""
Bem Vindo ao Mgre (Mostra Gráfica de Dados Escolares)
Matérias que temos dados:
- matemática
- português
- ciências
- história
- geografia
""")
        print("Escolha uma opção:")
        print("1. Ver média das matérias")
        print("2. Ver notas dos alunos em uma matéria específica")
        print("3. Ver as notas de uma matéria")
        print("4. Ver lista de nomes dos alunos")
        print("0. Sair")
       
        escolha = input("Digite o número da opção desejada: ")
       
        if escolha == "1":
            imprimir_media_materias()
        elif escolha == "2":
            materia = input("Digite o nome da matéria: ")
            imprimir_grafico_notas_materia(materia)
        elif escolha == "3":
            imprimir_nomes_alunos()
        elif escolha == "0":
            print("Saindo do programa...")
            break
        else:
            print("Opção inválida. Tente novamente.")

#executando o menu
menu()
