from datetime import datetime

def calcular_idade(ano_nascimento):
    ano_atual = datetime.now().year
    return ano_atual - ano_nascimento

def calcular_ano_aposentadoria(ano_nascimento):
    idade_atual = calcular_idade(ano_nascimento)
    idade_aposentadoria = 65
    anos_para_aposentadoria = idade_aposentadoria - idade_atual
    ano_aposentadoria = datetime.now().year + anos_para_aposentadoria
    return ano_aposentadoria

def obter_numero_positivo(prompt):
    while True:
        try:
            valor = int(input(prompt))
            if valor >= 0:
                return valor
            print("Número inválido. Deve ser um número inteiro não negativo.")
        except ValueError:
            print("Entrada inválida. Por favor, insira um número inteiro.")

def obter_float(prompt):
    while True:
        try:
            valor = float(input(prompt))
            return valor
        except ValueError:
            print("Entrada inválida. Por favor, insira um valor numérico.")

def main():
    print("Cadastro de Pessoa")

    nome = input("Digite o nome: ").strip()
    ano_nascimento = obter_numero_positivo("Digite o ano de nascimento: ")
    carteira_trabalho = obter_numero_positivo("Digite o número da carteira de trabalho (0 se não tiver): ")

    pessoa = {
        'Nome': nome,
        'Ano de Nascimento': ano_nascimento,
        'Idade': calcular_idade(ano_nascimento)
    }

    if carteira_trabalho != 0:
        ano_contratacao = obter_numero_positivo("Digite o ano de contratação: ")
        salario = obter_float("Digite o salário: R$ ")
        pessoa.update({
            'CTPS': carteira_trabalho,
            'Ano de Contratação': ano_contratacao,
            'Salário': salario
        })

    pessoa['Ano de Aposentadoria'] = calcular_ano_aposentadoria(ano_nascimento)

    print("\nDados Cadastrados:")
    for chave, valor in pessoa.items():
        print(f"{chave}: {valor}")

if __name__ == "__main__":
    main()
