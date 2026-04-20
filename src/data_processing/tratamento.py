# 1. IMPORTAÇÃO DE BIBLIOTECAS
# Ferramenta essencial para manipulação de tabelas (DataFrames)
import pandas as pd


def tratar_categoria(df):
    """
    Função especializada em organizar a hierarquia de categorias.
    No dataset da Amazon, as categorias vêm grudadas por um separador '|'.
    Exemplo: 'Eletrônicos|Acessórios|Cabos'
    """

    # Cria a 'categoria_principal' pegando apenas o que vem antes do primeiro '|'
    # .str.split("|").str[0] -> Divide o texto e seleciona a primeira parte
    # .str.replace("&", "_") -> Limpa caracteres especiais que podem causar erro em APIs
    df["categoria_principal"] = (
        df["categoria"]
        .str.split("|").str[0]
        .str.replace("&", "_", regex=False)
    )

    # Cria a 'subcategoria' pegando a segunda parte após o primeiro '|'
    df["subcategoria"] = (
        df["categoria"]
        .str.split("|").str[1]
        .str.replace("&", "_", regex=False)
    )

    return df


def tratar_dados(df):
    """
    Função principal de limpeza de tipos e renomeação.
    Transforma strings de moeda/porcentagem em números reais (float).
    """

    # .copy() garante que não estamos alterando o arquivo original na memória, mas sim uma cópia
    df = df.copy()

    # 2. PADRONIZAÇÃO DE NOMES (RENOMEAR)
    # Traduz os nomes das colunas de Inglês para Português para facilitar o código
    df = df.rename(columns={
        "product_name": "nome_produto",
        "brand": "marca",
        "discounted_price": "preco_desconto",
        "actual_price": "preco_original",
        "discount_percentage": "porcentagem_desconto",
        "rating": "avaliacao",
        "rating_count": "quantidade_avaliacoes",
        "category": "categoria",
        "sub_category": "sub_categoria",
        "product_url": "url_produto",
        "image_url": "url_imagem",
        "description": "descricao",
        "product_id": "id_produto",
        "about_product": "sobre_produto",
        "user_id": "id_usuario",
        "user_name": "nome_usuario",
        "review_id": "id_avaliacao",
        "review_title": "titulo_avaliacao",
        "review_content": "conteudo_avaliacao",
        "img_link": "link_imagem",
        "product_link": "link_produto"})

    # 3. REMOÇÃO DE VALORES INVÁLIDOS
    # Remove linhas que não possuem dados essenciais (preço ou nota)
    df = df.dropna(subset=["avaliacao", "preco_desconto", "preco_original"])

    # 4. LIMPEZA DE PREÇOS (REGEX)
    # Os preços vêm como 'R$ 1.200,00'. Precisamos remover tudo que não é número ou ponto.
    # [^\d.] significa: "Mantenha apenas dígitos (\d) e pontos (.)"
    df["preco_desconto"] = (
        df["preco_desconto"]
        .astype(str)
        .str.replace(r"[^\d.]", "", regex=True)
        .astype(float)
    )

    df["preco_original"] = (
        df["preco_original"]
        .astype(str)
        .str.replace(r"[^\d.]", "", regex=True)
        .astype(float)
    )

    # 5. LIMPEZA DE PERCENTUAL
    # Remove o símbolo '%' para que o 50% vire apenas o número 50.0
    df["porcentagem_desconto"] = (
        df["porcentagem_desconto"]
        .astype(str)
        .str.replace("%", "", regex=True)
        .astype(float)
    )

    # 6. CONVERSÃO DE NOTAS (RATING)
    # pd.to_numeric com errors="coerce" transforma qualquer texto inválido em NaN (nulo)
    df["avaliacao"] = pd.to_numeric(df["avaliacao"], errors="coerce")

    # 7. LIMPEZA DE QUANTIDADE DE AVALIAÇÕES
    # Remove vírgulas de números grandes (ex: 1,200 vira 1200)
    df["quantidade_avaliacoes"] = (
        df["quantidade_avaliacoes"]
        .astype(str)
        .str.replace(",", "")
        .astype(float)
    )

    return df
