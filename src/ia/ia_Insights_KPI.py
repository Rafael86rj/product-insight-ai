# 1. IMPORTAÇÃO DE BIBLIOTECAS
# Biblioteca padrão para se conectar a modelos de linguagem (LLMs)
from openai import OpenAI
# Biblioteca para converter dados Python em formato JSON (texto estruturado)
import json

# 2. CONFIGURAÇÃO DO CLIENTE (CONEXÃO LOCAL)
# Criamos o objeto 'client' apontando para o servidor local do LM Studio.
# O base_url é o endereço do seu "servidor" interno rodando na sua máquina.
client = OpenAI(
    base_url="http://127.0.0.1:1234/v1",
    api_key="lm-studio"  # Para uso local, o valor da chave pode ser qualquer texto
)


def analisar_categorias(dados_categoria):
    """
    Função que recebe os dados estatísticos e solicita uma análise de negócio ao modelo.
    """

    # 3. SERIALIZAÇÃO (CONVERSÃO DE DADOS)
    # Transforma a lista de dicionários do Python em uma string formatada (JSON).
    # O 'indent=2' facilita a leitura da IA ao colocar quebras de linha e espaços.
    contexto = json.dumps(dados_categoria, indent=2)

    # 4. ENGENHARIA DE PROMPT (INSTRUÇÕES)
    # Criamos o texto que define a Persona (quem a IA deve ser) e a Tarefa (o que deve fazer).
    # Note o uso do f-string para inserir a variável {contexto} dentro das instruções.
    prompt = f"""
    Você é um analista de dados sênior.

    Analise os dados abaixo.

    Regras obrigatórias:
    - Use APENAS os dados fornecidos
    - NÃO invente informações
    - NÃO use conhecimento externo
    - NÃO inferir eficiência financeira
    - NÃO inventar relações causais
    - NÃO mencionar categorias fora da lista
    - NÃO repetir os dados literalmente
    - NÃO classificar valores acima de 4.0 como baixos

    Critérios de análise:
    - Volume (qtd_produtos) é relevante
    - Média ponderada define comparação
    - Considere que todas as categorias podem ter desempenho alto

    Dados:
    {contexto}

    Formato de saída obrigatório:

    1. Categorias com maior média observada
    2. Categorias com menor média observada (dentro do conjunto)
    3. Observações comparativas

    ---

    Exemplo de saída (NÃO copiar, apenas seguir o formato):

    1. Categorias com maior média observada:
    - Categoria A (4.30)
    - Categoria B (4.20)

    2. Categorias com menor média observada:
    - Categoria C (4.05)

    3. Observações comparativas:
    - As diferenças entre as médias são pequenas, indicando consistência geral.
    - Nenhuma categoria apresenta desempenho criticamente baixo.

    ---

    Agora gere a resposta com base nos dados fornecidos.
    Seja técnico, objetivo e sem redundância.
    """

    # 5. CHAMADA DA API (REQUISIÇÃO)
    # Enviamos as instruções para o modelo carregado no LM Studio.
    response = client.chat.completions.create(
        # Nome do modelo que deve estar ativo no LM Studio
        model="qwen2.5-coder-3b-instruct",
        messages=[
            # Define a instrução mestra da conversa
            {"role": "system", "content": prompt}
        ],
        # A 'temperature' define a criatividade.
        # 0.2 é um valor baixo, ideal para análises técnicas que precisam de precisão e fatos.
        temperature=0.15
    )

    # 6. RETORNO DO RESULTADO
    # Extrai do objeto de resposta apenas o conteúdo de texto gerado pela IA.
    return response.choices[0].message.content
