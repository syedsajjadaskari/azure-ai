# rag_with_embeddings.py
import os
import numpy as np
from typing import List, Tuple
from azure.ai.projects import AIProjectClient
from azure.identity import DefaultAzureCredential




PROJECT_ENDPOINT = "https://agents-demo-resource.services.ai.azure.com/api/projects/agents-demo"
MODEL_NAME = "gpt-4o"
EMBEDDING_MODEL = "text-embedding-ada-002"

credential = DefaultAzureCredential()
project = AIProjectClient(endpoint=PROJECT_ENDPOINT, credential=credential)
openai_client = project.get_openai_client(api_version="2024-10-21")

class SimpleVectorStore:
    """Simple in-memory vector store for RAG"""
    
    def __init__(self):
        self.documents = []
        self.embeddings = []
    
    def add_documents(self, docs: List[str]):
        """Add documents and create embeddings"""
        print(f"Creating embeddings for {len(docs)} documents...")
        
        for doc in docs:
            # Get embedding for document
            response = openai_client.embeddings.create(
                model=EMBEDDING_MODEL,
                input=doc
            )
            embedding = response.data[0].embedding
            
            self.documents.append(doc)
            self.embeddings.append(embedding)
        
        print(f"✓ Added {len(docs)} documents to vector store")
    
    def search(self, query: str, top_k: int = 3) -> List[Tuple[str, float]]:
        """Search for most relevant documents"""
        # Get query embedding
        response = openai_client.embeddings.create(
            model=EMBEDDING_MODEL,
            input=query
        )
        query_embedding = response.data[0].embedding
        
        # Calculate cosine similarity
        similarities = []
        for doc, doc_embedding in zip(self.documents, self.embeddings):
            similarity = self._cosine_similarity(query_embedding, doc_embedding)
            similarities.append((doc, similarity))
        
        # Sort by similarity and return top_k
        similarities.sort(key=lambda x: x[1], reverse=True)
        return similarities[:top_k]
    
    @staticmethod
    def _cosine_similarity(a, b):
        """Calculate cosine similarity between two vectors"""
        a = np.array(a)
        b = np.array(b)
        return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))

# Initialize vector store
vector_store = SimpleVectorStore()

# Load and add documents
documents = []
doc_names = []
for filename in os.listdir("data"):
    if filename.endswith(".md"):
        with open(f"data/{filename}", "r") as f:
            content = f.read()
            documents.append(content)
            doc_names.append(filename)

vector_store.add_documents(documents)

def rag_with_retrieval(question: str, top_k: int = 2) -> str:
    """RAG with semantic search"""
    
    # 1. Retrieve relevant documents
    print(f"\nSearching for: {question}")
    results = vector_store.search(question, top_k=top_k)
    
    print("\nTop relevant documents:")
    for i, (doc, score) in enumerate(results):
        doc_preview = doc[:100].replace("\n", " ")
        print(f"  {i+1}. (Score: {score:.4f}) {doc_preview}...")
    
    # 2. Create context from top documents
    context = "\n\n".join([doc for doc, _ in results])
    
    # 3. Generate answer
    prompt = f"""Answer the question based on the following context. 
If the answer is not in the context, say "I don't have enough information to answer that."

CONTEXT:
{context}

QUESTION: {question}

ANSWER:"""
    
    response = openai_client.chat.completions.create(
        model=MODEL_NAME,
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.3
    )
    
    return response.choices[0].message.content

# Test queries
questions = [
    "What tents do you have and what are their features?",
    "I need something for carrying gear on a long hike, what do you recommend?",
    "How much does the stove weigh?",
    "Do you sell GPS devices?",
]

for question in questions:
    print("\n" + "="*80)
    print(f"Q: {question}")
    answer = rag_with_retrieval(question, top_k=2)
    print(f"\nA: {answer}")
    print("="*80)