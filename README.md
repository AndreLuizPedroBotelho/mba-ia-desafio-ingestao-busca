# MBA IA - Desafio Ingestão e Busca

Projeto para ingestão de documentos PDF e busca inteligente via chat, utilizando embeddings generativos e banco vetorial PostgreSQL (PGVector).

Permite processar um PDF, indexar seu conteúdo e realizar perguntas em linguagem natural sobre o documento.


## Requisitos
- Python 3.10+
- Conta Google Generative AI (API Key)
- PostgreSQL com extensão PGVector
- Docker (opcional, recomendado para banco de dados)


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
   PG_VECTOR_COLLECTION_NAME=mba_ia_desafio_ingestao_busca
   DATABASE_URL=postgresql+psycopg://user:password@localhost:5432/dbname
   ```
   - O modelo de embedding já está fixo no código como `models/embedding-001`.
   - O arquivo PDF deve estar no caminho especificado em `PDF_PATH`.

4. (Opcional) Suba um banco PostgreSQL+PGVector com Docker:
   ```bash
   docker-compose up -d
   ```
   Certifique-se de ajustar o `DATABASE_URL` conforme o serviço do docker-compose.


## Uso
### 1. Ingestão do PDF
Executa a ingestão do PDF e armazena os embeddings no banco vetorial:
```bash
python src/ingest.py
```

### 2. Chat de Busca
Permite buscar informações no PDF via chat:
```bash
python src/chat.py
```
Digite sua pergunta e pressione Enter. Para sair, digite apenas `q`.

#### Exemplo de uso:
```
❓ Pergunta (q para sair): Qual o objetivo do documento?
💬 Resposta: ...
```


## Estrutura do Projeto
- `src/ingest.py`: Ingestão do PDF para o banco vetorial
- `src/chat.py`: Interface de chat para busca
- `src/search.py`: Funções auxiliares de busca

## Observações
- O projeto utiliza Google Generative AI Embeddings (é necessário chave de API válida).
- O modelo de embedding está fixo como `models/embedding-001`.
- O banco de dados deve estar acessível conforme a string `DATABASE_URL`.
- O chat só encerra se digitar exatamente `q` (minúsculo, sem espaços).


## Licença
MIT