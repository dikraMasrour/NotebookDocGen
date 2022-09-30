import subprocess
from numpy import byte
import streamlit as st
from streamlit_ace import st_ace
import demo_utils as du
from strimlitbook.reader import read_ipynb
import json
import os


# '''TODO : 
#  prep help strings 
#  implement models
# '''

DUMP_PATH_COM = r'C:\Users\dmasrour\Documents\NotebookDocGen\DEMO'
DUMP_PATH = 'C:\\Users\\dmasrour\\Documents\\NotebookDocGen\\DEMO\\'
RUN_PATH = r'C:\Users\dmasrour\Documents\NotebookDocGen\Classification_Task\notebooks\scripts\run.py'


st.set_page_config(
    page_title="Magic notebook",
    page_icon="✨",
)


st.sidebar.markdown("# Upload your notebook Page🎉")


# session state initializing
du.initialize_session(st.session_state)


if st.session_state.uploaded_file == None:
    st.error('No file has been uploaded. Please navigate to the main page and upload a notebook.')
    st.session_state.go_back_main =  st.button('Main page')
    if st.session_state.go_back_main:
        du.switch_page('demo')
else:

    indent, top_class_but, top_doc_but, top_go_but = st.columns([2, 5, 4, 1], gap='small')

    with indent:
        st.write(' ')
        st.write(' ')
        st.session_state.go_back_main02 =  st.button('Upload another notebook')
        if st.session_state.go_back_main02:
            du.switch_page('demo')
    with top_class_but:
        classify = st.multiselect('Classify the notebook by', ['Domain', 'Technique'], help='help')
    with top_doc_but:
        gendoc = st.selectbox('Generate documentation using', ('-', 'PLBART'), help='help')
    with top_go_but:
        if (len(classify) != 0) | (gendoc != '-'):
            st.write(' ')
            st.write(' ')
            top_go_button = st.button('Go!')
    
  

    byte_nb = st.session_state.uploaded_file
    json_nb = json.loads(byte_nb)

    with open(DUMP_PATH + 'dump.json', 'w+', encoding='utf-8-sig') as json_dump:
        json.dump(json_nb, json_dump)


    if ('Domain' in classify) and (len(classify) == 1) and (top_go_button):
        os.system('python ' + RUN_PATH + ' ' + DUMP_PATH_COM + '\dump.json ' + '--class domain >> file.txt')
        with open('file.txt') as f:
            contents = str(f.readlines()[-1])

        dom, tech = du.prep_classification(contents)
        st.session_state.domain = dom
        # horizontal divider
        '''
        ---
        '''
        st.write("Your notebook's domain is : ", st.session_state.domain.strip().capitalize())
        '''
        ---
        '''

    elif ('Technique' in classify) and (len(classify) == 1) and (top_go_button):
        os.system('python ' + RUN_PATH + ' ' + DUMP_PATH_COM + '\dump.json ' + '--class technique >> file.txt')
        with open('file.txt') as f:
            contents = str(f.readlines()[-1])

        dom, tech = du.prep_classification(contents)
        st.session_state.technique = tech
        # horizontal divider
        '''
        ---
        '''
        st.write("Your notebook's technique is : ", st.session_state.technique.strip().capitalize())
        '''
        ---
        '''

    elif ('Technique' in classify) and ('Domain' in classify) and (top_go_button):
        os.system('python ' + RUN_PATH + ' ' + DUMP_PATH_COM + '\dump.json ' + '--class both >> file.txt')
        with open('file.txt') as f:
            contents = str(f.readlines()[-1])

        dom, tech = du.prep_classification(contents)
        dom, tech = str(dom).strip().capitalize(), str(tech).strip().capitalize()
        st.session_state.both = (dom, tech)
        # horizontal divider
        '''
        ---
        '''
        st.write("Your notebook's domain & technique are : ", st.session_state.both[0], ' & ', st.session_state.both[1])
        '''
        ---
        '''



    nb = read_ipynb(DUMP_PATH + 'dump.json')
    nb.display()