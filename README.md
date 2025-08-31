# MBA IA - Desafio Ingestão e Busca

Este projeto realiza a ingestão de documentos PDF e permite buscas inteligentes utilizando embeddings e banco de dados vetorial.

## Requisitos
- Python 3.10+
- Docker (opcional, para banco de dados)

## Instalação
1. Clone o repositório:
   ```bash
   git clone <repo-url>
   cd mba-ia-desafio-ingestao-busca
   ```
2. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```
3. Configure as variáveis de ambiente em um arquivo `.env`:
   ```env
   PDF_PATH=./document.pdf
   LLM_API_KEY=<sua-chave-google>
   PG_VECTOR_COLLECTION_NAME=docs
   DATABASE_URL=postgresql+psycopg://user:password@localhost:5432/dbname
   ```

## Uso
### Ingestão do PDF
Executa a ingestão do PDF e armazena os embeddings no banco vetorial:
```bash
python src/ingest.py
```

### Chat de Busca
Permite buscar informações no PDF via chat:
```bash
python src/chat.py
```
Digite sua pergunta ou "q" para sair.

## Estrutura
- `src/ingest.py`: Ingestão do PDF para o banco vetorial
- `src/chat.py`: Interface de chat para busca
- `src/search.py`: Funções auxiliares de busca

## Licença
MIT