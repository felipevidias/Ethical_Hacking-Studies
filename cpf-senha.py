from itertools import permutations

cpf = "12345678900"

# Gerar todas as permutações dos dígitos do CPF
permutacoes = [''.join(p) for p in permutations(cpf)]

# Salvar as permutações em um arquivo txt
with open("wpa_senhas.txt", "w") as f:
    for senha in permutacoes:
        f.write(senha + "\n")

print("Arquivo wpa_senhas.txt criado com todas as possibilidades de senhas.")
