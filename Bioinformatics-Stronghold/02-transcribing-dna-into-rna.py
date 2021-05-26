#! /usr/bin/env python3

import sys
import bioinformatics_tools as bfx

file = sys.argv[1]
rna = bfx.read_fasta(file)

for seq in rna:
    print(bfx.transcribe_dna_rna(seq))