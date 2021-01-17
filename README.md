# Solutions to Basic Introduction to Organic Chemistry

Exercises are on [LibreText][1].

For optimal viewing, go to [the nbviewer](https://nbviewer.jupyter.org/github/flippedAben/ochem_sols/tree/m/).

## Setup

I had to install `conda` because it's the easiest way to install `rdkit`. To do
so, install Miniconda from [this page](https://docs.conda.io/en/latest/miniconda.html).

Then,

```bash
conda create -n ochem_solutions_env
conda activate ochem_solutions_env

# install rdkit from the rdkit channel
conda install -c rdkit rdkit

# Get a Jupyter notebook
conda install jupyter
```

[1]: https://chem.libretexts.org/Bookshelves/Organic_Chemistry/Book%3A_Basic_Principles_of_Organic_Chemistry_%28Roberts_and_Caserio%29/01%3A_Introduction_to_Organic_Chemistry
