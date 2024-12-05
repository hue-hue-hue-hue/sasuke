from tavily import TavilyClient
from langchain_community.document_loaders import BraveSearchLoader
from swarm.util import debug_print

# from linkup import LinkupClient
import os


def tavily_search(query):
    debug_print(True, f"Processing tool call: {tavily_search.__name__}")
    tavily_client = TavilyClient(api_key="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")
    response = tavily_client.search(query=query)["results"]

    for result in response:
        result["text"] = result.pop("content")

    return response


def brave_search(query):
    debug_print(True, f"Processing tool call: {brave_search.__name__}")
    loader = BraveSearchLoader(
        query=query,
        api_key="BSACXk-7IV2P_qFzZzHS9CLsRDWKZoU",
        search_kwargs={"count": 5},
    )
    docs = loader.load()
    finaldocs = []
    for doc in docs:
        docdict = {}
        docdict.update(doc.metadata)
        docdict["text"] = doc.page_content
        finaldocs.append(docdict)
    return finaldocs


# def linkup_search(query):
# client = LinkupClient(api_key=os.environ["d29029da-250d-48d4-87ec-73be9a526871"])
# response = client.search(
# query=query,
# depth="deep",
# output_type="sourcedAnswer"
# )
# return response.answer
