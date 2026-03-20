# -----------------------------
# 4. VALIDAÇÃO DE ALFABETO
# -----------------------------

def validar_alfabeto(alfabeto, frase):
    """
    Verifica se todos os caracteres da frase
    pertencem ao alfabeto informado.
    """

    # transforma frase em conjunto de caracteres
    caracteres_frase = set(frase)

    # remove espaços (opcional)
    caracteres_frase.discard(" ")

    # verifica se é subconjunto
    return caracteres_frase.issubset(alfabeto)


# Exemplo de alfabeto (binário)
alfabeto_binario = {"0", "1"}

string1 = "10101"
string2 = "10102"

print("String 1 válida?",
      validar_alfabeto(alfabeto_binario, string1))

print("String 2 válida?",
      validar_alfabeto(alfabeto_binario, string2))
