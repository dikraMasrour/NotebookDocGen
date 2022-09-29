from opcode import stack_effect
from numpy import byte
import streamlit as st
from streamlit_ace import st_ace
import demo_utils as du
from strimlitbook.reader import read_ipynb
import json
import streamlit_modal as sm
import streamlit.components.v1 as components

DUMP_PATH = 'C:\\Users\\zbook\\Documents\\GitHub\\NotebookDocGen\\UI\\'

st.set_page_config(
    page_title="Magic notebook",
    page_icon="✨",
)


# session state initializing
du.initialize_session(st.session_state)



if st.session_state.uploaded_file == None:
    st.error('No file has been uploaded. Please navigate to the main page and upload a notebook.')
    st.session_state.go_back_main =  st.button('Main page')
    if st.session_state.go_back_main:
        du.switch_page('demo')
else:

    indent, class_but, doc_but = st.columns([5, 1, 2], gap='small')

    with class_but:
        st.button('Classify')
    with doc_but:
        st.button('Generate doc')



    byte_nb = st.session_state.uploaded_file
    json_nb = json.loads(byte_nb)

    with open(DUMP_PATH + 'dump.json', 'w', encoding='utf-8-sig') as json_dump:
        json.dump(json_nb, json_dump)
# print(json_nb)


## TODO : convert byte data to nb or json locally then pass path to strimlitbook


    nb = read_ipynb(DUMP_PATH + 'dump.json')
    nb.display()

# st.title("Generated documentation for your DS & ML notebooks")
# st.header("")


# with st.expander(" About the app"):

#     st.write(
#         """     

# The *Generated documentation for your DS & ML notebooks* app is an easy-to-use interface where you can uploade your notebook containning only code cells and get in return a commented notebook !

# 	    """
#     )



