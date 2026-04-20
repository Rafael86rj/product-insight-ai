# 1. CONFIGURAÇÃO DO AMBIENTE
from openai import OpenAI

# Conecta ao servidor local do LM Studio (ideal para a tua RAM de 8GB)
client = OpenAI(
    base_url="http://127.0.0.1:1234/v1",
    api_key="lm-studio"
)

# 2. FUNÇÃO MESTRE (CORE LOGIC)


def gerar_conclusao_base(contexto, tipo):
    """
    Esta é uma função genérica que processa diferentes tipos de análise.
    O segredo aqui é o uso de 'instruções dinâmicas' baseadas no parâmetro 'tipo'.
    """

    # 3. LÓGICA DE COMPORTAMENTO (IF/ELIF)
    # Se o tipo for 'kpi', a IA assume uma postura de Analista de Mercado
    if tipo == "kpi":
        instrucoes = """
Foco: análise de mercado (categorias)
Regras:
- NÃO repetir os dados fornecidos
- NÃO inventar números ou relações
- NÃO afirmar causalidade sem evidência
- Considerar volume e média ponderada

Formato obrigatório:

Conclusão:
As categorias analisadas apresentam avaliações consistentemente altas, com destaque para OfficeProducts e Computers_Accessories. As diferenças entre as médias são pequenas, indicando um mercado estável e sem categorias com desempenho crítico.

Recomendações:
- Priorizar categorias com maior volume para escala
- Explorar nichos com alta avaliação para diferenciação
- Monitorar consistência em categorias de grande volume
"""

    # Se o tipo for 'reviews', a IA vira uma Especialista em Experiência do Cliente (UX)
    elif tipo == "reviews":
        instrucoes = """
Foco: análise de produto (experiência do cliente)
Regras:
- NÃO generalizar
- NÃO usar termos técnicos não presentes nos reviews
- Considerar apenas padrões recorrentes

Formato obrigatório:

Conclusão:
- Síntese da experiência do cliente (máx 3 linhas)

Recomendações:
- Máx 4 melhorias práticas de produto
"""

    # 4. CONSTRUÇÃO DO PROMPT FINAL
    # Aqui unimos os dados (contexto) com as regras definidas acima
    prompt = f"""
Você é um analista de negócios.

Dados:
{contexto}

{instrucoes}

Seja direto e objetivo.
"""

    # 5. CHAMADA DA IA
    # Usando o Qwen 2.5 1.5B que é perfeito para a tua máquina
    resposta = client.chat.completions.create(
        model="qwen2.5-coder-3b-instruct",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.2  # Temperatura baixa para manter a sobriedade técnica
    )

    return resposta.choices[0].message.content

# 6. FUNÇÕES WRAPPERS (ATALHOS)
# Estas funções facilitam a chamada no Main.py, escondendo a complexidade do 'tipo'


def gerar_conclusao_kpi(insights_kpi):
    """Atalho para gerar conclusão focada em números."""
    return gerar_conclusao_base(insights_kpi, "kpi")


def gerar_conclusao_reviews(insights_reviews):
    """Atalho para gerar conclusão focada em sentimentos/reviews."""
    return gerar_conclusao_base(insights_reviews, "reviews")
