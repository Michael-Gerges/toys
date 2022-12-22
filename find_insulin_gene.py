!curl https://ftp.ncbi.nlm.nih.gov/genomes/refseq/vertebrate_mammalian/Homo_sapiens/latest_assembly_versions/GCF_000001405.40_GRCh38.p14/GCF_000001405.40_GRCh38.p14_genomic.gbff.gz --output genomic.gbff.gz
!gzip -d  genomic.gbff.gz
!pip install Bio



def translate(seq):
	
	table = {
		'ATA':'I', 'ATC':'I', 'ATT':'I', 'ATG':'M',
		'ACA':'T', 'ACC':'T', 'ACG':'T', 'ACT':'T',
		'AAC':'N', 'AAT':'N', 'AAA':'K', 'AAG':'K',
		'AGC':'S', 'AGT':'S', 'AGA':'R', 'AGG':'R',				
		'CTA':'L', 'CTC':'L', 'CTG':'L', 'CTT':'L',
		'CCA':'P', 'CCC':'P', 'CCG':'P', 'CCT':'P',
		'CAC':'H', 'CAT':'H', 'CAA':'Q', 'CAG':'Q',
		'CGA':'R', 'CGC':'R', 'CGG':'R', 'CGT':'R',
		'GTA':'V', 'GTC':'V', 'GTG':'V', 'GTT':'V',
		'GCA':'A', 'GCC':'A', 'GCG':'A', 'GCT':'A',
		'GAC':'D', 'GAT':'D', 'GAA':'E', 'GAG':'E',
		'GGA':'G', 'GGC':'G', 'GGG':'G', 'GGT':'G',
		'TCA':'S', 'TCC':'S', 'TCG':'S', 'TCT':'S',
		'TTC':'F', 'TTT':'F', 'TTA':'L', 'TTG':'L',
		'TAC':'Y', 'TAT':'Y', 'TAA':'_', 'TAG':'_',
		'TGC':'C', 'TGT':'C', 'TGA':'_', 'TGG':'W',
	}
	protein =""
	for i in range(0, len(seq), 3):
			codon = seq[i:i + 3]
			try:
				protein+= table[codon]
			except:
				continue
	return protein


from Bio import SeqIO
import pprint

in_file='genomic.gbff' # 704 records

in_handle = open(in_file, 'r')
for i, record in enumerate(SeqIO.parse(in_handle, 'genbank')):
    if "Homo sapiens chromosome 11" in record.description:
    #pprint.pprint(record)
    #print(dir(record))
        print(record.description)
        features = record.features
        break
    

in_handle.close()

for i, feature in enumerate(features):
    if feature.type =="CDS":
        #print(feature.location)
        if "INS" == (feature.qualifiers["gene"][0]):
            seqq = ((feature.extract(record)).seq)
            #print(feature)
            print(seqq)
            print(feature.location)
            print(feature.qualifiers["translation"])
            print(translate(feature.location.extract(record).seq))



#!pip install Bio
from Bio.Align import substitution_matrices
names = substitution_matrices.load()

from Bio.Align import substitution_matrices
from Bio import Align
aligner = Align.PairwiseAligner()
aligner.substitution_matrix = substitution_matrices.load("BLOSUM62")

#alignments = pairwise2.align.globalds(seq1, seq2, matrix, -10, -0.5)


#alignments = aligner.align("KEVLA", "EVL")

# Define the protein sequences to compare
seq1 = "MAEGEITTFTALTEKFNLPPGNYKKPKLLYCSNGGHFLRILPDGTVDGTRDRSDQHIQLQLSAESVGEVYIKSTETGQYLAMDTSGLLYGSQTPSEECLFLERLEENHYNTYTSKKHAEHKTNATLPCRIKQYERMALENPKKYVFDEFDLEEFLNTYKGSYQPVNKTNQRNRTPQGYYMGSYTFDYWGQGTLVTVSSASTKGPSVFPLAPSSKSTSGGTAALGCLVKDYFPEPVTVSWNSGALTSGVHTFPAVLQSDLYTLSSSVTVPSSTWPSETVTCNVAHPASSTKVDKKIVPRDCT"
seq2 = "MAEGEITTFTALTEKFNLPPGNYKKPKLLYCSNGGHFLRILPDGTVDGTRDRSDQHIQLQLSAESVGEVYIKSTETGQYLAMDTSGLLYGSQTPSEECLFLERLEENHYNTYTSKKHAEHKTNATLPCRIKQYERMALENPKKYVFDEFDLEEFLNTYKGSYQPVNKTNQRNRTPQGYYMGSYTFDYWGQGTLVTVSSASTKGPSVFPLAPSSKSTSGGTAALGCLVKDYFPEPVTVSWNSGALTSGVHTFPAVLQSDLYTLSSSVTVPSSTWPSETVTCNVAHPASSTKVDKKIVPRDCT"
alignments = aligner.align(seq1,seq2)


alignments = list(alignments)
print("Number of alignments: %d" % len(alignments))
alignment = alignments[0]
print("Score = %.1f" % alignment.score)
print(alignment)

seq1_aligned, seq2_aligned= alignment
identity = sum([1 for a, b in zip(seq1_aligned, seq2_aligned) if a == b]) / len(seq1_aligned)

# Print the percentage identity
print(f"Percentage identity: {identity:.2f}")
