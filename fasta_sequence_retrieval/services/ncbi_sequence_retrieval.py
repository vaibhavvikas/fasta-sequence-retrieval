from bs4 import BeautifulSoup
from selenium import webdriver
from fasta_sequence_retrieval.utils.utils import format_text

import time


URL = "https://www.ncbi.nlm.nih.gov/nuccore/"


def setup_selenium():
    options = webdriver.ChromeOptions()
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--incognito')
    options.add_argument('--headless')
    driver = webdriver.Chrome("driver/chromedriver", chrome_options=options)
    return driver


def get_page_source(accession_number, driver):
    driver.get(URL + accession_number)
    time.sleep(5)
    soup = BeautifulSoup(driver.page_source, "lxml")
    source = soup.find_all('pre', class_='genbank')
    page_source = ""
    for data in source:
        page_source += data.text.strip()
    return page_source


def get_amino_acid_sequence(data: list[str]):
    amino_acid_seq = []
    flag = False
    for line in data:
        if flag:
            if line.endswith('"'):
                amino_acid_seq.append(line.split('"')[0])
                break
            else:
                amino_acid_seq.append(line)

        if line.startswith("/translation"):
            amino_acid_seq.append(line.split('"')[-1])
            flag = True

    return "".join(amino_acid_seq)


def get_locus(data: list[str]):
    for line in data:
        if line.startswith("LOCUS"):
            locus = line.split(" ")
            for index in range(len(locus)):
                if locus[index] == "bp":
                    return " ".join(locus[index - 1: index + 1])
    
    return ""


def get_definition(data: list[str]):
    definition = []
    flag = False
    for line in data:
        if flag:
            if not line.split(" ")[0].isupper():
                definition.extend(line.split())
            else:
                break
        
        if line.startswith("DEFINITION"):
            definition.extend(line.split(" ")[1:])
            flag = True

    return " ".join(definition)


def get_source_info(data: list[str]):
    organism = ""
    host = ""
    country = ""
    collection_data = ""
    protein_id = ""

    for line in data:
        if line.startswith("/organism"):
            organism = line.split('"')[1]
        if line.startswith("/host"):
            host = line.split('"')[1]
        if line.startswith("/country"):
            country = line.split('"')[1]
        if line.startswith("/collection_date"):
            collection_data = line.split('"')[1]
        if line.startswith("/protein_id"):
            protein_id = line.split('"')[1]
            break

    return organism, host, country, collection_data, protein_id


def get_details(source) -> dict():
    data = format_text(source)
    details = dict()
    details["locus"] = get_locus(data)
    details["definition"] = get_definition(data)
    details["organism"], details["host"], details["country"], \
    details["collection_date"], details["protein_id"] = get_source_info(data)
    details["amino_acid_seq"] = get_amino_acid_sequence(data)
    return details


def download_sequence_info(accession_number, driver):
    try:
        page_source = get_page_source(accession_number, driver)
        return get_details(page_source), None
    except Exception as e:
        return {}, str(e)
