## fasta_sequence_retrieval

Python Project that can be used to extract their amino acid from their accession number from the ncbi portal. Sample resuklts in `output` directory.

## Features

* Retrieve the amino acids seq, along with their various details from the ncbi portal in one click.
Just put your files inside the data directory.

## Project Setup
1. Clone the repository
2. Replace the chromedriver inside `/driver` with the one respective to your chrome version. Follow [selenium.dev](https://www.selenium.dev/documentation/webdriver/getting_started/install_drivers/) to get the version respective to the chrome browser you have installed.
3. Open cmd/terminal and run the following commnd to install dependency `pip install -e .`
4. Put the files inside `data` directory.
    - If only accession numbers are there in your file, put it inside data directly
    - If your files contains the accession with their seq like in `sequence` dir, put that file inside the `sequence` directory

    Note: File names doesn't matter
5. Your output will be generated inside the output directory. Please test with small numbers of seq first to make sure you're getting what is expected.

## Credits

This package was created with Cookiecutter_ and the `vaibhavvikas/cookiecutter-pypackage` project template.

* Cookiecutter: (https://github.com/audreyr/cookiecutter)
* `vaibhavvikas/cookiecutter-pypackage`: (https://github.com/vaibhavvikas/cookiecutter-pypackage)
