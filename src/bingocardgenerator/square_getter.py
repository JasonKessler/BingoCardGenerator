from typing import List

import numpy as np

from scattertext import CohensD


def filter_candidates(candidates: List[str]) -> List[str]:
    filtered_candidates: List[str] = []
    for i, candidate in enumerate(candidates):
        if not any(candidate in other_candidate for other_candidate in candidates[i + 1:] + filtered_candidates):
            filtered_candidates.append(candidate)
    return filtered_candidates

class SquareGetter:
    def __init__(self, corpus):
        '''

        :param corpus: a Scattertext Corpus object

        '''
        self._corpus = corpus

    def generate_squares(
            self,
            num_squares=25,
            percentage_of_candidate_list_to_consider=3.,
            shuffle=True
    ):
        categories = self._corpus.get_term_freq_df('').sum().sort_values(ascending=False).index
        n_cats = len(categories)
        scores = {}
        for cat in categories:
            candidates = list(
                self._get_category_scores(cat)
            )[:int(percentage_of_candidate_list_to_consider * num_squares / n_cats)]

            filtered_candidates = filter_candidates(candidates)
            if shuffle:
                np.random.shuffle(filtered_candidates)
            scores[cat] = filtered_candidates

        to_ret = []
        cur_pos = 0
        for i in range(num_squares):
            if i > 0 and i % n_cats == 0: cur_pos += 1
            cat = categories[i % n_cats]
            to_ret.append(cat + ': ' + scores[cat][cur_pos])
        return to_ret

    def _get_category_scores(self, cat):
        return CohensD(self._corpus).set_categories(
            cat
        ).get_score_df().sort_values(
            by='cohens_d', ascending=False
        ).index
