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
        


def show_upload_form(session_state):
    with st.container():
        st.markdown("## 📋 Upload your notebook")
        st.warning("Note : Not all notebooks have a specific Domain and Technique!")
    
        domain = st.checkbox('Domain')
        technique = st.checkbox('Technique')
        session_state.uploaded_file = st.file_uploader("Please upload a .ipynb file")
        # print(session_state.uploaded_file)
        if session_state.uploaded_file != None:
            bytes_data = session_state.uploaded_file.read()
            session_state.upload_submit_button = st.button("Let's go !")
    session_state.start_button = True

