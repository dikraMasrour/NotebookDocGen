import nbformat as nbf
from transformers import PLBartForConditionalGeneration, PLBartTokenizer



def check_ipynb(file_path):
    print('Checking file format ...')
    # check whether the input nb is a python notebook
    file_path = 'r' + file_path
    return file_path.endswith(".py") or file_path.endswith(".irnb") or file_path.endswith(".R") or file_path.endswith(".Rmd")




def generate_doc(c):
    
    plbarttokenizer = PLBartTokenizer.from_pretrained("uclanlp/plbart-python-en_XX", src_lang="python", tgt_lang="en_XX")
    plbart_model = PLBartForConditionalGeneration.from_pretrained("uclanlp/plbart-python-en_XX")

    inputs = plbarttokenizer(c, return_tensors="pt")
    translated_tokens = plbart_model.generate(**inputs, decoder_start_token_id=plbarttokenizer.lang_code_to_id["en_XX"], max_new_tokens=20)

    doc = nbf.v4.new_markdown_cell(plbarttokenizer.batch_decode(translated_tokens, skip_special_tokens=True)[0])
    
    return doc

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
    # print(notebook['cells'][1].get('cell_type'))
    # print(type(notebook.cells), len(notebook.cells), notebook.cells)

    

    # fname = notebook_file

    notebook = nbf.read(notebook_file, as_version=4)
    new_notebook = remove_commented_cells(notebook)
    new_notebook = remove_markdown_cells(notebook)
    code_cells = new_notebook.cells 

    print('Generating documentation using PLBart ...')
    
    print('Documenting the notebook ...')
    for cell in list(code_cells):
        if cell.get('cell_type') == 'code':
            # print(code_cells.index(cell), cell)

            doc = generate_doc(cell.get('source'))
            # print(doc)
            new_notebook.cells.insert(code_cells.index(cell), doc)
            # break
            
    filename = notebook_file + 'PLBART_documented.ipynb' 

    nbf.write(new_notebook, filename, version=nbf.NO_CONVERT)
    print('Documenting the notebook : DONE')
    return filename

