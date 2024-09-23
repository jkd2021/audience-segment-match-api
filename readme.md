# Semantic Audience Matching API

This project implements a containerized Python Flask API that performs semantic matching between audience segments. 
It allows users to provide a list of audience segment descriptions as input and returns the best match from a given 
source list, along with a similarity score indicating the confidence of matching.

## Directory Structure

- working-dir/
  - api.py # API code
  - test_api.py # unit tests for API
  - requirements.txt # API dependencies
  - Dockerfile # Docker build file
  - test_audiences.json # test segments
  - source_segments.csv # source list of segments
  - README.md # readme file


## Assumptions

### 1. Files

- test_audiences.json & source_segments.csv already in the working directory

### 2. Toolkits

- python 3.9 is used
- use Flask to build API


## Prerequisites

### Libraries:

- **flask**: as the framework for this light API
- **pandas**: data extraction from csv
- **numpy**: similarity calculation



## Instructions of API

### 1. Clone the Repository

First, clone this repository from GitHub:
> git clone https://github.com/jkd2021/audience-segment-match-api.git \
cd audience-segment-match-api
