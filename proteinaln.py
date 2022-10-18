"""Substitution Matrices

Substitution matrices are an extremely important part of everyday bioinformatics work.
They provide the scoring terms for classifying how likely two different residues are to substitute for each other. 
This is essential in doing sequence comparisons.
The book “Biological Sequence Analysis” by Durbin et al. provides a really nice introduction to Substitution Matrices and their uses. 
Some famous substitution matrices are the PAM and BLOSUM series of matrices.
Biopython provides a ton of common substitution matrices, and also provides functionality for creating your own substitution matrices."""


import numpy


filename = r"C:\Users\micha\Desktop\biopython-master\Tests\Clustalw\protein.aln"

from Bio import AlignIO
alignment = AlignIO.read(filename, "clustal")

observed_frequencies = alignment.substitutions

#observed_frequencies = observed_frequencies.select("DEHKR")

observed_frequencies /= numpy.sum(observed_frequencies)
residue_frequencies = numpy.sum(observed_frequencies, 0)
#print(format(residue_frequencies, "%.4f"))
expected_frequencies = numpy.dot(residue_frequencies[:, None], residue_frequencies[None, :])
m = numpy.log2(observed_frequencies/expected_frequencies)
#print(m)
#print(observed_frequencies)
#
#print(expected_frequencies)
from Bio.Align import PairwiseAligner
aligner = PairwiseAligner()
aligner.substitution_matrix = m
aligner.gap_score = -3.0
alignments = aligner.align("DEHEK", "DHHKK")

print(alignments.score)