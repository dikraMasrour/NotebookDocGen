import streamlit as st



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


def show_upload_form(session_state):
    with st.container():
        upload_title = load_text('streamlit_awesome-main\\upload_icon.md')
        st.write(upload_title, unsafe_allow_html=True)
        st.warning("Note : Not all notebooks have a specific Domain and Technique!")

        session_state.uploaded_file = st.file_uploader("Please upload a .ipynb file")
        # print(session_state.uploaded_file)
        if session_state.uploaded_file != None:
            # print(session_state.uploaded_file)
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
        domain = list[0]
        technique = list[1]
        return domain, technique