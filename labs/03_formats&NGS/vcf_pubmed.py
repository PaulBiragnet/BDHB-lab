import sys
from Bio import Entrez
from pathlib import Path

# --- Configuration ---
handle = "PaulBiragnet"
Entrez.email = "paul.biragnet@student.upt.ro" 

VCF_PATH = Path("sample.vcf")
MAX_PUBMED_RESULTS = 3
out_report = Path(f"labs/03_formats&NGS/variants_{handle}.txt")
# --- End Configuration ---

def search_pubmed(query):
    """Performs a search on PubMed and returns titles."""
    try:
        handle_search = Entrez.esearch(db="pubmed", term=query, retmax=MAX_PUBMED_RESULTS)
        record = Entrez.read(handle_search)
        id_list = record["IdList"]
        handle_search.close()
        
        if not id_list:
            return [f"No articles found for query: {query}"]

        handle_fetch = Entrez.efetch(db="pubmed", id=id_list, retmode="text", rettype="abstract")
        # Read the abstract text (which contains the title)
        abstracts = handle_fetch.read().split('\n\n')
        handle_fetch.close()

        # Simple title extraction: assuming title is usually one of the first lines
        titles = []
        for abstract in abstracts:
            for line in abstract.split('\n'):
                line = line.strip()
                if line and not line.startswith('PMID'):
                    # Only take the first title-like line from each abstract chunk
                    titles.append(f"Title: {line}")
                    break
        
        return titles[:MAX_PUBMED_RESULTS]

    except Exception as e:
        return [f"PubMed API Error: {e} for query: {query}"]

def parse_vcf_and_search():
    """Reads VCF, extracts variants, and queries PubMed based on ID or coordinates."""
    
    out_report.parent.mkdir(parents=True, exist_ok=True)
    
    if not VCF_PATH.exists():
        # Check if file exists in the current working directory (CWD)
        if not Path.cwd() / VCF_PATH:
            return [f"[ERROR] VCF file not found at {VCF_PATH}. Please ensure 'sample.vcf' is present."]

    results = []
    
    with VCF_PATH.open("r", encoding="utf-8") as vcf_file:
        variant_count = 0
        for line in vcf_file:
            if line.startswith('#'):
                continue
            
            if variant_count >= 2: # Stop after processing 2 variants as required
                break
                
            parts = line.strip().split('\t')
            if len(parts) < 8: continue

            # VCF fields: CHROM, POS, ID, REF, ALT, QUAL, FILTER, INFO
            chrom, pos, rsid = parts[0], parts[1], parts[2]
            
            # We assume TP53 is on chromosome 17 for coordinate searching
            
            search_query = ""
            if rsid and rsid != ".":
                # Strategy 1: Search using known rsID
                search_query = f"{rsid} AND TP53"
                search_type = f"rsID ({rsid})"
            else:
                # Strategy 2: Search using coordinates and gene name
                if not chrom.startswith('chr'):
                    chrom = f"chr{chrom}"
                search_query = f"{chrom}:{pos} AND TP53"
                search_type = f"Coordinates ({chrom}:{pos})"
            
            results.append(f"--- Variant {variant_count + 1} ({search_type}) ---")
            results.append(f"Searching PubMed with: '{search_query}'")
            
            pubmed_results = search_pubmed(search_query)
            results.extend(pubmed_results)
            results.append("-" * 30)
            
            variant_count += 1
            
    if variant_count == 0:
        results.append("No variants found in the VCF file to process.")

    return results

def main():
    results = parse_vcf_and_search()
    
    with open(out_report, "w", encoding="utf-8") as out:
        out.write('\n'.join(results))
        
    print(f"[OK] VCF variant search report saved to -> {out_report.resolve()}")

if __name__ == "__main__":
    main()