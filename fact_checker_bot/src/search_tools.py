from duckduckgo_search import DDGS

def search(query: str, num_results: int = 5) -> list[dict]:
    """Searches the web for a given query using DuckDuckGo.

    Args:
        query: The query to search for.
        num_results: The number of results to return.

    Returns:
        A list of search results, where each result is a dictionary
        containing the title, url, and snippet of the result.
    """
    results = []
    with DDGS() as ddgs:
        for r in ddgs.text(query, max_results=num_results):
            results.append(r)
    return results
