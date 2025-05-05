
from Bio.Align import PairwiseAligner
#Smith Waterman algorith for comaprign two dna sequences
def compare_sequences(seq1, seq2):
    aligner = PairwiseAligner()
    aligner.mode = "local"  # Smith-Waterman
    aligner.match_score = 1
    aligner.mismatch_score = 0
    aligner.open_gap_score = -1
    aligner.extend_gap_score = -0.5

    alignments = aligner.align(seq1, seq2)
    top_alignment = alignments[0]

    normalized_score = top_alignment.score / max(len(seq1), len(seq2))
    return round(normalized_score, 4)
    #print(f"Normalized Score: {normalized_score:.4f}")
    #print(top_alignment)
#smith_waterman()


