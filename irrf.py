def verificar_obrigacao_irrf(salario_mensal):
    meses_no_ano = 12
    limite = 30639.90
    rendimentos_anuais = salario_mensal * meses_no_ano
    
    if rendimentos_anuais > limite:
        return rendimentos_anuais, "Você está obrigado a declarar o IRRF para 2024, atingiu o limite de R$ {}".format(limite)
    else:
        return rendimentos_anuais, "Você está isento de declarar o IRRF para 2024, não atingiu o limite de R$ {}".format(limite)

if __name__ == "__main__":
    # Solicitar ao usuário que informe o salário mensal
    salario_mensal = float(input("Informe o seu salário mensal: R$ "))
    
    # Calcular e obter o resultado
    rendimentos_anuais, mensagem = verificar_obrigacao_irrf(salario_mensal)
    
    # Exibir o resultado
    print(f"Rendimentos anuais: R$ {rendimentos_anuais:.2f}")
    print(mensagem)
