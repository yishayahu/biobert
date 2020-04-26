from typing import Set, Any

from gensim.models import KeyedVectors
from gensim.models.keyedvectors import Word2VecKeyedVectors
from nltk import word_tokenize
import nltk

nltk.download('stopwords')
nltk.download('punkt')
from nltk.corpus import stopwords
from string import punctuation


class Word2VecModel:

    def __init__(self, path="C:\\Users\\Y\\PycharmProjects\\covid_nlp\\BioWordVec_PubMed_MIMICIII_d200.vec.bin"):
        self.word_vector = KeyedVectors.load_word2vec_format(path, binary=True)
        self.stop_words = set(stopwords.words('english'))
        self.exist_counter = 0
        self.not_exist_counter = 0

    def get_vec(self, token):
        assert type(token) == str
        token = token.lower()
        if token in self.word_vector:
            self.exist_counter += 1
            return self.word_vector[token]
        else:
            self.not_exist_counter += 1
            return []

    def get_sent_vec(self, sent):
        sent_vec = []
        for token in word_tokenize(sent):
            if token not in punctuation and token not in self.stop_words:
                res = self.get_vec(token=token)
                if res:
                    sent_vec.append(res)

    def corpus_to_mat(self, corpus):
        data_matrix = []
        for sent in corpus:
            print("curr sent is {}".format(sent))
            data_matrix.append(self.get_sent_vec(sent))
        return data_matrix

    def print_counter(self):
        print(self.exist_counter)
        print(self.not_exist_counter)
