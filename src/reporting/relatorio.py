# 1. IMPORTAÇÕES
# Importamos as funções especializadas do módulo de IA.
# Agora temos uma função para olhar o mercado (KPI) e outra para o produto (Reviews).
from src.ia.ia_conclusao import gerar_conclusao_kpi, gerar_conclusao_reviews

# 1. DEFINIÇÃO DA FUNÇÃO DE EXPORTAÇÃO


def gerar_relatorio(insights_kpi, insights_reviews):
    """
    Função de Consolidação e Escrita.
    Responsável por unir análise quantitativa e qualitativa em um documento final formatado.
    """

    # 2. SÍNTESE ESTRATÉGICA (IA EM CAMADAS)
    # Aqui a IA processa os resumos anteriores para criar conclusões de alto nível.
    # Conclusão KPI: Foca no macro (oportunidades de mercado e categorias).
    conclusao_kpi = gerar_conclusao_kpi(insights_kpi)

    # Conclusão Reviews: Foca no micro (ajustes no produto e experiência do usuário).
    conclusao_reviews = gerar_conclusao_reviews(insights_reviews)

    # 3. MONTAGEM DO TEMPLATE (MARKDOWN)
    # O uso de f-strings com aspas triplas permite criar um documento multilinhas.
    # Estruturamos o relatório para que ele vá do "geral" (Insights) para o "específico" (Conclusões).
    relatorio = f"""
# 📊 Relatório de Análise de Produtos

## 🔍 Principais Insights (Dados)
{insights_kpi}

---

## 💬 Análise de Feedback do Cliente
{insights_reviews}

---

## 📌 Conclusão Estratégica
{conclusao_kpi}

## 🔧 Conclusão Operacional
{conclusao_reviews}
"""

    # 4. PERSISTÊNCIA DE DADOS (ESCRITA EM ARQUIVO)
    # 'with open' garante que o arquivo seja fechado automaticamente, mesmo se ocorrer um erro.
    # O modo 'w' limpa o arquivo antigo e escreve o novo.
    # encoding='utf-8' é vital para que os emojis e acentos não virem caracteres estranhos.
    with open("output/relatorio.txt", "w", encoding="utf-8") as f:
        f.write(relatorio)

    # 5. FEEDBACK DE EXECUÇÃO
    # Imprime no terminal para o desenvolvedor saber que o pipeline terminou com sucesso.
    print("Relatório gerado com sucesso.")
