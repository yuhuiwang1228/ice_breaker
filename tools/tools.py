from langchain_community.tools.tavily_search import TavilySearchResults

def get_profile_url_tavily(name: str) -> str:
    search = TavilySearchResults()
    res = search.run(f"{name}")
    return res[0]["url"]

if __name__ == "__main__":
    print(get_profile_url_tavily("Eden Marco"))