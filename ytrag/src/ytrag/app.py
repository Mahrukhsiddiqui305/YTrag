from .data_loader import load_all_documents
from .embedding import EmbeddingPipeline



## Example usage

if __name__ == "__main__":
    docs = load_all_documents("data")
    chunks=EmbeddingPipeline().embed_chunks(docs)
    embeddings=EmbeddingPipeline().embed_chunks(docs)
    chunkvectors=EmbeddingPipeline().embed_chunks(chunks)
    print(chunkvectors)

   