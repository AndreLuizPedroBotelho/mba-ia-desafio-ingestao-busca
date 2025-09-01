from search import search_prompt
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_postgres import PGVector
import os
from dotenv import load_dotenv

load_dotenv()


def main():
    while True:
        query = input("\n❓ Pergunta (q para sair): ")
        if query.lower() == "q" and len(query) == 1:
            break

        chain = search_prompt()

        if not chain:
            print(
                "Não foi possível iniciar o chat. Verifique os erros de inicialização."
            )
            return

        embeddings = GoogleGenerativeAIEmbeddings(
            model=str(os.getenv("LLM_MODEL_EMBEDDING", "models/embedding-001")),
            google_api_key=os.getenv("LLM_API_KEY"),
        )

        store = PGVector(
            embeddings=embeddings,
            collection_name=os.getenv("PG_VECTOR_COLLECTION_NAME"),
            connection=os.getenv("DATABASE_URL"),
            use_jsonb=True,
        )

        results = store.similarity_search_with_score(query, k=5)
        result = chain.invoke({"pergunta": query, "contexto": results})
        print(f"\n💬 Resposta: {result.content}")


if __name__ == "__main__":
    main()
