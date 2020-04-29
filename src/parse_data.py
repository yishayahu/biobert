import json
import os
import argparse
import warnings
import pickle


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--path", help="path to data_jsons", type=str, default='/home/yishayahu/biobert/data'
                                                                               '/comm_use_subset/comm_use_subset/pmc_json')
    parser.add_argument("--use_cache", help="use pickle cache sents", type=bool, default=False)
    return parser.parse_args()


def sents_from_data():
    args = parse_args()
    sents = []
    if args.use_cache:
        if not os.path.exists(os.path.join(os.path.abspath(os.getcwd()), "sents.p")):
            raise Exception("cache not exist")
        sents = pickle.load(open("sents.p", 'rb'))
    else:
        for file_path in os.listdir(args.path):
            print("parsing file {file_name}".format(file_name=file_path))
            file_full_path = os.path.join(args.path, file_path)
            assert os.path.isfile(file_full_path)
            json_file = json.load(open(file_full_path, 'r'))
            if "body_text" not in json_file:
                warnings.warn("file {file_name} not in the right format".format(file_name=file_path))
            body_text = json_file["body_text"]
            for item in body_text:
                if "text" not in item:
                    warnings.warn("body_text do not contain any text")
                sents.append(item["text"])
        pickle.dump(sents, open("sents.p", 'wb'))
    return sents


if __name__ == '__main__':
    sents_from_data()
