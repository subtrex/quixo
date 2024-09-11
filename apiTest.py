import requests
import xml.etree.ElementTree as ET

# Define the base URL for the arXiv API
base_url = "http://export.arxiv.org/api/query?"

# Define the parameters for the query
params = {
    "search_query": "music genre classification using machine learning",  # Search term
    "start": 0,  # Start at the first result
    "max_results": 50,  # Limit the results to 5 papers
    "sortBy": "relevance",  # Sort by relevance
    "sortOrder": "descending"  # Sort order
}

# Make a GET request to the arXiv API with the parameters
response = requests.get(base_url, params=params)

# Parse the XML response
root = ET.fromstring(response.content)

# Define the namespace for parsing XML (arXiv uses Atom namespace)
namespace = {"atom": "http://www.w3.org/2005/Atom"}

# Iterate through the XML tree and extract relevant information
for entry in root.findall("atom:entry", namespace):
    title = entry.find("atom:title", namespace).text
    summary = entry.find("atom:summary", namespace).text
    author = entry.find("atom:author/atom:name", namespace).text
    published = entry.find("atom:published", namespace).text
    pdf_link = entry.find("atom:link[@title='pdf']", namespace).attrib['href']

    # Print the extracted data in a clean format
    print(f"Title: {title}\nAuthor: {author}\nPublished: {published}\nPDF Link: {pdf_link}\nSummary: {summary.strip()}\n{'-'*80}\n")
