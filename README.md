# Lossy compression error tolerances from ERA5 ensemble data

[![image](https://img.shields.io/github/actions/workflow/status/juntyr/era5-ensemble-compression-tolerance/ci.yml?branch=main)](https://github.com/juntyr/era5-ensemble-compression-tolerance/actions/workflows/ci.yml?query=branch%3Amain)
<!--[![image](https://zenodo.org/badge/DOI/10.5281/zenodo.18355539.svg)](https://doi.org/10.5281/zenodo.18355539)-->

This repository contains the analyses published in the "Towards recommendations for lossy compression error tolerances of weather and climate data" paper for deriving compression error tolerances from ERA5 ensemble data and comparing them with expert-provided tolerances.


## Overview

The repository is structured as follows (listed in order of execution since some scripts have iter-dependencies):

- setup
  - `.python-version` declares the required Python version
  - `requirements.txt` declares the required Python packages and their versions
- data download
  - `data/fetch.py` downloads a subset of the ERA5 single-level and pressure-level datasets into the `data/` folder, please execute this script from inside the `data/` folder
- error tolerances
  - `bit-information-recommendations.ipynb` computes pointwise relative error tolerances from ERA5 ensemble means using the bit information method[^bit-information] and writes them to `recommendations/bit-information.yaml`
  - `data-limit-recommendations.ipynb` guesses data limits and writes them to `recommendations/data-limits.yaml`
  - `ensemble-spread-recommendations.ipynb` computes pointwise absolute/relative/quadratic error tolerances from ERA5 ensemble means and spreads and writes them to `recommendations/ensemble-spread.yaml`
  - `grib-linear-packing-recommendations.ipynb` computes range-relative error tolerances caused by linear packing in GRIB from a small sample of ERA5 reanalysis and ensemble means and spreads and writes them to `recommendations/grib-linear-packing.yaml`
- comparisons
  - `range.ipynb` computes the data range from ERA5 ensemble means and writes it to `expert-quantile-(single|pressure).csv`
  - `compression-ratio.ipynb` computes compression ratios for the ensemble-derived error tolerances and writes them to `compression-ratio-(single|pressure).csv`
  - `expert-quantile.ipynb` computes the quantiles of the expert tolerances amongst the ERA5 ensemble spreads and writes them to `expert-quantile-(single|pressure).csv`
- plotting
  - `compression-ratio-plots.ipynb` plots the compression ratios the ensemble-derived error tolerances and writes them to `plots/compression/*.pdf`
  - `mean-spread-plots.ipynb` plots the ERA5 ensemble mean-spread distributions and derived error tolerances and writes them to `plots/(single|pressure)/*.pdf` and `plots/legend.pdf`
  - `quantile-plots.ipynb` plots the expert quantiles and error tolerance comparisons and correlations and writes them to `plots/quantiles/*.pdf`
  - `plots.zip` contains all pre-computed plots

[^bit-information]: Klöwer, M., Razinger, M., Dominguez, J. J., Düben, P. D., & Palmer, T. N. (2021). Compressing atmospheric data into its real information content. *Nature Computational Science*, 1(11), 713–724. Available from: [doi:10.1038/s43588-021-00156-2](https://doi.org/10.1038/s43588-021-00156-2).


## Citation

Please refer to the [CITATION.cff](CITATION.cff) file and refer to <https://citation-file-format.github.io> to extract the citation in a format of your choice.


## License

Licensed under the Mozilla Public License, Version 2.0 ([LICENSE](LICENSE) or https://www.mozilla.org/en-US/MPL/2.0/).


## Funding

This research was conducted as part of [ESiWACE3](https://www.esiwace.eu), the third phase of the Centre of Excellence in Simulation of Weather and Climate in Europe.

Juniper Tyree, Sara Faghih-Naini, Peter Dueben, and Heikki Järvinen are funded by the ESiWACE3 Centre of Excellence. Funded by the European Union. This work has received funding from the European High Performance Computing Joint Undertaking (JU) under grant agreement No 101093054. This work received 50% complementary funding from the Research Council of Finland under grant No 359787.

Milan Klöwer acknowledges funding from the Natural Environment Research Council under grant number UKRI191.

Peter Dueben acknowledges funding from the WeatherGenerator Horizon Europe project (grant No 101187947).
