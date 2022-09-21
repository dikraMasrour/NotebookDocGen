#importing libs

# basic
import pandas as pd
import numpy as np
import json
import string
import pathlib

# cleaning & preprocessing
import re
import mdtex2html
import pyparsing
from langdetect import detect, DetectorFactory, detect_langs
from bs4 import BeautifulSoup
from cleantext import clean, cleantext


def check_ipynb(file_path):
    # check whether the input nb is a python notebook
    file_path = 'r' + file_path
    return file_path.endswith(".py") or file_path.endswith(".irnb") or file_path.endswith(".R") or file_path.endswith(".Rmd")



def check_lang_title(file_path):
    DetectorFactory.seed = 0
    # extract file name
    path = pathlib.PurePath(file_path)
    filename = str(path.name)
    filename = re.sub('-', ' ', filename)
    filename = re.sub('.ipynb', '', filename)
    return detect(filename) == 'en'




def check_lang_content(clean_md):
    DetectorFactory.seed = 0
    is_english = False
    # check notebook content for non english
    for row in clean_md.index:
        is_english = is_english + (detect(str(clean_md.loc[row])) == 'en')

    # we define a threshold of .80 for non english rows as the library results is not consistent
    if len(clean_md) != 0 :  is_english = (is_english / len(clean_md) > 0.80)
    else: is_english = True

    return is_english



def read_notebook_cells(file_path):
    # get notebook from path and return dataframe of all its cells 
    with open(file_path, 'r', encoding='utf-8') as nb:
        notebook = json.load(nb) # read JSON file from path (this is a dict)
        df = pd.DataFrame(notebook['cells'], columns=['cell_type', 'source']) # parse JSON into Pandas Dataframe

    return df

def check_source_format(df):
    # check whether the source is in list format and remove brackets
    for row in df.index:
        # print(type(str(df.loc[row, 'source'])))s
        if str(df.loc[row, 'source']).startswith("[") and str(df.loc[row, 'source']).endswith("]"):
            df.loc[row, 'source'] = ' '.join(df.loc[row, 'source'])

def remove_raw(df):
    # drop raw cell-types
    df.drop(df.index[df['cell_type'] == "raw"], inplace=True)


def remove_empty(df):
    # drop na rows
    # df['source'].dropna(inplace = True)
    df['source'].replace('', np.nan, inplace=True)
    df.dropna(subset = ['source'], inplace = True)



# to optimize time : only pass markdown rows 
def clean_markdown(md_df):
    clean_md = pd.DataFrame(columns=['source'])

    # patterns
    punctuation = r'[' + string.punctuation + ']'
    url = re.compile(r'https?://\S+|www\.\S+')
    latex_equation = r"(\$+)(?:(?!\1)[\s\S])*\1"
    author_name = r'(\s)@\w+'


    for row in md_df.index:
        clean_md.loc[len(clean_md)] = clean(re.sub(punctuation,' ',re.sub(author_name, r'\1',url.sub(r'',BeautifulSoup(mdtex2html.convert(re.sub("\$","",re.sub(latex_equation," ",re.sub('\n'," ",str(md_df.loc[row]), 0, re.MULTILINE)))), "lxml").text))), no_emoji=True)
    
    return clean_md

# to optimize time : only pass code rows 
def clean_code(code_df):
    clean_code = pd.DataFrame(columns=['source'])

    # comment pattern
    comment_filter = pyparsing.pythonStyleComment.suppress()

    for row in code_df.index:
        clean_code.loc[len(clean_code)] = re.sub(r"\n"," ",comment_filter .transformString(str(code_df.loc[row])))
    return clean_code


def preprocess(file_path):

    # if not check_lang_title(file_path):
    #     print('Preprocessing failed : Please enter an english notebook title')
    #     exit()

    raw_df = read_notebook_cells(file_path)
    remove_raw(raw_df)
    check_source_format(raw_df)
    remove_empty(raw_df)
    
    clean_md = clean_markdown(raw_df[raw_df['cell_type'] == 'markdown']['source'])
    # if not check_lang_content(clean_md):
    #     print('Preprocessing failed : Please enter an english notebook content')
    #     exit()

    clean_cd = clean_code(raw_df[raw_df['cell_type'] == 'code']['source'])
    clean_df = pd.concat([clean_md, clean_cd])
    clean_df.reset_index(drop=True, inplace=True)

    return clean_df