# METCS777-VectorDB
This is a repository for term project implementation for METCS777. This is a RAG application with Weaviate vector database


### What is RAG
Retrieval Augement Generation is a framework that allows LLM backed application to have access to updated, proprietory data that the underlying model was not trained with. This pattern has 3 main components:

- `Retrieval` - powered by Vector Search or a Vector Database. In this process user's `query` is used to search to similar documents or document chunks. The user's `query` is first encoded by an Embedding Model (which is the same as the Embedding Model used in creating vector embeddings stored in Vector Database) and turned into vector embeddings. Next a Vector Search Algorithm is performed (which is either an exhaustive-KNN or ANN) to find `top-k` vectors that have distance closest to the input

- `Augmentation`: retrieved documents chunks from `Retrieval` process are added to the System prompt, along with the user's original query to create a final Prompt

- `Generation`: the final Prompt is sent to an LLM (such as OpenAI) for text generation

### Developer Install
#### Option 1: Run in local virtual environments
Prepare your environments and software
1. Install Docker
3. create virtual environment (Optional but recommended)
   ```bash
   python -m venv .venv
   ```
4. activate virtual environment
5. install dependencies
   ```bash
   pip install -r requirements.txt
   ```

6. Set the following environment variables:  
   `OPENAI_API_KEY`=<your openai api key>  
   `WEAVIATE_URL`=http://localhost:8080

7. run Weaviate container with the following command
   ```bash
   docker run -p 8080:8080 cr.weaviate.io/semitechnologies/weaviate:1.24.4 
   ```

8. run `ingestion` pipeline first
   ```bash
   python ./script_ingestion.py
   ```

9. run `RAG chatapp`
   ```bash
   streamlit run ./app/app.py --server.runOnSave=True --browser.serverAddress=localhost
   ```
#### Option 2: Run docker compose