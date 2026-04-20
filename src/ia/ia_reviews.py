# 1. IMPORTAÇÃO DE BIBLIOTECA
from openai import OpenAI  # Conector padrão para comunicação com modelos de linguagem

import random  # Biblioteca para operações aleatórias, essencial para a amostragem de reviews


# 2. CONFIGURAÇÃO DO CLIENTE (LM STUDIO)
# Define o endereço do servidor local onde a IA está "escutando"
client = OpenAI(
    base_url="http://127.0.0.1:1234/v1",
    api_key="lm-studio"
)


def analisar_reviews(categoria, reviews):
    """
    Função de Análise de Sentimento e Feedback.

    Objetivo: Transformar uma lista de comentários desestruturados em 
    insights estratégicos sobre a experiência do usuário.
    """

    # 3. PREPARAÇÃO DO TEXTO (CONCATENAÇÃO)
    # Pega a lista de reviews e junta tudo em uma única String gigante.
    # O "\n\n".join(reviews) coloca dois espaços entre cada comentário para a IA não misturá-los.
    # Limita a 30 reviews para não sobrecarregar a IA
    reviews = random.sample(reviews, min(30, len(reviews)))
    texto_reviews = "\n\n".join(reviews)

    # 4. ENGENHARIA DE PROMPT (PERSONALIZAÇÃO)
    # Define uma Persona específica: "Especialista em experiência do cliente".
    # Note que passamos a 'categoria' para dar contexto geográfico/mercadológico à IA.
    prompt = f"""
Você é especialista em análise de feedback de clientes.

Regras:
- NÃO generalizar
- NÃO usar termos vagos (ex: "bom", "ótimo")
- Sempre descrever o que exatamente está sendo elogiado ou criticado
- Só considerar padrões que aparecem em múltiplos reviews
- NÃO usar termos que não estejam claramente presentes nos textos
- NÃO traduzir ou adaptar termos técnicos
- Ignorar termos ambíguos ou inconsistentes

Categoria: {categoria}

Reviews:
{texto_reviews}

Gere:

1. Principais elogios
   - Seja específico (ex: "aderência do material", "facilidade de instalação")
   - Indique padrão observado

2. Principais reclamações
   - Seja específico
   - Indique padrão observado

3. Principais problemas estruturais do produto

4. O que diferencia esse produto dos concorrentes (com base nos reviews)

5. Recomendações técnicas de melhoria

Evite linguagem genérica.
Seja analítico.
"""

    # 5. EXECUÇÃO DA ANÁLISE (REQUEST)
    # Enviamos o prompt. Note que a temperature=0.4 é um pouco mais alta que na análise numérica,
    # permitindo que a IA tenha uma sensibilidade maior para interpretar nuances de linguagem.
    resposta = client.chat.completions.create(
        # Lembre-se de usar o modelo que melhor roda na sua RAM
        model="qwen2.5-coder-3b-instruct",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.4
    )

    # 6. RETORNO DOS INSIGHTS
    # Retorna o texto formatado com os elogios, reclamações e sugestões.
    return resposta.choices[0].message.content
