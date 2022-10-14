#!/usr/bin/env python

"""The setup script."""

from pathlib import Path
from setuptools import setup, find_packages

with open('README.md') as readme_file:
    readme = readme_file.read()

project_dir = Path(__file__).parent

setup(
    author="Vaibhav Vikas",
    author_email='vbhvvikas@gmail.com',
    python_requires='>=3.8',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10'
    ],
    description="Python Project that can be used to extract their amino acid from their accession number from the ncbi portal. Sample resuklts in `output` directory.",
    install_requires=project_dir.joinpath('requirements.txt').read_text().split("\n"),
    license="BSD license",
    long_description=readme,
    include_package_data=True,
    keywords='fasta_sequence_retrieval',
    name='fasta_sequence_retrieval',
    packages=find_packages(include=['fasta_sequence_retrieval', 'fasta_sequence_retrieval.*']),
    project_dir={"":"'fasta_sequence_retrieval'"},
    test_suite='tests',
    tests_require=project_dir.joinpath('requirements.txt').read_text().split("\n"),
    url='https://github.com/vaibhavvikas/fasta-sequence-retrieval',
    version='0.1.0',
    zip_safe=False,
)
