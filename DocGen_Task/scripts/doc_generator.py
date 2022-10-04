import nbformat as nbf
from transformers import PLBartForConditionalGeneration, PLBartTokenizer
import pandas as pd


PLBARTTOKENIZER = PLBartTokenizer.from_pretrained("uclanlp/plbart-python-en_XX", src_lang="python", tgt_lang="en_XX")
PLBARTMODEL = PLBartForConditionalGeneration.from_pretrained("uclanlp/plbart-python-en_XX")

def check_ipynb(file_path):
    print('Checking file format ...')
    # check whether the input nb is a python notebook
    file_path = 'r' + file_path
    return file_path.endswith(".py") or file_path.endswith(".irnb") or file_path.endswith(".R") or file_path.endswith(".Rmd")




def generate_doc(c):
    doc = ''
    doc_string = ''
    try :
        inputs = PLBARTTOKENIZER(c, return_tensors="pt")
        translated_tokens = PLBARTMODEL.generate(**inputs, decoder_start_token_id=PLBARTTOKENIZER.lang_code_to_id["en_XX"], max_new_tokens=1024)

        doc = nbf.v4.new_markdown_cell(PLBARTTOKENIZER.batch_decode(translated_tokens, skip_special_tokens=True)[0])
        doc_string = PLBARTTOKENIZER.batch_decode(translated_tokens, skip_special_tokens=True)[0]
    except Exception as e:
        print(c, e)

    return (doc, doc_string)

def remove_markdown_cells(notebook):
    print('Removing markdown cells ...')
    new_notebook = notebook
    new_notebook.cells = [cell for cell in new_notebook.cells if cell.cell_type != "markdown"]
    return new_notebook


def is_all_commented(source):
    is_commented = True
    for line in source.splitlines():
        is_commented = is_commented and (str(line).startswith('#'))

    return is_commented



def remove_commented_cells(notebook):
    print('Removing entirely commented cells ...')
    new_notebook = notebook
    new_notebook.cells = [cell for cell in new_notebook.cells if not (is_all_commented(str(cell.source)))]
    return new_notebook



def document_notebook(notebook_file):

    notebook = nbf.read(notebook_file, as_version=4)
    # new_notebook = remove_commented_cells(notebook)
    # new_notebook = remove_markdown_cells(new_notebook)
    code_cells = notebook.cells 

    print('Generating documentation using PLBart ...')
    
    print('Documenting the notebook ...')
    for cell in list(code_cells):
        if cell.get('cell_type') == 'code':
            # print(code_cells.index(cell), cell)

            doc = generate_doc(cell.get('source'))[0]
            doc.source = '\U0001FA84' + doc.source 
            # print(doc)
            
            notebook.cells.insert(code_cells.index(cell), doc)
            # break
            
    
    if '.json' in str(notebook_file):
        notebook_file = str(notebook_file).rstrip('.json')
    elif '.ipynb' in str(notebook_file):
        notebook_file = str(notebook_file).rstrip('.ipynb')

    filename = notebook_file + '_PLBART_documented.ipynb' 
    nbf.write(notebook, filename)
    print('Documenting the notebook : DONE')
    return filename



def document_code_cell(code_series):

    doc_list = []
    for code in code_series:
        if is_all_commented(str(code)):
            doc_list.append('commented')
        
        (doc, docstring) = generate_doc(code)

        # print(docstring)

        doc_list.append(docstring)
    
    doc_series = pd.Series(doc_list)
    return doc_series
        
