demo_1

root@codespaces-f05757:/workspaces/BDHB-lab/labs/01_intro&databases# python ./demo01_entrez_brca1.py
Găsite 1 rezultate.
ID: 3070263245
Titlu: Homo sapiens isolate AB17 BRCA1 protein (BRCA1) gene, partial cds
Length: 350 bp
GC fraction: 0.423
First 50 nt: CCTGATGGGTTGTGTTTGGTTTCTTTCAGCATGATTTTGAAGTCAGAGGA

demo_2

root@codespaces-f05757:/workspaces/BDHB-lab/labs/01_intro&databases# python ./demo02_seq_ops.py 
DNA: ATGGCCATTGTAATGGGCCGCTGAAAGGGTGCCCGATAG
RNA: AUGGCCAUUGUAAUGGGCCGCUGAAAGGGUGCCCGAUAG
Protein: MAIVMGR*KGAR*
Reverse complement: CTATCGGGCACCCTTTCAGCGGCCCATTACAATGGCCAT
GC fraction: 0.564
ATG positions: [0, 12]

demo_3

root@codespaces-f05757:/workspaces/BDHB-lab/labs/01_intro&databases# python ./demo03_dbsnp.py 
Am găsit 5 SNP IDs.
SNP_ID: 2552282559 | CHRPOS: 17:43127349 | Funcție: upstream_transcript_variant,2KB_upstream_variant,intron_variant
SNP_ID: 2552281972 | CHRPOS: 17:43127232 | Funcție: upstream_transcript_variant,2KB_upstream_variant,intron_variant
SNP_ID: 2552281880 | CHRPOS: 17:43127053 | Funcție: upstream_transcript_variant,2KB_upstream_variant,intron_variant
SNP_ID: 2552281808 | CHRPOS: 17:43126996 | Funcție: upstream_transcript_variant,2KB_upstream_variant,intron_variant
SNP_ID: 2552281780 | CHRPOS: 17:43126982 | Funcție: upstream_transcript_variant,2KB_upstream_variant,intron_variant

ex_1

query

root@codespaces-f05757:/workspaces/BDHB-lab# python labs/01_intro\&databases/ex01_multifasta_gc.py \
  --email paul.biragnet@student.upt.ro \
  --query "TP53[Gene] AND Homo sapiens[Organism]" \
  --retmax 3 \
  --out "data/work/PaulBiragnet/lab01/my_tp53.fa"
[ok] Wrote 3 records to: data/work/PaulBiragnet/lab01/my_tp53.fa
NG_017013.2     GC=0.490
NC_060941.1     GC=0.453
NC_000017.11    GC=0.453

accession

root@codespaces-f05757:/workspaces/BDHB-lab# python ./labs/01_intro\&databases/ex01_multifasta_gc.py --email paul.biragnet@student.upt.ro --accession NM_000546 --out ./data/work/PaulBiragnet/lab01/nm000546.fa
[ok] Wrote 1 records to: data/work/PaulBiragnet/lab01/nm000546.fa
NM_000546.6     GC=0.534