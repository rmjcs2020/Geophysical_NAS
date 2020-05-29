
[![DOI](https://zenodo.org/badge/258007645.svg)](https://zenodo.org/badge/latestdoi/258007645)
# Geophysical_NAS
Case setup for "Recurrent Neural Network Architecture Search for Geophysical Emulation" - Submission to ISC 2020. 

In the following - we shall outline how to install DeepHyper on your local machine to assess a trial evaluation for LSTM architecture search.

# Installation instructions

1. `git clone https://github.com/rmjcs2020/Geophysical_NAS.git`
2. `cd Geophysical_NAS/`
3. `conda create --name sctest python==3.6.6`
4. `source activate sctest`
5. `git clone https://github.com/deephyper/deephyper.git`
6. `cd deephyper/`
7. `pip install -e '.[tests,docs,analytics]'`

# Incorporating this problem

8. `cd ../noaa_lstm_search/`
9. `pip install -e .`

# Ensuring installation is OK
10. `cd noaa_lstm_search_1/`
11. `python load_data.py` # Should output nothing
12. `python problem.py` # Should output description of problem
13. `python search_space.py` # Should output description of problem and a random neural network

# Initializing a new neural architecture search on your local machine using Aging Evolution
14. `python -m deephyper.search.nas.regevo --problem noaa_lstm_search_1.problem.Problem`
