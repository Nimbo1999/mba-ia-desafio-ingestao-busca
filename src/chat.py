from search import search_prompt
from config import get_chat_model
from enum import Enum

class Subject(str, Enum):
    OUT_OF_CONTEXT = "OUT_OF_CONTEXT"
    REVENUE = "REVENUE"

class ChatStructure:
    subject: Subject
    question: str

    def __init__(self, question: str = "", subject: Subject = Subject.REVENUE):
        self.subject = subject
        self.question = question

def main():
    model = get_chat_model()
    structures = [
        ChatStructure("Qual o faturamento da Empresa SuperTechIABrazil?", Subject.REVENUE),
        ChatStructure("Quantos clientes temos em 2024?", Subject.OUT_OF_CONTEXT),
    ]

    for i, structure in enumerate(structures, start=0):
        print(structure.subject == Subject.REVENUE and "Faça sua pergunta:\n" or "Perguntas fora do contexto:\n")
        print(f"Pergunta: {structure.question}")
        print("Resposta:", end=" ")
        prompt = search_prompt(structure.question)
        for response in model.stream(prompt):
            print(response.content, end="", flush=True)

        print() # Para adicionar uma nova linha após a resposta completa
        if i < len(structures) - 1:
            print("\n---\n")

if __name__ == "__main__":
    main()