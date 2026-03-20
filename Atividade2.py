# 1. Base de dados de usuários
usuarios = {
    "Alice": {"Python", "Jogos", "Música", "IA"},
    "Bob":   {"Java", "IA", "Música", "Caminhada"},
    "Carol": {"Python", "Caminhada", "Teatro"}
}

def recomendar_conteudo(interessado, referencia):
    """
    Compara dois usuários e retorna o que o 'interessado' 
    ainda não conhece do 'referencia'.
    """
    perfil_A = usuarios.get(interessado)
    perfil_B = usuarios.get(referencia)
    
    if not perfil_A or not perfil_B:
        return "Usuário não encontrado."

    comuns = perfil_A & perfil_B
    sugestoes = perfil_B - perfil_A
    
    return comuns, sugestoes

#
