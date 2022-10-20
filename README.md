## fasta_sequence_retrieval

Python Project to extract the amino acid sequences using the nucleotide accession numbers retrieved from the NCBI. Sample results in `output` directory.

## Features

* Retrieval of the amino acids sequences, along with various details such as locus, definition, organism, host, country, collection_date, protein_id from the NCBI.

* Put the files inside `data` directory.
    - If only accession numbers are there in your files, put it inside data directly.
    - If your files contain the accession numbers with their sequences similar to the one in `sequence` directory, put that files inside the `sequence` directory.
    
    Note: File names do not matter.

## Project Setup
1. Install python version >= 3.9
2. Clone the repository.
3. Open cmd/terminal and run the following command to install dependencies `pip install -e .`
4. Your output will be generated inside the output directory. Please test with small numbers of seq first to make sure you're getting what is expected.

## Credits

This package was created with Cookiecutter_ and the `vaibhavvikas/cookiecutter-pypackage` project template.

* [Cookiecutter](https://github.com/audreyr/cookiecutter)
* [vaibhavvikas/cookiecutter-pypackage](https://github.com/vaibhavvikas/cookiecutter-pypackage)
