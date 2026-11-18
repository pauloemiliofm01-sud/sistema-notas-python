def registrar_vendas(limite_meta):
    vendas = []
    total_acumulado = 0.0  
   
    while total_acumulado < limite_meta:
        valor = float(input("Digite o valor da venda: R$ "))

        if valor > 0:
           vendas.append(valor)
           total_acumulado += valor 

        else: 
            print("Valor inválido! Digite um valor maior que zero.")

    return vendas

def analisar_vendas(lista_vendas):
    soma = 0.0 
    vendas_altas = 0
    vendas_baixas = 0

    print("\n--- Vendas Registradas ---")

    for indice, venda in enumerate(lista_vendas, start=1):
        print(f"Operação {indice}: R$ {venda:.2f}")
        soma += venda

        if venda >= 100.0: 
            vendas_altas += 1

        else: 
            vendas_baixas += 1 

    media = soma / len(lista_vendas)
    return (soma, media, vendas_altas)

def definir_status_dia(total_faturado, meta_esperada):  

    if total_faturado >= meta_esperada * 1.20: 
        return "Superávit Excelente (Bônus para a Equipe)"

    elif total_faturado >= meta_esperada: 
        return "Meta Atingida com Sucesso"

    else:
        return "Meta Não Atingida (abaixo do esperado)"

if __name__ == "__main__": 
    print("=== SISTEMA DE CONTROLE DE VENDAS ===")
    meta = float(input("Digite a meta diária de vendas: R$ "))

    # Passo 1 (Questão 4): Registra vendas até atingir a meta
    lista_de_vendas = registrar_vendas(meta)

    # Passo 2 (Questão 5): Analisa a lista e desempacota a tupla retornada
    total_faturado, ticket_medio, qtd_vendas_altas = analisar_vendas(lista_de_vendas)

    # Passo 3 (Questão 6): Classifica o desempenho do dia
    status_dia = definir_status_dia(total_faturado, meta)

    # Exibição do relatório final
    print("\n=== RELATÓRIO DE PERFORMANCE DIÁRIA ===")
    print(f"Meta Estipulada: R$ {meta:.2f}")
    print(f"Total Faturado: R$ {total_faturado:.2f}")
    print(f"Ticket Médio: R$ {ticket_medio:.2f}")
    print(f"Vendas a partir de R$ 100,00: {qtd_vendas_altas}")
    print(f"Status do Dia: {status_dia}")