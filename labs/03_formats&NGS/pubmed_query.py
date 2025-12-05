import sys
from Bio import Entrez
from pathlib import Path

# --- Configuration ---
handle = "PaulBiragnet"
Entrez.email = "paul.biragnet@student.upt.ro" 
MAX_ARTICLES = 5
QUERY = "TP53 AND cancer"
out_report = Path(f"labs/03_formats&NGS/pubmed_{handle}.txt")
# --- End Configuration ---

def main():
    """Queries PubMed and saves the results (title, authors, abstract) to a file."""
    
    # Ensure output directory exists
    out_report.parent.mkdir(parents=True, exist_ok=True)
    
    try:
        # Search PubMed for the query
        handle_search = Entrez.esearch(db="pubmed", term=QUERY, retmax=MAX_ARTICLES)
        record = Entrez.read(handle_search)
        id_list = record["IdList"]
        handle_search.close()
        
        if not id_list:
            print(f"[ERROR] No results found for query: '{QUERY}'")
            return

        # Fetch details for the returned IDs
        handle_fetch = Entrez.efetch(db="pubmed", id=id_list, rettype="xml", retmode="xml")
        articles = Entrez.read(handle_fetch)
        handle_fetch.close()

    except Exception as e:
        print(f"[ERROR] Entrez API call failed: {e}. Check network connection or API setup.")
        sys.exit(1)

    with open(out_report, "w", encoding="utf-8") as out:
        out.write(f"--- PubMed Results for Query: '{QUERY}' ---\n")
        out.write(f"Total articles retrieved: {len(articles['PubmedArticle'])}\n\n")
        
        for i, article in enumerate(articles['PubmedArticle']):
            medline = article['MedlineCitation']
            article_info = medline['Article']
            
            # Extract Title
            title = article_info['ArticleTitle']
            
            # Extract Authors
            authors = ", ".join([
                f"{author.get('LastName', '')} {author.get('Initials', '')}"
                for author in article_info.get('AuthorList', [])
            ])
            
            # Extract Abstract (handle case where abstract might be missing, string, or complex list)
            abstract = ""
            if 'Abstract' in article_info:
                abstract_data = article_info['Abstract']['AbstractText']
                
                if isinstance(abstract_data, list):
                    # Robustly concatenate all text parts from the list structure
                    parts = []
                    for p in abstract_data:
                        # Extract the text from the dictionary structure (handles AbstractText or NlmCategory)
                        if isinstance(p, dict) and 'AbstractText' in p:
                             parts.append(p['AbstractText'])
                        # Fallback for unexpected structures, but primarily target AbstractText
                        elif isinstance(p, str):
                             parts.append(p)
                    abstract = "\n".join(parts)
                elif isinstance(abstract_data, str):
                    # Handle simple abstract which is directly a string
                    abstract = abstract_data
            
            out.write(f"--- ARTICLE {i+1} ---\n")
            out.write(f"Title: {title}\n")
            out.write(f"Authors: {authors}\n")
            out.write(f"Abstract:\n{abstract}\n\n")
            
    print(f"[OK] PubMed query results saved to -> {out_report.resolve()}")

if __name__ == "__main__":
    main()