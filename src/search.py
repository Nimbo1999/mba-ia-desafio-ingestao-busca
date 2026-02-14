from typing import Optional
from config import (
    get_embeddings,
    get_vector_store,
)
from langchain_core.prompts import PromptTemplate

PROMPT_TEMPLATE = """
CONTEXTO:
{context}

REGRAS:
- Responda somente com base no CONTEXTO.
- Se a informação não estiver explicitamente no CONTEXTO, responda:
  "Não tenho informações necessárias para responder sua pergunta."
- Nunca invente ou use conhecimento externo.
- Nunca produza opiniões ou interpretações além do que está escrito.

EXEMPLOS DE PERGUNTAS FORA DO CONTEXTO:
Pergunta: "Qual é a capital da França?"
Resposta: "Não tenho informações necessárias para responder sua pergunta."

Pergunta: "Quantos clientes temos em 2024?"
Resposta: "Não tenho informações necessárias para responder sua pergunta."

Pergunta: "Você acha isso bom ou ruim?"
Resposta: "Não tenho informações necessárias para responder sua pergunta."

PERGUNTA DO USUÁRIO:
{question}

RESPONDA A "PERGUNTA DO USUÁRIO"
"""

def search_prompt(question: Optional[str] = None) -> str:
    embeddings = get_embeddings()
    store = get_vector_store(embeddings)
    results = store.similarity_search_with_score(question, k=10)
    context = "\n".join([f"Documento {i+1}: {doc.page_content}" for i, (doc, _score) in enumerate(results)])
    prompt_template = PromptTemplate(
        input_variables=["context", "question"],
        template=PROMPT_TEMPLATE,
    )
    return prompt_template.format(context=context, question=question)
