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

- test_audiences.json & source_segments.csv already in the working directory (the contents are pure english words, no preprocessing required)

### 2. Toolkits

- python 3.9 is used
- use Flask to build API
- the GloVe model from gensim
- use scikit-learn cosine similarity calculation

### 2. Used methods

- use a word vectorizing model, here a pretrained GloVe model (65MB, light-weighted compared to Word2Vec or BERT), to embed words to vectors in a segment
- all words are assumed to be included in the model's vocabulary
- use the mean value of all word vectors in a segment to represent the segment in high-dimension space
- use cosine similarity to calculate matching confidences among segments


## Prerequisites

### Libraries:

- **flask**: as the framework for this light API
- **pandas**: data extraction from csv
- **numpy**: similarity calculation
- **gensim**: accessing word vectorizing model
- **scikit-learn**: similarity calculation among the segments


## Instructions of API

### 1. Clone the Repository

First, clone this repository from GitHub:
> git clone https://github.com/jkd2021/audience-segment-match-api.git \
cd audience-segment-match-api
