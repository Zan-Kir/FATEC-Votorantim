ano_nasc = int(input("Digite seu ano de Nascimento: "))
ano_atual = int(input("Digite ano atual: "))
idade = ano_atual - ano_nasc
idade_mes = idade * 12
idade_dias = idade * 365
idade_sem = idade * 53
print(f"Sua idade em anos é de {idade} anos.")
print(f"Sua idade em meses é de {idade_mes} meses.")
print(f"Sua idade em semanas é de {idade_sem} semanas.")
print(f"Sua idade em dias é de {idade_dias} dias.")
