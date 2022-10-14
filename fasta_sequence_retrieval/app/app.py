import os
from fasta_sequence_retrieval.services.accession_extractor import extract_acc_from_file, extract_accession_from_seq_files
from fasta_sequence_retrieval.services import ncbi_sequence_retrieval
from fasta_sequence_retrieval.utils import utils


def sequence_data_format(acc_num, seq_details):
    return ">" + acc_num + " - " + seq_details["protein_id"] + ": " + seq_details["definition"] + "\n" \
        + seq_details["amino_acid_seq"] + "\n"


def load_all_nucleotides():
    acc_numbers = set()

    seq_dir = "data/sequence/"
    for sequence_files in os.listdir(seq_dir):
        acc_numbers = acc_numbers.union(extract_accession_from_seq_files(seq_dir + sequence_files))

    for acc_files in os.listdir("data/"):
        if acc_files.endswith(".txt"):
            acc_numbers = acc_numbers.union(extract_acc_from_file("data/" + acc_files))
    
    return sorted(list(acc_numbers))


def download_seq_data(acc_numbers):
    finished, missed = [], []
    amino_acid_seq_data = []
    seq_details_data = []

    driver = ncbi_sequence_retrieval.setup_selenium()
    
    for accession_number in acc_numbers:
        print("Loading Accerssion Number:", accession_number)
        seq_details, err = ncbi_sequence_retrieval.download_sequence_info(accession_number, driver)
        if not err and seq_details["amino_acid_seq"] != "":
            seq_details["accession_number"] = accession_number
            amino_acid_seq_data.append(sequence_data_format(accession_number, seq_details))
            seq_details_data.append(seq_details)
            finished.append(accession_number)
        else:
            missed.append(accession_number)

    driver.close()

    # Save results in /output dir
    utils.save_text_file("\n".join(amino_acid_seq_data), "amino_acid_seq_data.txt")
    fields = ["accession_number", "locus", "definition", "organism", "host", "country", "collection_date", "protein_id"]
    utils.save_dict_to_csv(fields, seq_details_data, "seq_details.csv")

    utils.save_text_file("\n".join(finished), "finished.csv")
    utils.save_text_file("\n".join(missed), "missed.csv")
