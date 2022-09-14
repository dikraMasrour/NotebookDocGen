from distutils.command.clean import clean
from pyexpat import model
from typing import final
from transformers import AutoTokenizer, AutoModel, pipeline
import torch
import pandas as pd
import numpy as np


TOK = AutoTokenizer.from_pretrained("microsoft/codebert-base")
MODEL = AutoModel.from_pretrained("microsoft/codebert-base")



def embed_single_row(text):

    '''
    gets a text string (code or md) and the row index
    tests for sequences longer than 510 not to exceed the max_len limit of BERT model
    tokenizes and returns embeddings tensor
    
    '''
    
    nl_tokens = TOK.tokenize(text)

    # we choose max_len to be 510 as the tokenizer then adds 2 special tokens <s> and </s>
    if len(nl_tokens) > 510: 
        nl_tokens = nl_tokens[:510]

    tokens=[TOK.cls_token]+nl_tokens+[TOK.sep_token]

    tokens_ids = TOK.convert_tokens_to_ids(tokens)
    row_embeddings = MODEL(torch.tensor(tokens_ids)[None,:])[0]

    if row_embeddings is not None:
        return row_embeddings



def average_embeddings(embedding_tensor):

    '''
    gets the returned embeddings tensor of a sequence and averages it 
    to return one 768 dim vector for each row in the dataframe

    '''

    avg_rep = np.empty(1)
    if embedding_tensor is not None:
        if type(embedding_tensor) == torch.Tensor:
            # convert tensor into np array
            tensor_np = embedding_tensor.cpu().detach().numpy()
            # average of embeddings of the tokens in the sequence
            avg_rep = np.mean(tensor_np[0], axis=0)
        else: 
            tensor_np = embedding_tensor
            # average of embeddings of the tokens in the sequence
            avg_rep = np.mean(tensor_np, axis=0)
        # return average representation of a sequence of tokens
        return avg_rep


def embed_and_average_row(clean_df):
    row_avg_embedding = []
    for row in clean_df.index:
        embedding = embed_single_row(str(clean_df.loc[row]))
        row_avg_embedding.append(average_embeddings(embedding))
        # print(row)
        
    # build intermediary dataframe of averaged row vectors, titles and tags 
    vect_df = pd.DataFrame(row_avg_embedding)
    return vect_df



def embed_and_average_notebook(vect_df):
    vect_ntb = average_embeddings(vect_df)
    return vect_ntb


def build_input():
    vect_dim = 768
    features = []
    for i in range(vect_dim):
        features.append('num_feature_' + str(i))

    final_input = pd.DataFrame(columns=features)
    return final_input



def construct_final_input(vect_df):
    final_input = build_input()

    # for i in vect_df.index:
        # convert vector values to float
        # vect_df_float = []
        # vect_df_float.append([float(float_value) for float_value in vect_df.loc[i, 'notebook_vector'].strip('[]').split(',')])
        # # append tag to each notebook
        # vect_df[0].append(vect_df.loc[i, 'tag'])
    final_input.loc[len(final_input)] = list(vect_df)
    return final_input 



def embed(clean_df):
    vect_df = embed_and_average_row(clean_df)
    # print(vect_df)
    vect_ntb = embed_and_average_notebook(vect_df)
    # print(vect_ntb)
    return construct_final_input(vect_ntb)
    
