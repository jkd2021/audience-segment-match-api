import pandas as pd
import numpy as np
from flask import Flask, request, jsonify

app = Flask(__name__)

# extract segment data from source_segments.csv
source_segments = pd.read_csv("./source_segments.csv")["descriptions"].tolist()


def calculate_similarity(input_seg: list[str], source_seg: list[str]):
    """
    Similarity calculation of vectorized input and source segments
    :param input_seg: a list of segments from input json
    :param source_seg: a list that refers to the source segments in source_segments.csv
    :return: similarity_scores: an array of similarity scores between input and source
    """

    # TODO: apply matching algorithm here (here is only a test code)
    similarity_scores = np.ones((len(input_seg), len(source_seg)))
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
            "similarity_score": scores[best_index]
        }

        best_matches.append(best_match)

    return jsonify({'best_matches': best_matches})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)