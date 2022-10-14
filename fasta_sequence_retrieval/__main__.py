"""Main module."""
from fasta_sequence_retrieval.app.app import download_seq_data, load_all_nucleotides


def main():
    print("Application Started")
    acc_numbers = load_all_nucleotides()
    download_seq_data(acc_numbers)


if __name__ == "__main__":
    main()
