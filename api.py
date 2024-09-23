import pandas as pd
import numpy as np
import gensim.downloader as model_api
from flask import Flask, request, jsonify
from sklearn.metrics.pairwise import cosine_similarity

app = Flask(__name__)

# extract segment data from source_segments.csv
source_segments = pd.read_csv("./source_segments.csv")["descriptions"].tolist()

# configurations of the NLP model
nlp_model_name = "glove-wiki-gigaword-50"

# automatically download & load pretrained NLP model for word embedding
word_embed_model = model_api.load(nlp_model_name)
print("Loaded word embedding model from {}".format(model_api.load(nlp_model_name, return_path=True)))


def vectorize(segment: str):
    """
    Vectorization of a given segment
    :param segment: a given segment
    :return: mean_vector: mean word vector of the given segment
    """

    # split the segment into words
    words = segment.split()

    # vectorize the words using nlp model
    vectors = []
    for word in words:
        if word in word_embed_model:  # append word's vector if it's included in the nlp model's vocabulary
            vectors.append(word_embed_model[word])

    # worst case: no word vector found, return zeros, assumed as never happening
    if not vectors:
        vectors = np.zeros(word_embed_model.vector_size)

    # obtain the mean vector of all words in the segment to represent the entire segment
    mean_vector = np.mean(vectors, axis=0)

    return mean_vector


def calculate_similarity(input_seg: list[str], source_seg: list[str]):
    """
    Similarity calculation of vectorized input and source segments
    :param input_seg: a list of segments from input json
    :param source_seg: a list that refers to the source segments in source_segments.csv
    :return: similarity_scores: an array of similarity scores between input and source
    """

    input_vectors = np.array([vectorize(seg) for seg in input_seg])  # vectorize input segments
    source_vectors = np.array([vectorize(seg) for seg in source_seg])  # vectorize source segments
    similarity_scores = cosine_similarity(input_vectors, source_vectors)  # calculate cosine similarity

    return similarity_scores


@app.route('/match', methods=['POST'])
def match_audience_segments():
    """
    Semantic matching API for audience segments.
    """
    data = request.json
    input_segments = data.get('input_segments')

    if not input_segments:
        return jsonify({'error': 'No input segments given.'}), 400

    # get similarity scores between input and source segments
    similarity_scores = calculate_similarity(input_segments, source_segments)

    # get the best matches for each input segment
    best_matches = []
    for i, scores in enumerate(similarity_scores):

        # get the best match's index for each input segment
        best_index = scores.argmax()

        # get the best match
        best_match = {
            "input_segment": input_segments[i],
            "best_match": source_segments[best_index],
            "similarity_score": float(scores[best_index])
        }

        best_matches.append(best_match)

    return jsonify({'best_matches': best_matches})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)