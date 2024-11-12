from pathway.xpacks.llm.vector_store import VectorStoreClient

PATHWAY_PORT = 8123
PATHWAY_HOST = "127.0.0.1"
# PATHWAY_HOST = "3.6.115.182"

client = VectorStoreClient(
    host=PATHWAY_HOST,
    port=PATHWAY_PORT,
)


def retrieve_documents(query: str):
    documents = client.query(query, k=5)
    return documents
