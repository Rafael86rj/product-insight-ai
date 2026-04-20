# %%
# Marcador para execução em células no VS Code (Interactive Window)

# %% 1. IMPORTAÇÕES DE BIBLIOTECAS E MÓDULOS
from IPython.display import display
import pandas as pd
from src.data_processing.tratamento import tratar_dados, tratar_categoria
from src.ia.ia_Insights_KPI import analisar_categorias


# NOVAS IMPORTAÇÕES: Adição das ferramentas de extração e análise de texto
from src.analysis.Insights_Sentimento import extrair_reviews_por_categoria
from src.ia.ia_reviews import analisar_reviews

# NOVA IMPORTAÇÃO: Biblioteca para manipulação de arquivos e caminhos
from src.reporting.relatorio import gerar_relatorio

# %% 2. CONFIGURAÇÃO DE VISUALIZAÇÃO
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 1000)

# %% 3. CARREGAMENTO (EXTRAÇÃO)
caminho = r"C:\Users\Rafael\Desktop\Python\Python-IA\product-insight-ai\data\amazon.csv"
df = pd.read_csv(caminho)

# %% 4. PROCESSAMENTO (TRANSFORMAÇÃO)
df = tratar_dados(df)
df = tratar_categoria(df)

# %% 5. ANÁLISE ESTATÍSTICA E DESCOBERTA DE INSIGHTS
try:
    # FILTROS ESTRATÉGICOS: Identificação de anomalias (desconto alto + nota baixa)
    resultado = df[["nome_produto", "porcentagem_desconto", "avaliacao"]].sort_values(
        by=["porcentagem_desconto", "avaliacao"], ascending=[False, True]).head(10)

    # FILTROS ESTRATÉGICOS: Identificação de oportunidades (preço baixo + nota alta)
    resultado2 = df[["nome_produto", "preco_original", "avaliacao"]].sort_values(
        by=["preco_original", "avaliacao"], ascending=[True, False]).head(10)

    # AGRUPAMENTO POR CATEGORIA: Geração de KPIs (Indicadores de Performance)

    # Média Ponderada: Mitigação de distorções causadas por poucos votos
    restultado3 = df.groupby("categoria_principal").apply(
        lambda x: (x["avaliacao"] * x["quantidade_avaliacoes"]
                   ).sum() / x["quantidade_avaliacoes"].sum()
    ).sort_values(ascending=False).round(2).rename("media_ponderada")

    # Média Simples e Contagem (Volume)
    resultado4 = df.groupby("categoria_principal")["avaliacao"].mean(
    ).sort_values(ascending=False).round(2).rename("media_simples")

    resultado5 = df["categoria_principal"].value_counts().rename(
        "qtd_produtos")

    # CONSOLIDAÇÃO: União dos KPIs em uma única tabela de performance
    resultado_final = pd.concat([restultado3, resultado4, resultado5], axis=1)

    #  6. EXIBIÇÃO DOS RESULTADOS QUANTITATIVOS
    print("Existe produto com: alto desconto + baixa avaliação?")
    display(resultado)
    print("\n"+"-"*100+"\n")

    print("Existe produto com: baixo preço + alta avaliação?")
    display(resultado2)
    print("\n"+"-"*100+"\n")

    print("Qual categoria parece ter melhor percepção?")
    display(resultado_final)

    #  7. INTEGRAÇÃO COM IA - ANÁLISE DE KPIs (NÚMEROS)

    print("\n=== INSIGHTS DA IA (KPIs) ===\n")

    # 1. Filtrar categorias relevantes
    df_categorias_validas = resultado_final[resultado_final["qtd_produtos"] >= 10]

    # 2. Converter para formato que a IA entende
    dados_para_ia = df_categorias_validas .reset_index().to_dict(orient="records")

    # 3. Gerar insights
    insights = analisar_categorias(dados_para_ia)

    print(insights)
    print(df_categorias_validas)

    # 8. INTEGRAÇÃO COM IA - ANÁLISE DE SENTIMENTO (TEXTO)
    # Novo bloco: Busca entender o "porquê" por trás dos números da melhor categoria
    print("\n=== INSIGHTS REVIEWS (SENTIMENTO) ===\n")

    # Identifica automaticamente a categoria com a melhor média ponderada
    top_categoria = resultado_final.index[0]

    # Amostragem: Extrai uma lista aleatória de textos de review desta categoria
    reviews = extrair_reviews_por_categoria(df, top_categoria)

    # IA de Sentimento: Analisa o feedback textual dos consumidores
    insights_reviews = analisar_reviews(top_categoria, reviews)

    print(insights_reviews)

    print("\n=== RELATÓRIO ===\n")
    gerar_relatorio(insights, insights_reviews)

except Exception as e:
    # Captura de erros de processamento ou de colunas inexistentes
    print(f"Erro: Coluna não encontrada - {e}")
