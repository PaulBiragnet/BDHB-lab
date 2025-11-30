# Lab 02 Notes: Sequence Alignment

## 1. Datasets Used

For the execution of the exercises `ex02_global_nw.py` and `ex03_local_sw.py`, I used the following FASTA file:

* **File:** `data/work/PaulBiragnet/lab01/my_tp53.fa`
* **Sequences Aligned:** The sequences at indices 0 and 1 (ID: <ID_SEQ_0> vs <ID_SEQ_1>) after **truncation** to 2000 bases for performance reasons.

## 2. Reflection: When is global alignment preferred over local alignment?

**Global alignment** (Needleman–Wunsch) is preferred when aligning two sequences that are assumed to be **homologous over their entire length** and are of approximately the same size.

* **Goal:** To measure overall similarity and establish a complete evolutionary or functional relationship.
* **Result:** The alignment spans from the beginning to the end of both sequences, and terminal gaps are penalized.
* **Example:** Comparing two orthologous genes from closely related species (e.g., human TP53 gene vs. mouse TP53 gene).

**Local alignment** (Smith–Waterman) is preferred when searching for **highly similar regions** within sequences that may be very long, of different sizes, or only homologous across small fragments.

* **Goal:** To identify conserved domains, functional motifs, or major insertions/deletions.
* **Result:** The alignment is the highest-scoring segment found between the two sequences, ignoring dissimilar flanking regions.
* **Example:** Comparing a DNA fragment to a database of entire genomes, or identifying a conserved protein domain. 

## 3. Completed Exercises

The completed exercises have been saved in the `submissions` directory.