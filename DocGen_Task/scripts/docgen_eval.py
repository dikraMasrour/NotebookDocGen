import pandas as pd
import numpy as np
import doc_generator as dg
import argparse




def read_pairs(file_path):
    data_ref_pairs = pd.read_csv(file_path, index_col = 0)[['markdown', 'code']]
    return data_ref_pairs


def main():

    # Initialize parser
    parser = argparse.ArgumentParser()
    # Adding optional argument
    parser.add_argument("path", help = "Path to csv file")
    # Read arguments from command line
    args = parser.parse_args()

    data = read_pairs(args.path)
    # print(data)


    doc_series = dg.document_code_cell(data.code)

    data['generated_doc'] = doc_series

    data[['markdown', 'generated_doc']].to_csv('../data/generated_doc.csv')


if __name__ == "__main__":
    main()


'''
generated documentation has been evaluated against the references
using BERT_score

'''