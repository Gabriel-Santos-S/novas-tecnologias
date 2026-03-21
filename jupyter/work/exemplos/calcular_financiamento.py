

def calcular_financiamento(preco: float, entrada: float, parcelas: int) -> float:
    valor_financiado = preco - entrada

    valor_total: float = valor_financiado * (1 + 0.015 * parcelas)
    valor_parcela: float = valor_total / parcelas

    return valor_parcela