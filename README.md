# SniffIt-AI
[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/aungkhantmaw64/SniffIt-ai/main)

## Introduction
This repository contains analytics for the experimental ordor dataset I created using the hybrid-electronic nose designed as an aiding device for non-invasive diaganosis. I published an IEEE research article as a main author based on this device and the code used for the analytics of the dataset can be found in this repo. For the published article, please refer to https://ieeexplore.ieee.org/document/9495905.

## Building the Docker Image
```bash
docker build --progress tty -t data-analysis-ci:latest .
```

## Running the Container

### Windows (Powershell)
```bash
docker container run -p 8888:8888 --name data_analysis_ci --rm -it -v ${pwd}:/app data-analysis-ci:latest bash
```

## Running Jupyter Notebook
```bash
jupyter notebook --allow-root --ip 0.0.0.0 --port 8888
```