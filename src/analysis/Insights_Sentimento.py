# 1. IMPORTAÇÃO DE BIBLIOTECA
# Biblioteca padrão para operações aleatórias (essencial para amostragem)
import random


def extrair_reviews_por_categoria(df, categoria, n=10):
    """
    Função de Amostragem Aleatória de Comentários.

    Objetivo: Selecionar uma amostra representativa de feedbacks de clientes 
    para uma categoria específica, evitando sobrecarregar o processamento.
    """

    # 2. FILTRAGEM (SUBSET)
    # Filtra o DataFrame original para conter apenas produtos da categoria escolhida
    subset = df[df["categoria_principal"] == categoria]

    # 3. EXTRAÇÃO E LIMPEZA
    # Seleciona a coluna de conteúdo das avaliações, remove valores nulos (NaN)
    # e converte o resultado em uma lista simples de textos
    reviews = subset["conteudo_avaliacao"].dropna().tolist()

    # 4. VALIDAÇÃO DE SEGURANÇA
    # Se a categoria não tiver nenhum comentário, retorna uma lista vazia para evitar erro
    if len(reviews) == 0:
        return []

    # 5. AMOSTRAGEM ALEATÓRIA (RANDOM SAMPLE)
    # Seleciona 'n' comentários de forma aleatória da lista.
    # O uso do 'min(n, len(reviews))' garante que, se pedirmos 10 reviews
    # mas a categoria só tiver 3, o código não quebre e retorne os 3 disponíveis.
    return random.sample(reviews, min(n, len(reviews)))
