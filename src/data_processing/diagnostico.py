# 1. IMPORTAÇÃO DE FERRAMENTAS
import pandas as pd             # Manipulação de tabelas
import matplotlib.pyplot as plt  # Criação de gráficos estáticos
from IPython.display import display  # Renderização visual de tabelas no VS Code


def diagnosticar(df, sample_rows=5):
    """
    Função de Auditoria de Dados.
    Analisa a saúde, estatísticas e integridade do DataFrame.
    """

    # --- BLOCO 1: ESTRUTURA E INTEGRIDADE ---
    # Focado em entender o tamanho da base e se há desperdício (duplicados)
    print("#"*100)
    print("✅ 1. Estrutura da base")
    print("#"*100+"\n")
    # Dimensão da tabela (linhas, colunas)
    print('Nº de linhas e colunas:', df.shape)
    print('Nº de linhas duplicadas:', df.duplicated().sum())  # Linhas 100% iguais
    # Colunas com valores idênticos
    print('Nº de colunas duplicadas:', df.T.duplicated().sum())

    # Análise de Valores Faltantes (NaN)
    # É vital para decidir se vamos preencher ou apagar dados vazios
    print("-"*100+"\n")
    print("Nº de valores nulos por coluna:")
    display(df.isnull().sum())

    print("-"*100+"\n")
    print("% de valores faltantes:")
    # Proporção de nulos em percentual
    display((df.isnull().mean() * 100).round(2))

    # --- BLOCO 2: ESTATÍSTICAS DESCRITIVAS ---
    # Focado em entender a variação dos números e o comportamento dos textos
    print("\n"+"#"*100)
    print("✅ 2. Estatísticas descritivas")
    print("#"*100+"\n")

    print("Resumo de colunas numéricas:")
    # Mostra média, desvio padrão, valores min e max
    display(df.describe())

    print("-"*100+"\n")
    print("Resumo de colunas categóricas:")
    # Mostra a frequência de textos e quantos valores únicos existem
    display(df.describe(exclude="number"))

    # --- BLOCO 3: TIPOS E COERÊNCIA ---
    # Verifica se o Python entendeu o que é número e o que é texto (object)
    print("\n"+"#"*100)
    print("✅ 3. Tipos de dados e coerência")
    print("#"*100+"\n")

    print("Colunas numéricas:")
    display(df.select_dtypes(include="number").columns)

    print("-"*100+"\n")
    print("Colunas categóricas:")
    display(df.select_dtypes(include="object").columns)

    # --- BLOCO 4: INFORMAÇÃO TÉCNICA E AMOSTRA ---
    print("\n"+"-"*100+"\n")
    print("✅ 4. Informação do DataFrame")
    df.info()  # Mostra o uso de memória e detalhes técnicos

    print("-"*100+"\n")
    print("Amostra dos dados:")
    display(df.head(sample_rows))  # Visualização rápida das primeiras linhas

    # --- BLOCO 5: ANÁLISE VISUAL (GRÁFICOS) ---
    # Tenta gerar histogramas e boxplots para detetar Outliers (valores fora do comum)
    try:
        # Histograma: Mostra a frequência/distribuição dos números
        df.hist(figsize=(12, 8))
        plt.suptitle("Distribuição das colunas numéricas")
        plt.show()

        # Boxplot: Ótimo para identificar "pontos fora da curva" (Outliers)
        for col in df.select_dtypes(include="number").columns[:3]:
            df.boxplot(column=col)
            plt.title(f"Boxplot da coluna {col}")
            plt.show()

        # Medidas de distorção estatística
        # Verifica se os dados estão "pendidos" para um lado
        print("Assimetria (Skewness):\n", df.skew())
        # Verifica o "achatamento" da distribuição
        print("Curtose (Kurtosis):\n", df.kurtosis())

    except Exception as e:
        # Garante que o script não pare se o gráfico falhar
        print("Erro ao gerar gráficos:", e)
