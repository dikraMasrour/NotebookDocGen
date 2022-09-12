#importing libs

# basic
import pandas as pd
import numpy as np
import os 
import pickle
import json
import string
import warnings

# cleaning & preprocessing
import re
import mdtex2html
import pyparsing
from langdetect import detect, DetectorFactory
from bs4 import BeautifulSoup
from cleantext import clean

# embedding
import torch
from transformers import AutoTokenizer, AutoModel, pipeline

#define VARs
DATA_PATH_INPUT = ""
DATA_PATH_OUTPUT = ""
PATTERN = r'[' + string.punctuation + ']'
COMMENT_FILTER = pyparsing.pythonStyleComment.suppress()
RMV_URL = re.compile(r'https?://\S+|www\.\S+')
RMV_EQU = r"(\$+)(?:(?!\1)[\s\S])*\1"
tokenizer = AutoTokenizer.from_pretrained("microsoft/codebert-base")
model = AutoModel.from_pretrained("microsoft/codebert-base")
DetectorFactory.seed = 0
warnings.filterwarnings('ignore')

#notebook cleaning
def cleaning_ntbk(df,raw_df):
    for i in raw_df.index:

        #CLEANING FOR MARKDOWN CELLS 

        if raw_df.loc[i]['cell_type'] == 'markdown':
             
            ''' 
            # Equations remover
            raw_df.loc[i]['source'] = re.sub(RMV_EQU," ",str(raw_df.loc[i]['source']), 0, re.MULTILINE)
            # $ Remover to avoid conflicts
            re.sub("\$","",re.sub(RMV_EQU," ",string, 0, re.MULTILINE))
            # Latex converter to HTML
            raw_df.loc[i]['source'] = mdtex2html.convert(re.sub("\$",""(str(raw_df.loc[i]['source'])))
            # HTML's tags remover
            raw_df.loc[i]['source'] = BeautifulSoup(mdtex2html.convert(re.sub("\$",""(str(raw_df.loc[i]['source']))), "lxml").text
            # URLs - Names of authors - Punctuation & special caracters Remover
            raw_df.loc[i]['source'] = re.sub(PATTERN,'',re.sub(r'(\s)@\w+', r'\1',RMV_URL.sub(r'',str(raw_df.loc[i]['source']))))
            # Emojis Remover
            raw_df.loc[i]['source'] = clean(re.sub(PATTERN,'',re.sub(r'(\s)@\w+', r'\1',RMV_URL.sub(r'',BeautifulSoup(mdtex2html.convert(mdtex2html.convert(re.sub(RMV_EQU," ",str(raw_df.loc[i]['source']), 0, re.MULTILINE))), "lxml").text))), no_emoji=True)
            '''
            
            df.loc[len(df)]=[raw_df.loc[i]['cell_type'],clean(re.sub(PATTERN,' ',re.sub(r'(\s)@\w+', r'\1',RMV_URL.sub(r'',BeautifulSoup(mdtex2html.convert(re.sub("\$","",re.sub(RMV_EQU," ",re.sub('\n'," ",str(raw_df.loc[i]['source']), 0, re.MULTILINE)))), "lxml").text))), no_emoji=True)]
        

        #CLEANING FOR CODE CELLS
        elif raw_df.loc[i]['cell_type'] == 'code' :
            df.loc[len(df)]=[raw_df.loc[i]['cell_type'],re.sub(r"\n"," ",COMMENT_FILTER .transformString(str(raw_df.loc[i]['source'])))]



DATA_PATH_INPUT = "C:/Users/zdahmani/Documents/Documentation_generator_project/NotebookCodeGen/Scripts/Classification_Task/data/clustering/flight-crash-investigation.ipynb"
DATA_PATH_OUTPUT = "C:/Users/zdahmani/Documents/Documentation_generator_project/NotebookCodeGen/Scripts/Classification_Task/data/test.csv"

df = pd.DataFrame(columns=['cell-type','source'])

with open(DATA_PATH_INPUT, encoding="utf8") as jsonfile:
    data_ = json.load(jsonfile)
raw_df = pd.json_normalize(data_['cells'])


cleaning_ntbk(df,raw_df)
 

c = 0
for i in df.index:
    if df.loc[i]['cell-type'] == "raw" :
        c+=1

if c!=0 :
    df.drop(df[df['cell-type'] == "raw"], inplace=True)



#Embedding
def embed_single_row(text, row):

    '''
    gets a text string (code or md) and the row index
    tests for sequences longer than 510 not to exceed the max_len limit of BERT model
    tokenizes and returns embeddings tensor
    
    '''
    
    nl_tokens = tokenizer.tokenize(text)

    # we choose max_len to be 510 as the tokenizer then adds 2 special tokens <s> and </s>
    if len(nl_tokens) > 510: 
        nl_tokens = nl_tokens[:510]

    tokens=[tokenizer.cls_token]+nl_tokens+[tokenizer.sep_token]

    tokens_ids = tokenizer.convert_tokens_to_ids(tokens)
    row_embeddings = model(torch.tensor(tokens_ids)[None,:])[0]

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


row_avg_embedding = []
for row in df.index:
    embedding = embed_single_row(df.loc[row, 'source'], row)
    row_avg_embedding.append((average_embeddings(embedding)))
    
# build intermediary dataframe of averaged row vectors, titles and tags 
interm_df = pd.DataFrame(row_avg_embedding, columns = ['row_vector'])



#Final df
def build_df():
    vect_dim = 768
    features = []
    for i in range(vect_dim):
        features.append('num_feature_' + str(i))
    final_df = pd.DataFrame(columns=features)
    return final_df


def construct_final_df(vect_data):
    final_df = build_df()
    for i in vect_data.index:
        # convert vector values to float
        vect_data_float = []
        vect_data_float.append([float(float_value) for float_value in vect_data.loc[i, 'notebook_vector'].strip('[]').split(',')])
        # append tag to each notebook
        vect_data_float[0].append(vect_data.loc[i, 'tag'])
        final_df.loc[len(final_df)] = vect_data_float[0]
        print(i)
    return final_df 


final_df = construct_final_df(interm_df)


final_df.to_csv(DATA_PATH_OUTPUT)