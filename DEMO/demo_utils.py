import streamlit as st
import json
from strimlitbook.reader import read_ipynb
import torch
from transformers import AutoTokenizer, AutoModel, pipeline
from transformers import PLBartForConditionalGeneration, PLBartTokenizer


PLBARTOKENIZER = PLBartTokenizer.from_pretrained("uclanlp/plbart-python-en_XX", src_lang="python", tgt_lang="en_XX")
PLBARTMODEL = PLBartForConditionalGeneration.from_pretrained("uclanlp/plbart-python-en_XX")


def switch_page(page_name: str):
    from streamlit import _RerunData, _RerunException
    from streamlit.source_util import get_pages

    def standardize_name(name: str) -> str:
        return name.lower().replace("_", " ")

    page_name = standardize_name(page_name)

    pages = get_pages("demo.py")  # OR whatever your main page is called

    for page_hash, config in pages.items():
        if standardize_name(config["page_name"]) == page_name:
            raise _RerunException(
                _RerunData(
                    page_script_hash=page_hash,
                    page_name=page_name,
                )
            )

    page_names = [standardize_name(config["page_name"]) for config in pages.values()]

    raise ValueError(f"Could not find page {page_name}. Must be one of {page_names}")


def initialize_session(session_state):
    if 'start_button' not in session_state:
        session_state.start_button = False
    if 'upload_submit_button' not in session_state:
        session_state.upload_submit_button = False
    if 'uploaded_file' not in session_state:
        session_state.uploaded_file = None
    if 'uploaded_file_name' not in session_state:
        session_state.uploaded_file_name = ' '
    if 'go_back_main' not in session_state:
        session_state.go_back_main = False
    if 'go_back_main02' not in session_state:
        session_state.go_back_main02 = False
    if 'codeCells' not in st.session_state:
        st.session_state.codeCells = {}
    if 'domain' not in st.session_state:
        st.session_state.domain = 'No domain'
    if 'technique' not in st.session_state:
        st.session_state.technique = 'No technique'
    if 'both' not in st.session_state:
        st.session_state.both = 'No domain or technique'
    if 'documented' not in st.session_state:
        st.session_state.documented = False
    if 'doc_displayed' not in st.session_state:
        st.session_state.doc_displayed = False
    if 'domain' not in st.session_state:
        st.session_state.domain = None
    if 'technique' not in st.session_state:
        st.session_state.technique = None
    if 'classified' not in st.session_state:
        st.session_state.classified = False


def show_upload_form(session_state):
    with st.container():
        # upload icon
        upload_title = load_text('DEMO/streamlit_awesome-main/upload_icon.md')
        st.write(upload_title, unsafe_allow_html=True)

        st.warning("Note : Not all notebooks have a specific Domain and Technique!")

        session_state.uploaded_file = st.file_uploader("Please upload a .ipynb file", accept_multiple_files=False, type='ipynb')
        
        if session_state.uploaded_file != None:
            session_state.uploaded_file_name = session_state.uploaded_file.name
            session_state.uploaded_file = session_state.uploaded_file.read()
            session_state.upload_submit_button = st.button("Let's go !")
            if session_state.upload_submit_button:
                switch_page('upload_nb_page')


def load_text(file_path):
    """A convenience function for reading in the files used for the site's text"""
    with open(file_path) as in_file:
        return in_file.read()



def prep_classification(contents):
        
        contents = contents.replace(']', '')
        contents = contents.replace('[', '')
        contents = contents.replace('\n', '')  
        contents = contents.replace('"', '')
        contents = contents.replace('(', '')
        contents = contents.replace(')', '')
        contents = contents.replace("'", '')
        list = contents.split(',')
        print(list)
        domain = list[0].strip().capitalize()
        technique = list[1].strip().capitalize()
        return domain, technique



def display_nb():
    # load user's notebook as json
    byte_nb = st.session_state.uploaded_file
    json_nb = json.loads(byte_nb)

    # dump it locally 
    with open('dump.json', 'w+', encoding='utf-8-sig') as json_dump:
        json.dump(json_nb, json_dump)  

    nb = read_ipynb('dump.json')
    nb.display()



def display_gen_nb():
    # # load user's notebook as json
    # byte_nb = st.session_state.gen_uploaded_file
    # json_nb = json.loads(byte_nb)

    # dump it locally 
    # with open('dump_PLBART_documented.ipynb', 'w+', encoding='utf-8-sig') as json_dump:
    #     json.dump(json_nb, json_dump)  

    with open('dump_PLBART_documented.ipynb', encoding='utf-8-sig') as doc_nb:
        btn = st.download_button(
        label="Download your documented notebook here !",
        data=doc_nb,
        file_name=str(st.session_state.uploaded_file_name) + '_PLBART_documented.ipynb',
        mime='application/ipynb+json'
        )

    nb = read_ipynb('dump_PLBART_documented.ipynb')
    nb.display()
    