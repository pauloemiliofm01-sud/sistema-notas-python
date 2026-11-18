def coletar_notas(qtd_notas):
    #Lista vazia para armazenar as notas coletadas
    notas = []
    contador = 1
    # Laço de repetição WHILE para contralar o preccesso de coleta das notas
    while contador <= qtd_notas:
        nota = float(input(f"Digite a nota {contador}: nota (0 a 10) "))

        #Condional (IF/ELSE) validando o intervalo Permitido
        if 0.0 <= nota <= 10.0:
            notas.append(nota) #Inserido o item na lista
            contador += 1 # Incrementa o contador apenas se a nota for válida
        else:
            print("Nota inválidas! Digite um valor entre 0 e 10.")
    return notas  # Retorna a lista preenchida

def calcular_media(lista_notas):
    soma = 0.0

    print("\n--- Notas Registradas ---")

    for indice, nota in enumerate(lista_notas, start=1):
        print(f"Nota {indice}: {nota:.1f}")
        soma += nota

    media = soma / len(lista_notas)
    return media


def determinar_situacao(media):
    if media >= 7.0:
        return "Aprovado"
    elif media >= 5.0:
        return "Em Recuperação"
    else:
        return "Reprovado"


if __name__ == "__main__":
    print("=== SISTEMA DE NOTAS ESCOLARES ===")

    notas_aluno = coletar_notas(3)

    media_aluno = calcular_media(notas_aluno)

    situacao_final = determinar_situacao(media_aluno)

    print("\n=== BOLETIM FINAL ===")
    print(f"Média Final: {media_aluno:.2f}")
    print(f"Status do Aluno: {situacao_final}")