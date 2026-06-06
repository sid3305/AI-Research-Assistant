from app.utils.web_scraper import WebScraper


scraper = WebScraper()

result = scraper.extract_text(
    "https://fake-website-xyz-123.com"
)

print("TITLE:")
print(result["title"])

print("\nTEXT:")
print(result["text"][:1000])