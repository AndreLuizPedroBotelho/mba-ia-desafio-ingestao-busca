
# MBA IA - Desafio Ingestão e Busca

Projeto para ingestão de documentos PDF e busca inteligente via chat, utilizando embeddings generativos e banco vetorial PostgreSQL (PGVector).

Permite processar um PDF, indexar seu conteúdo e realizar perguntas em linguagem natural sobre o documento.

## Sumário
- [Requisitos](#requisitos)
- [Instalação](#instalação)
- [Uso](#uso)
- [Estrutura do Projeto](#estrutura-do-projeto)
- [Observações](#observações)
- [Licença](#licença)


## Requisitos
- Python 3.10+
- Conta Google Generative AI (API Key)
- PostgreSQL com extensão PGVector
- Docker


## Instalação
1. Clone o repositório:
   ```bash
   git clone <repo-url>
   cd mba-ia-desafio-ingestao-busca
   ```
2. (Opcional) Copie o arquivo de exemplo de variáveis de ambiente:
   ```bash
   cp .env.example .env
   ```
3. (Recomendado) Crie e ative um ambiente virtual (venv):
   - Linux/macOS:
     ```bash
     python3 -m venv .venv
     source .venv/bin/activate
     ```
   - Windows:
     ```cmd
     python -m venv .venv
     .venv\Scripts\activate
     ```
4. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```
5. Edite o arquivo `.env` conforme necessário:
   ```env
   LLM_API_KEY=                         # Chave da API Google Generative AI
   DATABASE_URL=                        # String de conexão PostgreSQL
   PG_VECTOR_COLLECTION_NAME=           # Nome da coleção PGVector
   PDF_PATH=document.pdf                # Caminho do PDF a ser indexado
   LLM_MODEL=gemini-2.5-flash-lite      # (opcional) Modelo LLM usado na busca (default: gemini-2.5-flash-lite)
   LLM_MODEL_EMBEDDING=models/embedding-001 # (opcional) Modelo de embedding (default: models/embedding-001)
   ```
   - `LLM_API_KEY`: Chave da API Google Generative AI (obrigatória)
   - `DATABASE_URL`: String de conexão PostgreSQL+PGVector (obrigatória)
   - `PG_VECTOR_COLLECTION_NAME`: Nome da coleção PGVector (obrigatória)
   - `PDF_PATH`: Caminho do PDF a ser indexado (obrigatória)
   - `LLM_MODEL`: Modelo LLM usado na busca (opcional, default: gemini-2.5-flash-lite)
   - `LLM_MODEL_EMBEDDING`: Modelo de embedding usado na indexação e busca vetorial (opcional, default: models/embedding-001)
   - O arquivo PDF deve estar no caminho especificado em `PDF_PATH`.
   - Se não definir `LLM_MODEL` ou `LLM_MODEL_EMBEDDING`, serão usados os valores padrão.

6. Suba um banco PostgreSQL+PGVector com Docker:
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
- O banco de dados deve estar acessível conforme a string `DATABASE_URL`.
- O chat só encerra se digitar exatamente `q` (minúsculo, sem espaços).
- As variáveis `LLM_MODEL` e `LLM_MODEL_EMBEDDING` podem ser definidas no `.env` para customizar os modelos usados. Valores padrão: `gemini-2.5-flash-lite` e `models/embedding-001`.


## Licença
MIT