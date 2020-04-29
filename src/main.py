import src
import pickle
if __name__ == '__main__':
    print("parsing data")
    sents = src.parse_data.sents_from_data()
    # print("loading model")
    # word2vec = Word2VecModel()
    # print("predict corpus")
    # data_matrix = word2vec.corpus_to_mat(sents)
    # pickle.dump(data_matrix, open("data_matrix.p", 'wb'))
    # print("print conters")
    # word2vec.print_counter()


