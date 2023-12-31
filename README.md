# E-nose Data Analysis [![Tests](https://github.com/aungkhantmaw64/enose-data-analysis/actions/workflows/tests.yml/badge.svg)](https://github.com/aungkhantmaw64/enose-data-analysis/actions)
## Introduction
This repository contains analytics for the experimental ordor dataset I created using the hybrid-electronic nose designed as an aiding device for non-invasive diaganosis. I published an IEEE research article as a main author based on this device and the code used for the analytics of the dataset can be found in this repo. For the published article, please refer to https:/ieeexplore.ieee.org/document/9495905.

## Building the Docker Image
```bash
docker build --progres tty -t data-analysis-ci:latest .
```

## Running the Container

### Windows (Powershell)
```bash
docker container run --name data_analysis_ci --rm -it -v $PWD:/app data-analysis-ci:latest bash
```
