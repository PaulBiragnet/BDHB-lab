"""
Exercise 04 — FASTQ QC on your own data

TODO:
- Read your FASTQ file from data/work/<handle>/lab03/:
    your_reads.fastq  or  your_reads.fastq.gz
- Compute statistics:
    * total number of reads
    * mean read length
    * proportion of 'N' bases
    * mean Phred score
- Save the report in:
    labs/03_formats&NGS/submissions/<handle>/qc_report_<handle>.txt
"""

import os
import gzip
import sys
from pathlib import Path
from Bio import SeqIO
import numpy as np

# TODO: replace <handle> with your GitHub username
handle = "PaulBiragnet"

in_fastq_plain = Path(f"data/work/{handle}/lab03/your_reads.fastq")
in_fastq_gz = Path(f"data/work/{handle}/lab03/your_reads.fastq.gz")
out_report = Path(f"labs/03_formats&NGS/submissions/{handle}/qc_report_{handle}.txt")
out_report.parent.mkdir(parents=True, exist_ok=True)

# Select the existing file
if in_fastq_plain.exists():
    reader = SeqIO.parse(str(in_fastq_plain), "fastq")
elif in_fastq_gz.exists():
    # Biopython reads from file-like objects; we use gzip.open(..., "rt")
    reader = SeqIO.parse(gzip.open(in_fastq_gz, "rt"), "fastq")
else:
    raise FileNotFoundError(
        f"Could not find either {in_fastq_plain} or {in_fastq_gz}. "
        f"Run ex03_fetch_fastq.py first or copy your own FASTQ."
    )

num_reads = 0
total_length = 0
total_n = 0
total_phred = 0
total_bases = 0

# TODO: complete the aggregation logic
for record in reader:
    
    num_reads += 1

    seq_str = str(record.seq)
    phred = record.letter_annotations["phred_quality"]

    current_length = len(seq_str)
    
    total_length += current_length
    total_bases += current_length

    total_n += seq_str.upper().count('N')

    total_phred += sum(phred)
    

# TODO: compute final values (watch out for division by zero)
if num_reads > 0:
    len_mean = total_length / num_reads
else:
    len_mean = 0.0

if total_bases > 0:
    n_rate = total_n / total_bases
else:
    n_rate = 0.0

if total_bases > 0:
    phred_mean = total_phred / total_bases
else:
    phred_mean = 0.0

with open(out_report, "w", encoding="utf-8") as out:
    out.write(f"Reads: {num_reads}\n")
    out.write(f"Mean length: {len_mean:.2f}\n")
    out.write(f"N rate: {n_rate:.4f}\n")
    out.write(f"Mean Phred: {phred_mean:.2f}\n")

print(f"[OK] QC report -> {out_report.resolve()}")
