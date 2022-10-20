from fasta_sequence_retrieval.utils import utils


def extract_accession_from_seq_files(filename):
    data = utils.read_file(filename).split("\n")
    nucleotides = set()
    for line in data:
        if line.startswith(">"):
            line_data = line.split(" ")[0][1:].split(":")
            nucleotide = line_data[0]
            nucleotides.add(nucleotide)

    return nucleotides


def extract_acc_from_file(filename):
    nucleotides = set(utils.read_file(filename).split("\n"))
    nucleotides.discard("")
    return nucleotides
