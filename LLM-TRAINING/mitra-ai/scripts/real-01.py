

from duckduckgo_search import DDGS

# --- DuckDuckGo Search Example ---
results = DDGS().text("India World Cup win", max_results=5)
print("Text Search Results:")
print(results)
print("\n" + "="*80 + "\n")

# --- DuckDuckGo News Example ---
keywords = 'Zelensky Trump fun meeting'
r = DDGS().news(keywords, region='in-en')

print("News Search Results:\n")
for article in r:
    date = article.get('date')
    title = article.get('title')
    body = article.get('body')
    url = article.get('url')
    image = article.get('image')
    source = article.get('source')

    print(f"Date: {date}")
    print(f"Title: {title}")
    print(f"Body: {body}")
    print(f"URL: {url}")
    print(f"Image: {image}")
    print(f"Source: {source}")
    print("\n" + "="*80 + "\n")

# Collect all titles + bodies into a text string
text = ""
for article in r:
    text += article.get('title', '') + "\n" + article.get('body', '') + "\n\n"

print("\nCollected Text:\n")
print(text)
